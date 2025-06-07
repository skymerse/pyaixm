from dataclasses import dataclass

from pyaixm.generated.geo_border_extension_type import GeoBorderExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GeoBorderExtension(GeoBorderExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
