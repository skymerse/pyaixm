from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.final_profile import FinalProfile

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalProfilePropertyType(AbstractAixmpropertyType):
    final_profile: Optional[FinalProfile] = field(
        default=None,
        metadata={
            "name": "FinalProfile",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
