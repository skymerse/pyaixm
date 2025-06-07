from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.holding_use import HoldingUse

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingUsePropertyType(AbstractAixmpropertyType):
    holding_use: Optional[HoldingUse] = field(
        default=None,
        metadata={
            "name": "HoldingUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
