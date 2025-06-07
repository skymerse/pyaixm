from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_sign_time_slice import AirportSignTimeSlice

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportSignTimeSlicePropertyType:
    airport_sign_time_slice: Optional[AirportSignTimeSlice] = field(
        default=None,
        metadata={
            "name": "AirportSignTimeSlice",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
