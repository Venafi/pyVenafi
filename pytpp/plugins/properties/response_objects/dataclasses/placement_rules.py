from dataclasses import dataclass


@dataclass
class Condition:
    field: str
    comparison: str
    value: str
