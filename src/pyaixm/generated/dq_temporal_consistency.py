from dataclasses import dataclass

from pyaixm.generated.dq_temporal_consistency_type import (
    DqTemporalConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalConsistency(DqTemporalConsistencyType):
    class Meta:
        name = "DQ_TemporalConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
