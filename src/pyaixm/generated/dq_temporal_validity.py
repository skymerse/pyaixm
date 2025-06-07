from dataclasses import dataclass

from pyaixm.generated.dq_temporal_validity_type import DqTemporalValidityType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalValidity(DqTemporalValidityType):
    class Meta:
        name = "DQ_TemporalValidity"
        namespace = "http://www.isotc211.org/2005/gmd"
