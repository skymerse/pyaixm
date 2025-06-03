from dataclasses import dataclass

from generated.oil_type import OilType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Oil(OilType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
