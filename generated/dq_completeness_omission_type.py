from dataclasses import dataclass

from generated.abstract_dq_completeness_type import AbstractDqCompletenessType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessOmissionType(AbstractDqCompletenessType):
    class Meta:
        name = "DQ_CompletenessOmission_Type"
