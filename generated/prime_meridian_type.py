from dataclasses import dataclass, field
from typing import Optional

from generated.greenwich_longitude import GreenwichLongitude
from generated.identified_object_type import IdentifiedObjectType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PrimeMeridianType(IdentifiedObjectType):
    greenwich_longitude: Optional[GreenwichLongitude] = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
