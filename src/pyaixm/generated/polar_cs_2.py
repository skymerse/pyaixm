from dataclasses import dataclass

from generated.polar_csproperty_type import PolarCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolarCs2(PolarCspropertyType):
    """
    Gml:polarCS is an association role to the polar coordinate system used by this
    CRS.
    """

    class Meta:
        name = "polarCS"
        namespace = "http://www.opengis.net/gml/3.2"
