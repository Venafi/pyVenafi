from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from functools import reduce
from typing import Dict, List, Literal, Set, Tuple, Union
import re
import autopep8


PROJECT_DIR = Path(__file__).parent
CLOUD_API_MODEL_PATH = Path(Path(__file__).parent, 'venafi', 'cloud', 'api', 'models')
if not CLOUD_API_MODEL_PATH.exists():
    raise FileNotFoundError(f'{CLOUD_API_MODEL_PATH} does not exist.')
CLOUD_API_ENDPOINTS_PATH = Path(Path(__file__).parent, 'venafi', 'cloud', 'api', 'endpoints')
if not CLOUD_API_ENDPOINTS_PATH.exists():
    raise FileNotFoundError(f'{CLOUD_API_ENDPOINTS_PATH} does not exist.')

CLOUD_API_MODEL_MODULE = 'venafi.cloud.api.models'

METHOD_TYPE = Literal['delete', 'get', 'patch', 'post', 'put']
INDENT = ' ' * 4
MAX_LINE_LENGTH = 145


@dataclass
class DataType:
    string: str
    imports: Dict[str, Set[str]] = field(default_factory=dict)

    @property
    def list_sub_type(self) -> str:
        return re.sub(r'^List\[|]$', '', self.string)


@dataclass
class Variable:
    name: str
    data_type: DataType
    root_field: bool = False


DATA_TYPE_FORMATS = {
    'uuid'     : DataType('UUID', {'uuid': {'UUID'}}),
    'boolean'  : DataType('bool'),
    'integer'  : DataType('int'),
    'string'   : DataType('str'),
    'date-time': DataType('datetime', {'datetime': {'datetime'}}),
    'float'    : DataType('float'),
    'decimal'  : DataType('float'),
    'array'    : DataType('List', {'typing': {'List'}}),
}


def get_data_type(d: Dict[str, ...], model_filename: str = None) -> DataType:
    if (ref := d.get('$ref')) is not None:
        if model_filename:
            return DataType(string=f"{model_filename}.{ref.rsplit('/', maxsplit=1)[-1]}")
        return DataType(string=ref.rsplit('/', maxsplit=1)[-1])
    if (any_of := d.get('anyOf')) is not None:
        dts = [get_data_type(dt) for dt in any_of]
        imports = defaultdict(set)
        for dt in dts:
            for package, items in dt.imports.items():
                for item in items:
                    imports[package].add(item)
        imports['typing'].add('Union')
        return DataType(
            string=f'''Union[{', '.join([dt.string for dt in dts])}]''',
            imports=imports
        )
    if (one_of := d.get('oneOf')) is not None:
        dts = [get_data_type(dt) for dt in one_of]
        imports = defaultdict(set)
        for dt in dts:
            for package, items in dt.imports.items():
                for item in items:
                    imports[package].add(item)
        imports['typing'].add('Union')
        return DataType(
            string=f'''Union[{', '.join([dt.string for dt in dts])}]''',
            imports=imports
        )
    if (all_of := d.get('allOf')) is not None:
        dts = [get_data_type(dt) for dt in all_of]
        imports = defaultdict(set)
        for dt in dts:
            for package, items in dt.imports.items():
                for item in items:
                    imports[package].add(item)
        imports['typing'].add('Union')
        return DataType(
            string=f'''Union[{', '.join([dt.string for dt in dts])}]''',
            imports=imports
        )
    if dt := d.get('format', d.get('type')):
        if dt == 'object':
            if (additional_properties := d.get('additionalProperties')) is not None:
                ap = get_data_type(additional_properties, model_filename=model_filename)
                return DataType(string=f'Dict[str, {ap.string}]', imports=dict(typing={'Dict'}))
            return DataType(string=f'Dict[str, Any]', imports=dict(typing={'Dict', 'Any'}))
        if dt == 'string' and d.get('enum'):
            return DataType(string=f'''Literal['{"', '".join(sorted(set(d["enum"])))}']''', imports=dict(typing={'Literal'}))
        if dt == 'array':
            imports = defaultdict(set)
            imports['typing'].add('List')
            sub_dt = get_data_type(d.get('items', {}), model_filename=model_filename)
            for package, items in sub_dt.imports.items():
                for item in items:
                    imports[package].add(item)
            return DataType(string=f'List[{sub_dt.string}]', imports=imports)
        return DATA_TYPE_FORMATS.get(d.get('format')) or DATA_TYPE_FORMATS.get(d.get('type'), DataType(string='Any', imports=dict(typing={'Any'})))
    raise ValueError(f'I do not know how to get the data type from this object: {d}')


