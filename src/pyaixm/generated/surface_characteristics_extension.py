from dataclasses import dataclass

from generated.surface_characteristics_extension_type import (
    SurfaceCharacteristicsExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceCharacteristicsExtension(SurfaceCharacteristicsExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
