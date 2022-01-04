from dataclasses import dataclass


@dataclass
class PlacementRules:
    field: str
    comparison: str
    value: str
