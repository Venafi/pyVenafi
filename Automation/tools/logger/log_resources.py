from config.settings import LOG_API_COLOR, LOG_CRITICAL_COLOR, LOG_FEATURE_COLOR, LOG_TEST_COLOR


class LogLevels:
    api = 0
    feature = 1
    test = 2
    critical = 9


def log_color(s, fg, bg): return "\033[{s};{fg};{bg}m ".format(s=s, fg=fg, bg=bg)


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


class LogColors:
    level_color = {
        LogLevels.api: log_color(*LOG_API_COLOR),
        LogLevels.feature: log_color(*LOG_FEATURE_COLOR),
        LogLevels.test: log_color(*LOG_TEST_COLOR),
        LogLevels.critical: log_color(*LOG_CRITICAL_COLOR)
    }

    end = log_color(TextStyle.no_style, 0, 0)
