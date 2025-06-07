from dataclasses import dataclass

from pyaixm.generated.surface_characteristics_type import (
    SurfaceCharacteristicsType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceCharacteristics(SurfaceCharacteristicsType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
