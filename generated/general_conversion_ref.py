from dataclasses import dataclass

from generated.sc_crs_property_type import GeneralConversionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralConversionRef(GeneralConversionPropertyType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml/3.2"
