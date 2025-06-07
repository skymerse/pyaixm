from dataclasses import dataclass

from generated.arresting_gear_type import ArrestingGearType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrestingGear(ArrestingGearType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