@dataclass
class Method:
    method: METHOD_TYPE
    data: Dict
    model_filename: str

    def lines(self) -> Tuple[List[str], Dict[str, Set[str]], Dict[str, ...]]:
        data_types = defaultdict(set)

        output_cls, object_properties_from_paths, rc_mapping = self._output_cls()
        root_field = None
        if isinstance(output_cls, Variable) and output_cls.name == 'pass':
            output_cls_lines = [
                f'{INDENT}class Output(CloudApiOutputModel):',
                f'{INDENT * 2}pass',
            ]
        else:
            for i in output_cls:
                for package, items in i.data_type.imports.items():
                    for item in items:
                        data_types[package].add(item)
            output_cls_lines = [
                f'{INDENT}class Output(CloudApiOutputModel):',
            ]
            for i in output_cls:
                if i.data_type.string.startswith('List'):
                    _name = f'{i.name}List'
                elif i.data_type.string.startswith('Dict'):
                    _name = f'{i.name}Dict'
                else:
                    _name = i.name
                if i.root_field:
                    root_field = _name
                output_cls_lines.append(f'{INDENT*2}{_name}: {i.data_type.string}')

        if len(params := self._params()) > 0:
            arg = 'params' if self.method in ('get', 'delete') else 'data'
            if root_field:
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}=data), root_field='{root_field}')"
            elif rc_mapping:
                rc_mapping_str = ', '.join([f"{k}: '{v}'" for k, v in rc_mapping.items()])
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}=data), rc_mapping={{ {rc_mapping_str} }})"
            else:
                generate_output = f'return generate_output(output_cls=Output, response=self._{self.method}({arg}=data))'
            lines = [
                f'def {self.method}(self, ' + ', '.join([f'{p.name}: {p.data_type.string}' for p in params]) + '):',
                f'{INDENT}data = {{',
                *[f"{INDENT*2}'{p.name}': {p.name}," for p in params],
                f'{INDENT}}}',
                *output_cls_lines,
                f'{INDENT}{generate_output}'
            ]
            for p in params:
                for package, items in p.data_type.imports.items():
                    for item in items:
                        data_types[package].add(item)
        elif len(request_body := self._request_body()) > 0:
            arg = 'params' if self.method in ('get', 'delete') else 'data'
            if root_field:
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}=data), root_field='{root_field}')"
            elif rc_mapping:
                rc_mapping_str = ', '.join([f"{k}: '{v}'" for k, v in rc_mapping.items()])
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}=data), rc_mapping={{ {rc_mapping_str} }})"
            else:
                generate_output = f'return generate_output(output_cls=Output, response=self._{self.method}({arg}=data))'
            if len(request_body) > 1:
                raise Exception("I'm not sure how to handle this yet.")
            lines = [
                f'def {self.method}(self, ' + ', '.join([f'{i.name}: {i.data_type.string}' for i in request_body]) + '):',
                f'{INDENT}data = {{' + ','.join([f'**{i.name}.dict()' for i in request_body]) + '}',
                *output_cls_lines,
                f'{INDENT}{generate_output}'
            ]
            for i in request_body:
                for package, items in i.data_type.imports.items():
                    for item in items:
                        data_types[package].add(item)
        else:
            arg = 'params' if self.method in ('get', 'delete') else 'data'
            if root_field:
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}={{}}), root_field='{root_field}')"
            elif rc_mapping:
                rc_mapping_str = ', '.join([f"{k}: '{v}'" for k, v in rc_mapping.items()])
                generate_output = f"return generate_output(output_cls=Output, response=self._{self.method}({arg}={{}}), rc_mapping={{ {rc_mapping_str} }})"
            else:
                generate_output = f'return generate_output(output_cls=Output, response=self._{self.method}({arg}={{}}))'
            lines = [
                f'def {self.method}(self):',
                *output_cls_lines,
                f'{INDENT}{generate_output}'
            ]
        return lines, data_types, object_properties_from_paths

    def _params(self) -> List[Variable]:
        params = []
        for param in self.data.get('parameters', []):
            if param.get('in') == 'path':
                continue
            name = param['name']
            schema = param.get('schema', {})
            data_type = get_data_type(schema, model_filename=self.model_filename)
            params.append(Variable(name=name, data_type=data_type))
        return params

    def _request_body(self) -> List[Variable]:
        params = []
        content = self.data.get('requestBody', {}).get('content', {})
        for content_type, content_data in content.items():  # type: str, dict
            schema = content_data.get('schema', {})
            if schema.get('anyOf') or schema.get('oneOf') or schema.get('allOf') or schema.get('not'):
                raise Exception('I have never handled this before, so now what???')
            name = schema['$ref'].rsplit('/')[-1]
            dt = get_data_type(content_data.get('schema', {}), model_filename=self.model_filename)
            params.append(Variable(name=name, data_type=dt))
        return params

    def _output_cls(self) -> Tuple[Union[Variable, List[Variable]], Dict[str, ...], Dict[str, str]]:
        lines = []
        object_properties_from_paths = {}
        rc_mapping = {}
        for code, response in self.data['responses'].items():  # type: str, dict
            if code.startswith('2'):
                if 'content' not in response:
                    return Variable(name='pass', data_type=DataType(string='pass')), object_properties_from_paths, rc_mapping
                for content_type, content_data in response.get('content', {}).items():
                    if content_type == 'text/csv':
                        continue
                    schema = content_data['schema']
                    root_field = False
                    if schema.get('type') == 'object' and schema.get('properties'):
                        for name, info in schema['properties'].items():
                            if info.get('format', info.get('type')) == 'object' and info.get('properties'):
                                dt = DataType(string=f'{self.model_filename}.{name}')
                                object_properties_from_paths[name] = info
                            else:
                                dt = get_data_type(info)
                            lines.append(Variable(name=name, data_type=dt))
                    else:
                        dt = get_data_type(schema, model_filename=self.model_filename)
                        if dt.string.startswith('List') or dt.string.startswith('Dict'):
                            root_field = True
                        if '$ref' in schema:
                            name = dt.string.split('.')[-1]
                        elif dt.list_sub_type:
                            name = dt.list_sub_type.split('.')[-1]
                        else:
                            raise Exception("I do not know what to call this variable.")
                        lines.append(Variable(name=name, data_type=dt, root_field=root_field))
                        rc_mapping[code] = name
        unique_lines = []
        [unique_lines.append(line) for line in lines if line.name not in [u.name for u in unique_lines]]
        if len(unique_lines) == 0:
            return Variable(name='pass', data_type=DataType(string='pass')), object_properties_from_paths, rc_mapping
        return unique_lines, object_properties_from_paths, rc_mapping


