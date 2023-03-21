import os
import re
import shutil
from pathlib import Path
from runpy import run_path
from textwrap import dedent
from typing import List

from pyvenafi.tpp.api.api_base import ObjectModel

PROJECT_ROOT = Path(__file__).parent.parent
FEATURES_PATH = Path(PROJECT_ROOT, 'pyvenafi', 'tpp', 'features')
FEATURES_DOC_PATH = Path(PROJECT_ROOT, 'docs', 'rst', 'tpp', 'features')
MODELS_PATH = Path(PROJECT_ROOT, 'pyvenafi', 'tpp', 'api', 'websdk', 'models')
MODELS_DOC_PATH = Path(PROJECT_ROOT, 'docs', 'rst', 'tpp', 'models')
EXCLUDED_FEATURE_PATHS = [
    Path(FEATURES_PATH, 'bases').absolute(),
    Path(FEATURES_PATH, 'definitions').absolute(),
]


def make_title(title: str, underline: str = '='):
    return title, (underline * len(title))


def model_rst_template(module: type, model_name: str):
    title, h1 = make_title(model_name, '-')
    return dedent(f"""
    {title}
    {h1}

    .. _{module.__name__}.{title.replace(" ", "_").lower()}_model:
    .. autopydantic_model:: {module.__name__}.{model_name}
    """).lstrip()


def toc_rst_template(title: str, toc_items: List[str], tag: str = 'feature_list'):
    made_title, h1 = make_title(title.replace('_', ' ').title())
    toc_items_rst = '\n\t\t'.join(toc_items)
    return dedent(f"""
    .. _{title.lower()}_{tag}:

    {made_title}
    {h1}

    .. toctree::
        :maxdepth: 1

        {toc_items_rst}
    """.replace('\t', '    ')).lstrip()


def feature_class_rst_template(module_path: str, class_: str, parent:str = None):
    title: str = getattr(class_, '__feature__')
    if not title:
        raise AttributeError(f'{class_.__name__} does not have a __feature__ attribute.')
    made_title, h1 = make_title(title)

    if parent:
        feature = f'_{parent}_{title.replace(" ", "_").lower()}_feature'
    else:
        feature = f'_{title.replace(" ", "_").lower()}_feature'

    return dedent(f"""
    .. {feature}:

    {made_title}
    {h1}

    .. autoclass:: {module_path}.{class_.__name__}
       :members:
       :undoc-members:
       :show-inheritance:
       :inherited-members:
    """).lstrip()


