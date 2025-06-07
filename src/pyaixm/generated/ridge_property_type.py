from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.ridge import Ridge

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RidgePropertyType(AbstractAixmpropertyType):
    ridge: Optional[Ridge] = field(
        default=None,
        metadata={
            "name": "Ridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
