from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.city import City

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CityPropertyType(AbstractAixmpropertyType):
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
