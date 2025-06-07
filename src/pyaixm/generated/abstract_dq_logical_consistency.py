from dataclasses import dataclass

from generated.abstract_dq_logical_consistency_type import (
    AbstractDqLogicalConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqLogicalConsistency(AbstractDqLogicalConsistencyType):
    class Meta:
        name = "AbstractDQ_LogicalConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
