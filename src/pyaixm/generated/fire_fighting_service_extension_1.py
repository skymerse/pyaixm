from dataclasses import dataclass

from pyaixm.generated.fire_fighting_service_extension_type_1 import (
    FireFightingServiceExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class FireFightingServiceExtension1(FireFightingServiceExtensionType1):
    class Meta:
        name = "FireFightingServiceExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
