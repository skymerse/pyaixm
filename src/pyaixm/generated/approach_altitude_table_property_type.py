from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.approach_altitude_table import ApproachAltitudeTable

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachAltitudeTablePropertyType(AbstractAixmpropertyType):
    approach_altitude_table: Optional[ApproachAltitudeTable] = field(
        default=None,
        metadata={
            "name": "ApproachAltitudeTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
