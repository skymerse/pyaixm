from dataclasses import dataclass

from generated.information_service_type import InformationServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationService(InformationServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
