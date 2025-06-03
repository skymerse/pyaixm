from dataclasses import dataclass, field
from typing import Optional

from generated.authority_for_airspace_time_slice import (
    AuthorityForAirspaceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAirspaceTimeSlicePropertyType:
    authority_for_airspace_time_slice: Optional[
        AuthorityForAirspaceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AuthorityForAirspaceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
