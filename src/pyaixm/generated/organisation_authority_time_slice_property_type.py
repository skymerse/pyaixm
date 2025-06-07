from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.organisation_authority_time_slice import (
    OrganisationAuthorityTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityTimeSlicePropertyType:
    organisation_authority_time_slice: Optional[
        OrganisationAuthorityTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthorityTimeSlice",
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
