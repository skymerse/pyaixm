from dataclasses import dataclass, field
from typing import Optional

from generated.organisation_authority_extension import (
    OrganisationAuthorityExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityTimeSliceTypeExtension:
    class Meta:
        global_type = False

    organisation_authority_extension: Optional[
        OrganisationAuthorityExtension
    ] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthorityExtension",
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
