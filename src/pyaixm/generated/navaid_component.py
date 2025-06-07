from dataclasses import dataclass

from generated.navaid_component_type import NavaidComponentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidComponent(NavaidComponentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
