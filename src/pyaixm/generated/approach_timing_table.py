from dataclasses import dataclass

from generated.approach_timing_table_type import ApproachTimingTableType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachTimingTable(ApproachTimingTableType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
