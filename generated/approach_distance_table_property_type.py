from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.approach_distance_table import ApproachDistanceTable

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachDistanceTablePropertyType(AbstractAixmpropertyType):
    approach_distance_table: Optional[ApproachDistanceTable] = field(
        default=None,
        metadata={
            "name": "ApproachDistanceTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
