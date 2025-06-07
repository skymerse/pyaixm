from dataclasses import dataclass

from pyaixm.generated.final_profile_type import FinalProfileType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalProfile(FinalProfileType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
