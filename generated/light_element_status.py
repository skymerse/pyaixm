from dataclasses import dataclass

from generated.light_element_status_type import LightElementStatusType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightElementStatus(LightElementStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