@dataclass
class Node:
    path: str
    model_filename: str
    methods: Dict[METHOD_TYPE, dict] = field(default_factory=dict)
    parents: List[Node] = field(default_factory=list)
    children: List[Node] = field(default_factory=list)

    @property
    def endpoint(self) -> str:
        return self.path.rsplit('/', maxsplit=1)[-1]

    @property
    def is_dynamic_path(self) -> bool:
        return bool(re.match(r'^{\w+}$', self.endpoint))

    @property
    def _is_first_ancestor(self) -> bool:
        return len(self.parents) == 1 and isinstance(self.parents[0], RootNode)

    @property
    def _class_name(self):
        return self.endpoint if not self.is_dynamic_path else re.sub(r'[{}]', '', self.endpoint).upper()

    def lines(self, depth: int = 0) -> Tuple[List[str], Dict[str, Set[str]], Dict[str, ...]]:
        indent = lambda x: (INDENT * depth) + (INDENT * x)
        sanitize = lambda x: [f'{i}{y}' for i, y in x if y.rstrip()]

        # region CLASS STATEMENT
        class_statement = sanitize([(indent(0), self._class_statement())])
        # endregion CLASS STATEMENT

        # region INIT METHOD
        init_method = sanitize([
            (indent(1), self._init_statement()),
            (indent(2), self._get_super_call()),
            *[(indent(2), ivar) for ivar in self._get_inst_vars()]
        ])
        # endregion INIT METHOD

        # region DYNAMIC FUNCTIONS
        dynamic_functions = sanitize([(indent(1), line) for line in self._get_dynamic_functions()])
        # endregion DYNAMIC FUNCTIONS

        # region REST METHODS
        rest_methods, data_types, object_properties_from_paths = self._get_methods()
        rest_methods = sanitize([(indent(1), line) for line in rest_methods])
        # endregion REST METHODS

        lines = [
            *class_statement,
            *init_method,
            *dynamic_functions,
            *rest_methods,
        ]

        for child in self.children:
            lns, dts, opfp = child.lines(depth=depth + 1)
            lines += lns
            object_properties_from_paths.update(opfp)
            for package, items in dts.items():
                for item in items:
                    data_types[package].add(item)
        return [x for x in lines if x.rstrip()], data_types, object_properties_from_paths

    # region Class Statement
    def _class_statement(self) -> str:
        return f'class _{self._class_name}(CloudApiEndpoint):'
    # endregion Class Statement

    # region __init__ Method
    def _init_statement(self) -> str:
        if self._is_first_ancestor:
            return f'def __init__(self, api_obj):'
        elif self.children:
            return f'def __init__(self, *args, **kwargs):'
        return ''

    def _get_super_call(self) -> str:
        if self._is_first_ancestor:
            return f"super().__init__(api_obj=api_obj, url='{self.path}')"
        elif self.children:
            return f"super().__init__(*args, **kwargs)"
        return ''

    def _get_inst_vars(self) -> List[str]:
        return [
            f"self.{child._class_name} = self._{child._class_name}(api_obj=self._api_obj, url=f'{{self._url}}/{child.endpoint}')"
            for child in self.children if not child.is_dynamic_path
        ]
    # endregion __init__ Method

    # region Dynamic Functions
    def _get_dynamic_functions(self) -> List[str]:
        lines = []
        for child in self.children:
            if child.is_dynamic_path:
                lines += [
                    f'def {child._class_name}(self, {child._class_name.lower()}: str):',
                    f"{INDENT}return self._{child._class_name}(api_obj=self._api_obj, url=f'{{self._url}}/{{{child._class_name.lower()}}}')"
                ]
        return lines
    # endregion Dynamic Functions

    # region REST Methods
    def _get_methods(self) -> Tuple[List[str], Dict[str, Set[str]], Dict[str, ...]]:
        lines = []
        data_types = defaultdict(set)
        object_properties_from_paths = {}
        for name, data in self.methods.items():
            lns, dts, opfp = Method(name, data, self.model_filename).lines()
            lines += lns
            object_properties_from_paths.update(opfp)
            for package, items in dts.items():
                for item in items:
                    data_types[package].add(item)
        return lines, data_types, object_properties_from_paths
    # endregion REST Methods


