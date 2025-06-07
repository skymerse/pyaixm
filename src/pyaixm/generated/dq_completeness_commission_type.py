from dataclasses import dataclass

from pyaixm.generated.abstract_dq_completeness_type import (
    AbstractDqCompletenessType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessCommissionType(AbstractDqCompletenessType):
    class Meta:
        name = "DQ_CompletenessCommission_Type"
