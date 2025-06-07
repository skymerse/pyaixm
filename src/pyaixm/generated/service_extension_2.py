from dataclasses import dataclass

from pyaixm.generated.service_extension_type_2 import ServiceExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ServiceExtension2(ServiceExtensionType2):
    class Meta:
        name = "ServiceExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
