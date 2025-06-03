from dataclasses import dataclass

from generated.rules_procedures_time_slice_type import (
    RulesProceduresTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RulesProceduresTimeSlice(RulesProceduresTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
