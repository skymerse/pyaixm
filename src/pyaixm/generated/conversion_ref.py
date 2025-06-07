from dataclasses import dataclass

from generated.conversion_property_type import ConversionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ConversionRef(ConversionPropertyType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml/3.2"
