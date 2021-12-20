import re
from textwrap import dedent
from pathlib import Path
from runpy import run_path
from typing import List
import shutil


PYTPP_PATH = Path(__file__).parent.parent
FEATURES_PATH = Path(PYTPP_PATH, 'pytpp', 'features')
FEATURES_DOC_PATH = Path(PYTPP_PATH, 'docs', 'rst', 'features')
shutil.rmtree(path=str(FEATURES_DOC_PATH), ignore_errors=True)
FEATURES_DOC_PATH.mkdir(exist_ok=True, parents=True)


def feature_toc_rst_template(title: str, toc_items: List[str]):
    title = title.replace('_', ' ').title()
    h1 = '=' * len(title)
    toc_items_rst = '\n\t\t'.join(toc_items)
    return dedent(f"""
    .. _{title.replace(" ", "_").lower()}_feature_list:
    
    {title}
    {h1}

    .. toctree::
        :maxdepth: 1

        {toc_items_rst}
    """.replace('\t', '    ')).lstrip()

def feature_class_rst_template(module_path: str, class_: str):
    title: str = getattr(class_, '__feature__')
    if not title:
        raise AttributeError(f'{class_.__name__} does not have a __feature__ attribute.')
    h1 = '=' * len(title)
    return dedent(f"""
    .. _{title.replace(" ", "_").lower()}_feature:
    
    {title}
    {h1}
    
    .. autoclass:: {module_path}.{class_.__name__}
       :members:
       :undoc-members:
       :show-inheritance:
       :inherited-members:
    """).lstrip()

def main():
    features_rst_files = [] # rst/feature/<feature> files to be added to the main features TOC.
    for feature in FEATURES_PATH.glob('*.py'):
        if not feature.is_file() or feature.name.startswith('_'):
            continue

        # Collection feature classes
        classes = run_path(str(feature.absolute()))
        feature_classes = sorted([c for c in classes.values() if hasattr(c, '__feature__')],
                                 key=lambda x: x.__name__)

        # Get the module path for Sphinx's .. autoclass:: directive.
        rel_file_path = Path(classes['__file__']).relative_to(PYTPP_PATH)
        module_path = Path(str(rel_file_path).replace('/', '.')).stem

        # Create the rst/features/<feature> folder.
        feature_file_path = Path(FEATURES_DOC_PATH, feature.stem)
        feature_file_path.mkdir(exist_ok=True, parents=True)


        def process_class_rst(cls):
            # Create the .. autoclass:: rst file.
            rst = feature_class_rst_template(module_path=module_path, class_=cls)
            rst_file_name = Path(re.sub("[^a-zA-Z\d]+", "_", cls.__feature__).lower() + '.rst')
            rst_file_path = Path(feature_file_path, rst_file_name) # rst/features/<feature>/<feature_class>.rst
            with rst_file_path.open('w') as f:
                f.write(rst)
            return rst_file_path  # <feature_class>

        if len(feature_classes) > 1:
            # Stores all class rst files for each class in a feature file with @feature().
            feature_class_rst_files = []

            # Create the feature class rst files.
            for feature_class in feature_classes:
                feature_class_rst_files.append(process_class_rst(feature_class).stem)

            # Create the rst/features/<feature>/<feature>.rst file.
            feature_toc_rst = feature_toc_rst_template(title=feature.stem, toc_items=feature_class_rst_files)
            feature_rst_file = Path(feature_file_path, f'{feature.stem}_toc.rst')
            with feature_rst_file.open('w') as f:
                f.write(feature_toc_rst)
            features_rst_files.append(feature_rst_file)
        else:
            features_rst_files.append(process_class_rst(feature_classes[0]))
    pytpp_features_rst = feature_toc_rst_template(
        title='Features',
        toc_items=[f'{f.parent.name}/{f.stem}' for f in sorted(features_rst_files)]
    )
    pytpp_features_rst = f'.. _features:\n\n{pytpp_features_rst}'
    with Path(FEATURES_DOC_PATH, 'features_toc.rst').open('w') as f:
        f.write(pytpp_features_rst)

if __name__ == '__main__':
    main()

