from typing import Union, Dict


class ForegroundColors:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37


class BackgroundColors:
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    purple = 45
    cyan = 46
    white = 47
    transparent = 48


class TextStyle:
    no_style = 0
    bold = 1
    italics = 3
    underline = 4
    cross_through = 9


def console_log_color(s=None, fg=None, bg=None):
    log_color = f"\033["
    log_color += ';'.join([str(x) for x in (s,fg,bg) if x])
    return f"{log_color}m "


class LogLevel:
    def __init__(self, name: str, level: int, console_color: tuple = None, html_color: str = None):
        self.name = name
        self.level = level

        class Colors:
            console = console_log_color(*console_color)
            html = html_color

        self.colors = Colors()

    def __repr__(self):
        return str(self.level)

    def as_dictionary(self):
        log_level = {}
        for key, value in vars(self).items():  # type: str, LogLevel
            # type value:  LogLevel
            if not key.startswith('_'):
                log_level.update({key: value})
        return log_level


class LogLevels:
    low = LogLevel(
        name='API',
        level=10,
        console_color=(TextStyle.italics, ForegroundColors.yellow, BackgroundColors.transparent),
        html_color='palegoldenrod'
    )
    medium = LogLevel(
        name='Feature',
        level=20,
        console_color=(TextStyle.italics, ForegroundColors.cyan, BackgroundColors.transparent),
        html_color='lightcyan'
    )
    high = LogLevel(
        name='Main',
        level=30,
        console_color=(TextStyle.bold, ForegroundColors.purple, BackgroundColors.transparent),
        html_color='hotpink'
    )
    critical = LogLevel(
        name='Critical',
        level=90,
        console_color=(TextStyle.underline, ForegroundColors.red, BackgroundColors.transparent),
        html_color='red'
    )

    @classmethod
    def as_dictionary(cls) -> Dict[int, LogLevel]:
        log_levels = {}
        for var in dir(cls):  # type: str
            if not var.startswith('_') and hasattr(getattr(cls, var), 'as_dictionary'):
                value = getattr(cls, var)  # type:  LogLevel
                log_levels.update({value.level: value})
        return log_levels
