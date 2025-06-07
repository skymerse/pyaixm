from dataclasses import dataclass, field
from typing import Optional

from generated.identified_object_type import IdentifiedObjectType
from generated.minimum_occurs import MinimumOccurs

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralOperationParameterType(IdentifiedObjectType):
    minimum_occurs: Optional[MinimumOccurs] = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
