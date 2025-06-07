from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.interpretation_value import InterpretationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Interpretation:
    """Property indicating how the timeslice is to be interpreted.

    See the AIXM Temporality model for details.
    """

    class Meta:
        name = "interpretation"
        namespace = "http://www.aixm.aero/schema/5.1"

    value: Optional[InterpretationValue] = field(default=None)
