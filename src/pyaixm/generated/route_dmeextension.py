from dataclasses import dataclass

from pyaixm.generated.route_dmeextension_type import RouteDmeextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RouteDmeextension(RouteDmeextensionType):
    class Meta:
        name = "RouteDMEExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
