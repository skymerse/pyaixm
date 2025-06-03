from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.authority_for_aerial_refuelling import (
    AuthorityForAerialRefuelling,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAerialRefuellingPropertyType(AbstractAixmpropertyType):
    authority_for_aerial_refuelling: Optional[AuthorityForAerialRefuelling] = (
        field(
            default=None,
            metadata={
                "name": "AuthorityForAerialRefuelling",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
