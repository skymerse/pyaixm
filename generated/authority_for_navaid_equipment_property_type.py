from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.authority_for_navaid_equipment import (
    AuthorityForNavaidEquipment,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForNavaidEquipmentPropertyType(AbstractAixmpropertyType):
    authority_for_navaid_equipment: Optional[AuthorityForNavaidEquipment] = (
        field(
            default=None,
            metadata={
                "name": "AuthorityForNavaidEquipment",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
