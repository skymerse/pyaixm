from dataclasses import dataclass

from generated.temporal_crsproperty_type import TemporalCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCrsref(TemporalCrspropertyType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
