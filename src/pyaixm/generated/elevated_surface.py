from dataclasses import dataclass

from pyaixm.generated.elevated_surface_type import ElevatedSurfaceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedSurface(ElevatedSurfaceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
