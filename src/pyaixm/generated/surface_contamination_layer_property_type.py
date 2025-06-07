from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.surface_contamination_layer import SurfaceContaminationLayer

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceContaminationLayerPropertyType(AbstractAixmpropertyType):
    surface_contamination_layer: Optional[SurfaceContaminationLayer] = field(
        default=None,
        metadata={
            "name": "SurfaceContaminationLayer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
