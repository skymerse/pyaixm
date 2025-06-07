from dataclasses import dataclass

from pyaixm.generated.runway_direction_extension_type_2 import (
    RunwayDirectionExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayDirectionExtension2(RunwayDirectionExtensionType2):
    class Meta:
        name = "RunwayDirectionExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
