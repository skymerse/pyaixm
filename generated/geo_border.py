from dataclasses import dataclass

from generated.geo_border_type import GeoBorderType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GeoBorder(GeoBorderType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
