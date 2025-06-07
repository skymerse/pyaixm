from dataclasses import dataclass

from generated.time_csproperty_type import TimeCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCs2(TimeCspropertyType):
    """
    Gml:timeCS is an association role to the time coordinate system used by this
    CRS.
    """

    class Meta:
        name = "timeCS"
        namespace = "http://www.opengis.net/gml/3.2"
