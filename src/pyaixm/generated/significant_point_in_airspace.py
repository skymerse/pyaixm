from dataclasses import dataclass

from pyaixm.generated.significant_point_in_airspace_type import (
    SignificantPointInAirspaceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SignificantPointInAirspace(SignificantPointInAirspaceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
