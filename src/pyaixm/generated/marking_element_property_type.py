from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.marking_element import MarkingElement

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingElementPropertyType(AbstractAixmpropertyType):
    marking_element: Optional[MarkingElement] = field(
        default=None,
        metadata={
            "name": "MarkingElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
