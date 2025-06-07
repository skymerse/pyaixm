from dataclasses import dataclass

from generated.apron_light_system_type import ApronLightSystemType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronLightSystem(ApronLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
