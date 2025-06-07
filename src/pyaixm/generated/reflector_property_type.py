from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.reflector import Reflector

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ReflectorPropertyType(AbstractAixmpropertyType):
    reflector: Optional[Reflector] = field(
        default=None,
        metadata={
            "name": "Reflector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
