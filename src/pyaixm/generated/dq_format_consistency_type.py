from dataclasses import dataclass

from pyaixm.generated.abstract_dq_logical_consistency_type import (
    AbstractDqLogicalConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqFormatConsistencyType(AbstractDqLogicalConsistencyType):
    class Meta:
        name = "DQ_FormatConsistency_Type"
