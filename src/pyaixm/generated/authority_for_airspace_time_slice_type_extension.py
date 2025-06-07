from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.authority_for_airspace_extension import (
    AuthorityForAirspaceExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAirspaceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    authority_for_airspace_extension: Optional[
        AuthorityForAirspaceExtension
    ] = field(
        default=None,
        metadata={
            "name": "AuthorityForAirspaceExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
