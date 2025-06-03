from dataclasses import dataclass

from generated.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeType1(MeasureType):
    class Meta:
        name = "TimeType"
