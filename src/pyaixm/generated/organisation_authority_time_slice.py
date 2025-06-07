from dataclasses import dataclass

from pyaixm.generated.organisation_authority_time_slice_type import (
    OrganisationAuthorityTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityTimeSlice(OrganisationAuthorityTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
