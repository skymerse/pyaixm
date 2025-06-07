from dataclasses import dataclass

from generated.sc_crs_property_type import VerticalDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatumRef(VerticalDatumPropertyType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
