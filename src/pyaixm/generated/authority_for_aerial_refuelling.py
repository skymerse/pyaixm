from dataclasses import dataclass

from pyaixm.generated.authority_for_aerial_refuelling_type import (
    AuthorityForAerialRefuellingType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAerialRefuelling(AuthorityForAerialRefuellingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
