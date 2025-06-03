from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.approach_timing_table import ApproachTimingTable

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachTimingTablePropertyType(AbstractAixmpropertyType):
    approach_timing_table: Optional[ApproachTimingTable] = field(
        default=None,
        metadata={
            "name": "ApproachTimingTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
