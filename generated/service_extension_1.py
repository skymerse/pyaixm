from dataclasses import dataclass

from generated.service_extension_type_1 import ServiceExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ServiceExtension1(ServiceExtensionType1):
    class Meta:
        name = "ServiceExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
