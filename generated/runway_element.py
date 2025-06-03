from dataclasses import dataclass

from generated.runway_element_type import RunwayElementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayElement(RunwayElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
