from dataclasses import dataclass

from pyaixm.generated.abstract_dq_result_type import AbstractDqResultType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqResult(AbstractDqResultType):
    class Meta:
        name = "AbstractDQ_Result"
        namespace = "http://www.isotc211.org/2005/gmd"
