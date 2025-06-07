from dataclasses import dataclass

from pyaixm.generated.abstract_rs_reference_system_type import (
    AbstractRsReferenceSystemType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractRsReferenceSystem(AbstractRsReferenceSystemType):
    class Meta:
        name = "AbstractRS_ReferenceSystem"
        namespace = "http://www.isotc211.org/2005/gmd"
