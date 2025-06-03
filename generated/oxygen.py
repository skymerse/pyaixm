from dataclasses import dataclass

from generated.oxygen_type import OxygenType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Oxygen(OxygenType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
