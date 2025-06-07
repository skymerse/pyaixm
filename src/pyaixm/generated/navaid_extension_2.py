from dataclasses import dataclass

from pyaixm.generated.navaid_extension_type_2 import NavaidExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NavaidExtension2(NavaidExtensionType2):
    class Meta:
        name = "NavaidExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
