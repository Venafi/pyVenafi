from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Set
import pyodbc
import pandas as pd
import re
from argparse import ArgumentParser
import urllib.request
import ssl
from lxml import etree
from concurrent.futures.thread import ThreadPoolExecutor
from packaging.version import Version
from pathlib import Path
from threading import Lock

PRINT_LOCK = Lock()

DB_ADDRESS = '10.100.205.56'
DB_NAME = 'tpp'
DB_USERNAME = 'sa'
DB_PASSWORD = 'newPassw0rd!'


@dataclass
class Option:
    name: str
    schema_version: str = None


@dataclass
class Node:
    name: str
    parents: List[Node] = field(default_factory=list)
    children: List[Node] = field(default_factory=list)
    options: List[Option] = field(default_factory=list)


class UpdateConfig:
    def __init__(self, version: str, update_pkcs11: bool):
        sql = pyodbc.connect(
            p_str='',
            server=DB_ADDRESS,
            port=1433,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            driver='SQL Server',
            autocommit=True
        )

        cursor = sql.cursor()
        cursor.execute(f"""
            select *
            from config_relations
        """)
        try:
            response = list(cursor)
        except:
            response = None
        sql.commit()
        sql.close()
        columns = [x[0] for x in cursor.description]
        core_results = response
        if update_pkcs11:
            pkcs11_results = self.add_pkcs11_vse()
            all_results = core_results + pkcs11_results
        else:
            all_results = core_results
        results = dict(zip(columns, zip(*all_results)))
        self.config_relations = pd.DataFrame(results)
        self.version = Version(version)
        self.all_classes = []

    @classmethod
    def add_pkcs11_vse(cls):
        sql = pyodbc.connect(
            p_str='',
            server='10.100.206.17',
            port=1433,
            database='TPP',
            user='sa',
            password='P@ssw0rd!',
            driver='SQL Server',
            autocommit=True
        )

        cursor = sql.cursor()
        cursor.execute(f"""
            select *
            from config_relations
            where ClassName in ('pkcs11', 'pkcs11 application group')
        """)
        try:
            response = list(cursor)
        except:
            response = None
        sql.commit()
        sql.close()
        return response

    @staticmethod
    def snake_case(string: str):
        return re.sub(r'[^a-zA-Z0-9]\s*', '_', str(string)).lower()

    def get_root_classes(self) -> List[Node]:
        children = sorted(list(self.config_relations.query(
            f'Flags in ("SuperClass", "ContainedBy")'
        )['ClassName']))
        roots = sorted(set([c for c in list(self.config_relations['ClassName']) if c not in children]))
        return [Node(name=n) for n in roots]

    def option_to_variable(self, option: str, schema_version: str):
        if schema_version:
            try:
                version = Version(f'{schema_version[:2]}.{schema_version[2:4]}')
                if (15 <= version.major <= self.version.major) and (1 <= version.minor <= 4):
                    return f"""{self.snake_case(option)} = Attribute('{str(option).replace("'", '"')}', min_version='{version}')"""
            except:
                pass
        return f"""{self.snake_case(option)} = Attribute('{str(option).replace("'", '"')}')"""

    def create_tree(self, node: Node) -> Node:
        node.options = [
            Option(x) for x in sorted(self.config_relations.query(
                f'ClassName == "{node.name}" and Flags == "Optional"'
            )['Reference'])
        ]
        all_parent_classes = self.config_relations.query(
            f'Reference == "{node.name}" and Flags == "ContainedBy"'
        )['ClassName']
        for cls in sorted(set(all_parent_classes)):
            parent = Node(cls)
            parent.options = [
                Option(x) for x in sorted(self.config_relations.query(
                    f'ClassName == "{parent.name}" and Flags == "Optional"'
                )['Reference'])
            ]
            node.parents.append(parent)

        all_child_classes = self.config_relations.query(
            f'Reference == "{node.name}" and Flags == "SuperClass"'
        )['ClassName']
        for cls in sorted(set(all_child_classes)):
            child = Node(cls)
            node.children.append(child)
            self.create_tree(node=child)

        return node

    def dump_attributes(self, tree: Node):
        def dump(node: Node):
            imports = []
            if node.options:
                imports.append('from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute')
            else:
                imports.append('from pyvenafi.tpp.attributes._helper import IterableMeta')
            parents = [Node(x) for x in self.config_relations.query(
                f'ClassName == "{node.name}" and Flags == "SuperClass"'
            )['Reference'].values]
            parent_classes = []
            superclasses = []

            def get_superclass_hierarchy(x: Node):
                ps = list(self.config_relations.query(
                    f'ClassName == "{x.name}" and Flags == "SuperClass"'
                )['Reference'].values)
                results = ps
                for p in ps:
                    results += get_superclass_hierarchy(Node(p))
                return results

            for parent in parents:
                superclasses += get_superclass_hierarchy(parent)
            for parent in parents:
                if parent.name not in list(self.config_relations['ClassName'].values):
                    continue
                if parent.name in superclasses:
                    continue
                parent_class = f"""{re.sub(r'[^a-zA-Z0-9 ]', '', str(parent.name))}""".replace(' ', '') + 'Attributes'
                parent_classes.append(parent_class)
                imports.append(f'from pyvenafi.tpp.attributes.{self.snake_case(parent.name)} import {parent_class}')
            script = '\n'.join(imports) + '\n\n'
            file_name = self.snake_case(node.name)
            class_name = f"""{re.sub(r'[^a-zA-Z0-9 ]', '', str(node.name))}""".replace(' ', '') + 'Attributes'
            if parent_classes:
                class_def = f'class {class_name}({", ".join(parent_classes)}, metaclass=IterableMeta):'
            else:
                class_def = f'class {class_name}(metaclass=IterableMeta):'
            script += f'\n{class_def}\n'
            script += f'    __config_class__ = "{node.name}"\n'
            for option in node.options:
                script += f'    {self.option_to_variable(option.name, str(option.schema_version))}\n'
            for child in node.children:
                dump(child)
            for parent in node.parents:
                dump(parent)
            file_path = Path(f'pyvenafi/tpp/attributes/{file_name}.py')
            if not file_path.parent.exists():
                file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open('w') as f:
                print(script, end='', file=f)
            self.all_classes.append(node.name)
        dump(tree)

    def get_xml_files(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        build_prod_url = f'https://files.eng.venafi.com/builds-prod/TPP_{self.version}_Build_Prod_W2016'
        with urllib.request.urlopen(build_prod_url, context=ctx) as f:
            html = etree.HTML(f.read().decode())
        latest = sorted([
            e.text.strip('/') for e in
            html.xpath('//*[@class="even" or @class="odd"]/*[@class="indexcolname"]/a')
            if e.text.lower() != 'parent directory'
        ], reverse=True) + [None]

        latest_schema_url = ''
        for build in latest:
            try:
                latest_schema_url = f'{build_prod_url}/{build}/Schema'
                with urllib.request.urlopen(latest_schema_url, context=ctx) as f:
                    html = etree.HTML(f.read().decode())
                break
            except:
                if build is None:
                    raise Exception('There are currently no builds with XML schema definitions for this version.')
        xml_names = [
            e.text.strip('/') for e in
            html.xpath('//*[@class="even" or @class="odd"]/*[@class="indexcolname"]/a')
            if e.text.lower() != 'parent directory' and e.text.lower().endswith('.xml')
        ]

        pool = ThreadPoolExecutor(len(xml_names))

        def get_xml_file(xml_name):
            xml_url = f'{latest_schema_url}/{xml_name}'
            with urllib.request.urlopen(xml_url, context=ctx) as xf:
                try:
                    return xml_name, etree.XML(xf.read())
                except:
                    return None, None

        return filter(lambda x: x[0] is not None, list(pool.map(get_xml_file, xml_names)))

    @staticmethod
    def parse_xml(xml_items):
        xml_name, xml_root = xml_items[0], xml_items[1]  # type: str, etree._Element
        schema_root = '//ConfigSchema/SchemaVersion/*'
        config_schema = xml_root.xpath('//ConfigSchema')[0].attrib['Type']
        try:
            schema_version = int(xml_root.xpath('//ConfigSchema/SchemaVersion')[0].attrib['Version'])
        except:
            return

        def parse(start_node):
            schema = {}
            for child in start_node:
                for grandchild in child.getchildren():
                    grandchild_schema = parse(grandchild)
                    if grandchild_schema:
                        for k, v in grandchild_schema.items():
                            if not k:
                                del grandchild_schema[k]
                    schema.update(grandchild_schema)
                if child.tag in ('DefineClass', 'UpdateClass', 'AddAttribute'):
                    class_name = child.attrib['Name']
                    superclasses = [x.text for x in child.xpath('SuperClass')]
                    contained_by = [x.text for x in child.xpath('ContainedBy')]
                    options = [x.text for x in child.xpath('Optional')]
                    schema[class_name] = {
                        'SuperClasses': schema.get(class_name, {}).get('SuperClasses', []) + superclasses,
                        'ContainedBy' : schema.get(class_name, {}).get('ContainedBy', []) + contained_by,
                        'Options'     : schema.get(class_name, {}).get('Options', []) + options
                    }
            return schema

        return {
            'name'          : xml_name,
            'config_schema' : config_schema,
            'schema_version': schema_version,
            'schema'        : parse(start_node=xml_root.xpath(schema_root))
        }

    def apply_version_to_attrs(self, tree: Node):
        xml_files = self.get_xml_files()
        results = [self.parse_xml(xml_file) for xml_file in xml_files]
        parsed = sorted(list(filter(
            lambda x: x is not None, results)),
            key=lambda x: x['schema_version']
        )

        flattened_attrs = {}
        for schema in parsed:
            for class_name, values in schema['schema'].items():
                if class_name not in flattened_attrs.keys():
                    flattened_attrs[class_name] = {}
                for option in values['Options']:
                    if not option:
                        continue
                    flattened_attrs[class_name][option] = schema['schema_version']

        def apply_version(node: Node):
            for opt in node.options:
                opt.schema_version = flattened_attrs.get(node.name, {}).get(opt.name)
            for child in node.children:
                apply_version(child)

        apply_version(tree)

    def dump_classes(self):
        classes = '\n    '.join(f'{self.snake_case(c)} = "{c}"' for c in sorted(set(self.all_classes)))
        script = '\n'.join([
            'from pyvenafi.tpp.attributes._helper import IterableMeta\n\n',
            'class Classes(metaclass=IterableMeta):',
            f'    {classes}',
            ''
        ])
        file_path = Path(f'pyvenafi/tpp/features/definitions/classes.py')
        with file_path.open('w') as f:
            print(script, end='', file=f)

    def main(self):
        roots = self.get_root_classes()

        def doit(root):
            with PRINT_LOCK:
                print(f'Processing {root} tree...')
            tree = self.create_tree(root)
            self.apply_version_to_attrs(tree)
            self.dump_attributes(tree)

        with ThreadPoolExecutor(4) as pool:
            list(pool.map(doit, roots))
        self.dump_classes()


if __name__ == '__main__':
    parser = ArgumentParser('Update config schema in tpp.')
    parser.add_argument('-v', '--version', required=True, help='Version of TPP')
    parser.add_argument('-p', '--pkcs11', action='store_true', required=False, help='Update PKCS11')
    args = parser.parse_args()

    UpdateConfig(args.version, update_pkcs11=args.pkcs11).main()