@dataclass
class RootNode:
    model_filename: str
    children: List[Node] = field(default_factory=list)

    @property
    def parents(self):
        return []

    @classmethod
    def load(cls, data: dict, model_filename: str):
        sorted_data = dict(sorted(data.items(), key=lambda x: str(x[0]).count('/')))  # noqa

        tree = cls(model_filename=model_filename)

        def add_parts(parts, method_items=None):
            parts_to_process = [p for p in parts if p not in ('', 'v1')]
            getter = lambda x, y: next(i for i in x.children if i.endpoint == y)
            new_node = Node(path='/'.join(parts), methods=method_items or {}, model_filename=model_filename)
            try:
                node: Node = reduce(getter, parts_to_process[:-1], tree)  # noqa
            except StopIteration:
                add_parts(parts_to_process[:-1])
                node: Node = reduce(getter, parts_to_process[:-1], tree)  # noqa
            new_node.parents = node.parents + [node]
            node.children.append(new_node)

        for path, methods in sorted_data.items():  # type: str, dict
            add_parts(path.split('/'), methods)
        return tree

    def lines(self) -> Tuple[List[str], Dict[str, ...]]:
        lines = []
        object_properties_from_paths = {}
        imports = [
            'from __future__ import annotations',
            'from venafi.cloud.api.api_base import CloudApiEndpoint, CloudApiOutputModel, generate_output',
            f'from {CLOUD_API_MODEL_MODULE} import {self.model_filename}'
        ]
        data_types = defaultdict(set)
        for child in sorted(self.children, key=lambda x: x.path):
            lns, dts, opfp = child.lines()
            lines += lns
            object_properties_from_paths.update(opfp)
            for package, items in dts.items():
                for item in items:
                    data_types[package].add(item)

        for package, items in data_types.items():
            if len(items) > 1:
                imports.append(f'''from {package} import ({', '.join(sorted(items))})''')
            else:
                imports.append(f'''from {package} import {', '.join(items)}''')
        return imports + lines, object_properties_from_paths


