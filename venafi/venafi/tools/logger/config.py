from abc import abstractmethod
from typing import List


class LogTag:
    def __init__(self, name: str, value: int, html_color: str = None):
        self.name = name
        self.alias = ''.join([c.lower() for c in name if c.isalpha()])
        self.value = value
        self.html_color = html_color

    def to_dict(self):
        return {
            'name'      : self.name,
            'value'     : self.value,
            'html_color': self.html_color
        }


class LogTagTemplate:
    @property
    @abstractmethod
    def default(self) -> LogTag:
        raise NotImplementedError('Default log level definition required!')

    @property
    @abstractmethod
    def critical(self) -> LogTag:
        raise NotImplementedError('Critical log level definition required!')

    @classmethod
    def to_dict(cls):
        items = {}
        for var in dir(cls):
            if not var.startswith('_') and not callable(var):  # type: LogTag
                if hasattr(value := getattr(cls, var), 'to_dict'):
                    items[var] = value.to_dict()
        return items

    @classmethod
    def get_all(cls) -> List[LogTag]:
        return [ll for item in dir(cls) if isinstance(ll := getattr(cls, item), LogTag)]


class LogTags(LogTagTemplate):
    default = LogTag(
        name='Default',
        value=0,
        html_color='limegreen'
    )

    critical = LogTag(
        name='Critical',
        value=90,
        html_color='red'
    )
