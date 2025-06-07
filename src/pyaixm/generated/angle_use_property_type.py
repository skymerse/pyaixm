from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.angle_use import AngleUse

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleUsePropertyType(AbstractAixmpropertyType):
    angle_use: Optional[AngleUse] = field(
        default=None,
        metadata={
            "name": "AngleUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
