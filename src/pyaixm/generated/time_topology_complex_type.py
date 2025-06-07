from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_time_complex_type import AbstractTimeComplexType
from pyaixm.generated.time_topology_primitive_property_type import (
    TimeTopologyPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeTopologyComplexType(AbstractTimeComplexType):
    primitive: Iterable[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
