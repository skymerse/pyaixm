from dataclasses import dataclass

from pyaixm.generated.information_service_extension_type import (
    InformationServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class InformationServiceExtension(InformationServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
