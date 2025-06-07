from dataclasses import dataclass

from pyaixm.generated.approach_altitude_table_type import (
    ApproachAltitudeTableType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachAltitudeTable(ApproachAltitudeTableType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
