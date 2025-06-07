from dataclasses import dataclass

from generated.abstract_dq_thematic_accuracy_type import (
    AbstractDqThematicAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqThematicAccuracy(AbstractDqThematicAccuracyType):
    class Meta:
        name = "AbstractDQ_ThematicAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
