from dataclasses import dataclass

from pyaixm.generated.light_activation_type import LightActivationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightActivation(LightActivationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
