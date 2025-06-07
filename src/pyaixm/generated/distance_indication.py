from dataclasses import dataclass

from generated.distance_indication_type import DistanceIndicationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DistanceIndication(DistanceIndicationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
