from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.light_element import LightElement

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightElementPropertyType(AbstractAixmpropertyType):
    light_element: Optional[LightElement] = field(
        default=None,
        metadata={
            "name": "LightElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
