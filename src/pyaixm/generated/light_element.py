from dataclasses import dataclass

from generated.light_element_type import LightElementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightElement(LightElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
