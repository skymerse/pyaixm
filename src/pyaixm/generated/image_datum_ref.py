from dataclasses import dataclass

from generated.sc_crs_property_type import ImageDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatumRef(ImageDatumPropertyType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
