from dataclasses import dataclass

from pyaixm.generated.navaid_time_slice_type import NavaidTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidTimeSlice(NavaidTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
