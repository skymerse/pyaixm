from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.light_element_status import LightElementStatus

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightElementStatusPropertyType(AbstractAixmpropertyType):
    light_element_status: Optional[LightElementStatus] = field(
        default=None,
        metadata={
            "name": "LightElementStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
