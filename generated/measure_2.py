from dataclasses import dataclass

from generated.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Measure2(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """

    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml/3.2"
