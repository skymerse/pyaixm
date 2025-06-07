from dataclasses import dataclass

from generated.approach_lighting_system_type import ApproachLightingSystemType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystem(ApproachLightingSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
