from dataclasses import dataclass

from generated.md_image_description_type import MdImageDescriptionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImageDescription(MdImageDescriptionType):
    class Meta:
        name = "MD_ImageDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
