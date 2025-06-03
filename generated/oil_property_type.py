from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.oil import Oil

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OilPropertyType(AbstractAixmpropertyType):
    oil: Optional[Oil] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
