from dataclasses import dataclass

from pyaixm.generated.intermediate_leg_type import IntermediateLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class IntermediateLeg(IntermediateLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
