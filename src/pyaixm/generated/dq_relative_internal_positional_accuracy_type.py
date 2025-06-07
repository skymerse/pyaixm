from dataclasses import dataclass

from pyaixm.generated.abstract_dq_positional_accuracy_type import (
    AbstractDqPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqRelativeInternalPositionalAccuracyType(
    AbstractDqPositionalAccuracyType
):
    class Meta:
        name = "DQ_RelativeInternalPositionalAccuracy_Type"
