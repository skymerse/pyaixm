from dataclasses import dataclass

from pyaixm.generated.circling_restriction_type import CirclingRestrictionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingRestriction(CirclingRestrictionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
