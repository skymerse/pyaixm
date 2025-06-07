from dataclasses import dataclass

from generated.abstract_dq_positional_accuracy_type import (
    AbstractDqPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqPositionalAccuracy(AbstractDqPositionalAccuracyType):
    class Meta:
        name = "AbstractDQ_PositionalAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
