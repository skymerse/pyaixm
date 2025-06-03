from dataclasses import dataclass

from generated.surface_contamination_layer_type import (
    SurfaceContaminationLayerType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceContaminationLayer(SurfaceContaminationLayerType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
