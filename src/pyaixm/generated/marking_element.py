from dataclasses import dataclass

from pyaixm.generated.marking_element_type import MarkingElementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingElement(MarkingElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
