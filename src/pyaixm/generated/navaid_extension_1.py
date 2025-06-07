from dataclasses import dataclass

from pyaixm.generated.navaid_extension_type_1 import NavaidExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NavaidExtension1(NavaidExtensionType1):
    class Meta:
        name = "NavaidExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
