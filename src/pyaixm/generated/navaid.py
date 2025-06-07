from dataclasses import dataclass

from generated.navaid_type import NavaidType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Navaid(NavaidType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
