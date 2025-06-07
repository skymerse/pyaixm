from dataclasses import dataclass

from generated.surface_type_2 import SurfaceType2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Surface2(SurfaceType2):
    class Meta:
        name = "Surface"
        namespace = "http://www.aixm.aero/schema/5.1"
