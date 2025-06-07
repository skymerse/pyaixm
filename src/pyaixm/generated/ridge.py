from dataclasses import dataclass

from pyaixm.generated.ridge_type import RidgeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Ridge(RidgeType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
