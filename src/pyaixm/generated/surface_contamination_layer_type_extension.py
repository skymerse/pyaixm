from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.surface_contamination_layer_extension import (
    SurfaceContaminationLayerExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceContaminationLayerTypeExtension:
    class Meta:
        global_type = False

    surface_contamination_layer_extension: Optional[
        SurfaceContaminationLayerExtension
    ] = field(
        default=None,
        metadata={
            "name": "SurfaceContaminationLayerExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
