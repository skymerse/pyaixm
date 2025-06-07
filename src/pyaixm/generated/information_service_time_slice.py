from dataclasses import dataclass

from generated.information_service_time_slice_type import (
    InformationServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationServiceTimeSlice(InformationServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
