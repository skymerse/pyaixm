from dataclasses import dataclass

from pyaixm.generated.apron_marking_extension_type_2 import (
    ApronMarkingExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ApronMarkingExtension2(ApronMarkingExtensionType2):
    class Meta:
        name = "ApronMarkingExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
