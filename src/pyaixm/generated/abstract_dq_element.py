from dataclasses import dataclass

from pyaixm.generated.abstract_dq_element_type import AbstractDqElementType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqElement(AbstractDqElementType):
    class Meta:
        name = "AbstractDQ_Element"
        namespace = "http://www.isotc211.org/2005/gmd"
