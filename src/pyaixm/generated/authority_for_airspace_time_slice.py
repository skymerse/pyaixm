from dataclasses import dataclass

from pyaixm.generated.authority_for_airspace_time_slice_type import (
    AuthorityForAirspaceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAirspaceTimeSlice(AuthorityForAirspaceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