@dataclass
class PathParser:
    data: Dict[str, dict]
    model_filename: str
    _tree: RootNode = field(default=None, init=False)

    def __post_init__(self):
        self._tree = RootNode.load(data=self.data, model_filename=self.model_filename)

    def get_code(self):
        lines, object_properties_from_paths = self._tree.lines()
        code = autopep8.fix_code('\n'.join(lines), options={'max_line_length': MAX_LINE_LENGTH})
        # print(code)
        return code, object_properties_from_paths


@dataclass
class ComponentSchemaParser:
    schemas: dict
    object_properties_from_paths: Dict[str, ...] = field(default_factory=dict)
    refs: List[str] = field(default_factory=list, init=False)
    _imports: Dict[str, Set[str]] = field(init=False, default_factory=lambda: defaultdict(set))

    def get_code(self):
        lines = self._lines()
        code = autopep8.fix_code('\n'.join(lines), options={'max_line_length': MAX_LINE_LENGTH})
        # print(code)
        return code

    def _lines(self):
        lines = []
        for name, info in sorted(self.schemas.items(), key=lambda x: x[0]):
            if info['type'] != 'object':
                raise Exception(f'Got an unexpected type: {info["type"]}')
            lines += self._get_model(name, info.get('properties', {}))

        if self.object_properties_from_paths:
            def doit(name_, props_):
                lines_ = self._get_model(name_, props_)
                for k_, v_ in props_.items():
                    if v_.get('format', v_.get('type')) == 'object' and v_.get('properties'):
                        lines_ += doit(k_, v_.get('properties', {}))
                return lines_

            for k, v in sorted(self.object_properties_from_paths.items(), key=lambda x: x[0]):
                lines += doit(k, v.get('properties', {}))

        imports = self._get_imports()
        update_refs = [
            f'{ref}.update_forward_refs()' for ref in self.refs
        ]
        return imports + lines + update_refs

    def _get_imports(self):
        lines = [
            'from __future__ import annotations',
            'from venafi.cloud.api.api_base import ApiField, ObjectModel'
        ]
        for package, items in self._imports.items():
            if len(items) > 1:
                lines.append(f'''from {package} import ({f', '.join(sorted(items))})''')
            else:
                lines.append(f'''from {package} import {f', '.join(items)}''')
        return lines

    def _get_model(self, name: str, properties: Dict[str, Dict[str, str]]) -> List[str]:
        lines = []

        for prop, info in properties.items():
            if info.get('format', info.get('type')) == 'object' and info.get('properties'):
                data_type = DataType(string=prop)
            else:
                data_type = get_data_type(info)
            if data_type.string.startswith('List'):
                lines.append(f'''{INDENT}{prop}: {data_type.string} = ApiField(alias='{prop}', default_factory=list)''')
            elif data_type.string.startswith('Dict'):
                lines.append(f'''{INDENT}{prop}: {data_type.string} = ApiField(alias='{prop}', default_factory=dict)''')
            else:
                lines.append(f'''{INDENT}{prop}: {data_type.string} = ApiField(alias='{prop}')''')
            for package, items in data_type.imports.items():
                for item in items:
                    self._imports[package].add(item)
        if len(lines) == 0:
            lines = [f'{INDENT}pass']
        self.refs.append(name)
        return [
            f'class {name}(ObjectModel):'
        ] + lines


def main():
    import requests
    from pathlib import Path

    base_url = 'https://api.staging.qa.venafi.io'
    services = requests.get(f'{base_url}/v3/api-docs/swagger-config').json()  # type: dict
    for item in sorted(services.get('urls', []), key=lambda x: x['name']):
        name = str(item['name']).replace('-', '_')
        print(f'Processing {name}...')
        url = f'{base_url}/{item["url"].lstrip("/")}'
        data = requests.get(url).json()
        object_properties_from_paths = {}
        if (paths := data.get('paths')) is not None:
            pp = PathParser(data=paths, model_filename=name)
            code, object_properties_from_paths = pp.get_code()
            file = Path(CLOUD_API_ENDPOINTS_PATH, f'{name}.py')
            with file.open('w') as f:
                f.write(code)
        if (schemas := data.get('components', {}).get('schemas')) is not None:
            csp = ComponentSchemaParser(schemas=schemas, object_properties_from_paths=object_properties_from_paths)
            code = csp.get_code()
            file = Path(CLOUD_API_MODEL_PATH, f'{name}.py')
            with file.open('w') as f:
                f.write(code)


if __name__ == '__main__':
    main()
