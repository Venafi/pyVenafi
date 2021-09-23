import warnings


class DeprecationMeta(type):
    def __getattribute__(self, item: str):
        reason = super().__getattribute__('__deprecation_reason__')
        warnings.warn(reason)
        return super().__getattribute__(item)
