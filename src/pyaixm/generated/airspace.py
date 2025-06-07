from dataclasses import dataclass

from pyaixm.generated.airspace_type import AirspaceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Airspace(AirspaceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
