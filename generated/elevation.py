from dataclasses import dataclass

from generated.elevation_type import ElevationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Elevation(ElevationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
