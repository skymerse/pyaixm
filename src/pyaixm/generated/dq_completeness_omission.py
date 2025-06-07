from dataclasses import dataclass

from pyaixm.generated.dq_completeness_omission_type import (
    DqCompletenessOmissionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessOmission(DqCompletenessOmissionType):
    class Meta:
        name = "DQ_CompletenessOmission"
        namespace = "http://www.isotc211.org/2005/gmd"
