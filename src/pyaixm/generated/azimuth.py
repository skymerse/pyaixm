from dataclasses import dataclass

from pyaixm.generated.azimuth_type import AzimuthType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Azimuth(AzimuthType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
