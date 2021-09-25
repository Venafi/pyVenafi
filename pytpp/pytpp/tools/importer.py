from importlib import import_module

class Importer:
    def __init__(self, name: str, imports: dict):
        self.name = name
        self.imports = imports

    def getattr(self, name):
        try:
            module, attr = self.imports[name]
        except KeyError as err:
            offender = err.__traceback__.tb_frame.f_back.f_back.f_code.co_filename
            raise ImportError(f"cannot import name '{name}' from '{self.name}' ({offender})") from None
        return getattr(__import__(module, globals(), locals(), ['']), attr)
