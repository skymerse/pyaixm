from dataclasses import dataclass

from pyaixm.generated.surface_contamination_layer_extension_type import (
    SurfaceContaminationLayerExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceContaminationLayerExtension(
    SurfaceContaminationLayerExtensionType
):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
