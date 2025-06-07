from dataclasses import dataclass

from pyaixm.generated.dq_relative_internal_positional_accuracy_type import (
    DqRelativeInternalPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqRelativeInternalPositionalAccuracy(
    DqRelativeInternalPositionalAccuracyType
):
    class Meta:
        name = "DQ_RelativeInternalPositionalAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
