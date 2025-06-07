from dataclasses import dataclass

from pyaixm.generated.abstract_traffic_separation_service_type import (
    AbstractTrafficSeparationServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractTrafficSeparationService(AbstractTrafficSeparationServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