def get_feature_docs():
    # Recreate the features doc folder.
    shutil.rmtree(path=str(FEATURES_DOC_PATH), ignore_errors=True)
    FEATURES_DOC_PATH.mkdir(exist_ok=True, parents=True)

    def walk_features(
        current_features_path: Path
    ):
        current_docs_path = Path(FEATURES_DOC_PATH, current_features_path.relative_to(FEATURES_PATH))  # doc-path corresponding to features-path
        write_rst_files = []  # files to be added to the current directory's TOC
        current_feature_toc_file = Path(current_docs_path, f'{current_features_path.stem}_toc.rst')  # current directory's TOC file

        # Get features and feature directories in current directory
        current_dir_items = [Path(current_features_path, str(f)) for f in os.listdir(current_features_path)]
        child_feature_dirs = [
            f for f in current_dir_items
            if f.is_dir()
               and not f.absolute() in EXCLUDED_FEATURE_PATHS
               and not f.name.startswith('_')
        ]

        child_features = [
            f for f in current_dir_items
            if f.is_file()
               and f.match('**/*.py')
               and not f.name.startswith('_')
               and not any(f.absolute().match(f'{e}/*') for e in EXCLUDED_FEATURE_PATHS)
        ]
        # Recursively walk through child directories and add them to current directory's TOC
        for feature_dir in child_feature_dirs:
            child_toc_rst = walk_features(feature_dir)
            if child_toc_rst:
                write_rst_files.append(child_toc_rst)

        # Create TOC for each feature
        for feature in child_features:
            classes = run_path(str(feature.absolute()))
            feature_classes = sorted(
                [c for c in classes.values() if hasattr(c, '__feature__')],
                key=lambda
                    x: x.__name__
            )

            # Get the module path for Sphinx's .. autoclass:: directive.
            rel_file_path = Path(classes['__file__']).relative_to(PROJECT_ROOT)
            module_path = Path(str(rel_file_path).replace('/', '.')).stem

            # Create doc directory for feature
            feature_file_path = Path(current_docs_path, feature.stem)
            feature_file_path.mkdir(exist_ok=True, parents=True)

            rel_feature_file_path = feature.relative_to(FEATURES_PATH)

            feature_parent = str(rel_feature_file_path.parent).replace('/', '_')
            feature_parent = feature_parent if feature_parent != '.' else None

            def process_class_rst(
                f_cls
            ):
                # Create the .. autoclass:: rst file.
                rst = feature_class_rst_template(module_path=module_path, class_=f_cls, parent=feature_parent)
                f_class_feature = f_cls.__feature__
                # if feature_parent:
                #     f_class_feature =  '_'.join([feature_parent, f_class_feature])
                rst_file_name = Path(re.sub(r"[^a-zA-Z\d]+", "_", f_class_feature).lower() + '.rst')
                rst_file_path = Path(feature_file_path, rst_file_name)
                with rst_file_path.open('w') as ff:
                    ff.write(rst)
                return rst_file_path  # <feature_class>

            # If there are multiple classes in the feature file, create a child TOC file for each class and add to TOC
            if len(feature_classes) > 1:
                # Stores all class rst files for each class in a feature file with @feature().
                feature_class_rst_files = []

                # Create the feature class rst files
                for feature_class in feature_classes:
                    a = process_class_rst(feature_class).stem
                    feature_class_rst_files.append(a)

                feature_title = feature.stem
                if feature_parent:
                    feature_title =  '_'.join([feature_parent, feature.stem])

                feature_toc_rst = toc_rst_template(title=feature_title, toc_items=feature_class_rst_files)
                feature_rst_file = Path(feature_file_path, f'{feature_title}_toc.rst')
                with feature_rst_file.open('w') as f:
                    f.write(feature_toc_rst)
                write_rst_files.append(feature_rst_file)

            # If there is only one class in the file, just add it current directory's TOC
            elif feature_classes:
                write_rst_files.append(process_class_rst(feature_classes[0]))

        # Write RST and child TOC links to TOC
        toc_name = current_features_path.stem
        root_features_rst = toc_rst_template(
            title=toc_name.capitalize(),
            toc_items=[f'{f.parent.name}/{f.stem}' for f in sorted(write_rst_files)]
        )
        root_features_rst_features_rst = f'.. _{toc_name}:\n\n{root_features_rst}'
        with current_feature_toc_file.open('w') as f:
            f.write(root_features_rst_features_rst)

        # Return TOC file, so it can be added to parent TOC
        return current_feature_toc_file

    # Recursively walk through features and build documentation
    walk_features(FEATURES_PATH)

def get_property_docs():
    from pyvenafi.tpp.api.websdk import models
    import inspect

    # Recreate the dataclasses doc folder.
    shutil.rmtree(path=str(MODELS_DOC_PATH), ignore_errors=True)
    MODELS_DOC_PATH.mkdir(exist_ok=True, parents=True)

    toc_items = []
    for item in vars(models).values():
        if not inspect.ismodule(item):
            continue
        mod_file = Path(item.__file__)
        title, h1 = make_title(mod_file.stem.replace('_', ' ').title())
        rst_path = Path(MODELS_DOC_PATH, f'{mod_file.stem}.rst')
        objects = run_path(str(mod_file))
        rst_content = [f'{title}\n{h1}\n']
        for name, obj in sorted(objects.items(), key=lambda x: x[0]):
            if isinstance(obj, type) and issubclass(obj, ObjectModel) and obj is not ObjectModel:
                rst_content.append(model_rst_template(item, obj.__name__))
        with rst_path.open('w') as dm:
            dm.write('\n'.join(rst_content))
        toc_items.append(rst_path.stem)
    models_toc_rst_content = toc_rst_template('Models', toc_items, tag='models')
    with Path(MODELS_DOC_PATH, 'models_toc.rst').open('w') as pd:
        pd.write(models_toc_rst_content)


def main():
    print('\n\n\n############RECOMPILING FEATURES AND PROPERTIES!!!############\n\n\n')
    get_feature_docs()
    get_property_docs()


if __name__ == '__main__':
    main()
