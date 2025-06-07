from dataclasses import dataclass

from generated.runway_marking_extension_type_2 import (
    RunwayMarkingExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayMarkingExtension2(RunwayMarkingExtensionType2):
    class Meta:
        name = "RunwayMarkingExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
