from dataclasses import dataclass

from generated.abstract_dq_element_type import AbstractDqElementType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqCompletenessType(AbstractDqElementType):
    class Meta:
        name = "AbstractDQ_Completeness_Type"
