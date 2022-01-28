import warnings
import traceback
import sys


def warn_with_traceback(message, category, filename, lineno, file=None, line=None):
    log = file if hasattr(file, 'write') else sys.stderr
    print('---- Deprecation Warning ----')
    traceback.print_stack(file=log)
    print(f'{filename}:{lineno}: {message}', file=log)
    print('-----------------------------')

warnings.showwarning = warn_with_traceback

class DeprecationMeta(type):
    def __getattribute__(self, item):
        reason = super().__getattribute__('__deprecation_reason__')
        warnings.warn(reason)
        return super().__getattribute__(item)


