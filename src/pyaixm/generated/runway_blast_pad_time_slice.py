from dataclasses import dataclass

from pyaixm.generated.runway_blast_pad_time_slice_type import (
    RunwayBlastPadTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayBlastPadTimeSlice(RunwayBlastPadTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
