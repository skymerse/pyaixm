from dataclasses import dataclass

from pyaixm.generated.abstract_service_type import AbstractServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractService(AbstractServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
