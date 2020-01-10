from datetime import datetime, timezone, timedelta
from dateutil.parser import parse


def to_date_string():
    pass


def from_date_string(date_string: str, is_str_format: bool = False) -> datetime:
    if 'Date' in date_string:
        date_as_num = ''.join([c for c in date_string if c.isnumeric() or c == '+'])
        if '+' in date_as_num:
            dt, tz = date_as_num.split('+')
            tz = timezone(timedelta(hours=int(tz)/100))
        else:
            dt, tz = date_as_num, None
        date_as_float = float(int(dt) / 1000)
        return datetime.fromtimestamp(date_as_float, tz=tz)

    elif date_string.startswith('PT'):
        tm = date_string.lstrip('PT')
        hour, tm = tm.split('H')
        minute, tm = tm.split('M')
        secs, milsecs = tm.split('.')
        tm = timedelta(hours=int(hour), minutes=int(minute), seconds=int(secs), milliseconds=int(milsecs.rstrip('S')))
        return datetime.now() - tm

    else:
        return parse(date_string)


date = from_date_string('PT3H28M57.680125S')
print(date)
