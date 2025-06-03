from dataclasses import dataclass, field
from typing import Optional

from generated.identified_object_type import IdentifiedObjectType
from generated.second_defining_parameter_1 import SecondDefiningParameter1
from generated.semi_major_axis import SemiMajorAxis

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidType(IdentifiedObjectType):
    semi_major_axis: Optional[SemiMajorAxis] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    second_defining_parameter: Optional[SecondDefiningParameter1] = field(
        default=None,
        metadata={
            "wrapper": "secondDefiningParameter",
            "name": "SecondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
