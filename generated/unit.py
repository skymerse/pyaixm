from dataclasses import dataclass

from generated.unit_type import UnitType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Unit(UnitType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
