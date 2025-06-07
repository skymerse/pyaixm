from dataclasses import dataclass

from generated.approach_distance_table_type import ApproachDistanceTableType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachDistanceTable(ApproachDistanceTableType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
