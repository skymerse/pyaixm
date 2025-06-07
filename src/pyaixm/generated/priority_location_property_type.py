from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.location_property_type import LocationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
