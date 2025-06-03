from dataclasses import dataclass

from generated.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractReference(ReferenceType):
    """
    Gml:abstractReference may be used as the head of a subtitution group of more
    specific elements providing a value by-reference.
    """

    class Meta:
        name = "abstractReference"
        namespace = "http://www.opengis.net/gml/3.2"
