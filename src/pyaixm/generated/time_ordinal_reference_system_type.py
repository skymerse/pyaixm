from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.time_ordinal_era_type import TimeOrdinalEraPropertyType
from pyaixm.generated.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeOrdinalReferenceSystemType(TimeReferenceSystemType):
    component: Iterable[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
