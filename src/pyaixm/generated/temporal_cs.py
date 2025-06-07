from dataclasses import dataclass

from generated.temporal_cstype import TemporalCstype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml/3.2"
