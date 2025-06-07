from dataclasses import dataclass

from pyaixm.generated.image_crsproperty_type import ImageCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageCrsref(ImageCrspropertyType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
