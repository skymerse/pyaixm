from dataclasses import dataclass

from pyaixm.generated.dq_absolute_external_positional_accuracy_type import (
    DqAbsoluteExternalPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqAbsoluteExternalPositionalAccuracy(
    DqAbsoluteExternalPositionalAccuracyType
):
    class Meta:
        name = "DQ_AbsoluteExternalPositionalAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
