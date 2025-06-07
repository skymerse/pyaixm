from dataclasses import dataclass

from pyaixm.generated.fire_fighting_service_extension_type_2 import (
    FireFightingServiceExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FireFightingServiceExtension2(FireFightingServiceExtensionType2):
    class Meta:
        name = "FireFightingServiceExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
