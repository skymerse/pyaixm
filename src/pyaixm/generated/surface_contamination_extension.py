from dataclasses import dataclass

from pyaixm.generated.surface_contamination_extension_type import (
    SurfaceContaminationExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceContaminationExtension(SurfaceContaminationExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
