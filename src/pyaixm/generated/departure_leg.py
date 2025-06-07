from dataclasses import dataclass

from pyaixm.generated.departure_leg_type import DepartureLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureLeg(DepartureLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
