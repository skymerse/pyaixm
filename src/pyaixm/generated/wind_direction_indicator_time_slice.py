from dataclasses import dataclass

from pyaixm.generated.wind_direction_indicator_time_slice_type import (
    WindDirectionIndicatorTimeSliceType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class WindDirectionIndicatorTimeSlice(WindDirectionIndicatorTimeSliceType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
