from dataclasses import dataclass

from pyaixm.generated.sc_crs_property_type import GeodeticDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatumRef(GeodeticDatumPropertyType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
