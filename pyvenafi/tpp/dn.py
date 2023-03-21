class DN(str):
    def __init__(self, dn: str):
        super().__init__()
        self.dn = str(dn)
        if '\\' in self.dn:
            self._parent, self.name = self.dn.rsplit('\\', maxsplit=1)
        else:
            self._parent, self.name = None, self.dn
        self.depth = self.dn.count('\\') - 1

    def __new__(cls, dn: str):
        return str.__new__(cls, dn)

    def __add__(self, other):
        return DN(self.dn + other)

    @property
    def parent(self):
        return DN(self._parent) if self._parent else None
