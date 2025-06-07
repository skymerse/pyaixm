from dataclasses import dataclass

from pyaixm.generated.airspace_activation_type import AirspaceActivationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceActivation(AirspaceActivationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
