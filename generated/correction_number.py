from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CorrectionNumber:
    """Used for indicating the order of the corrections of a Time Slice.

    See the AIXM Temporality model for details.
    """

    class Meta:
        name = "correctionNumber"
        namespace = "http://www.aixm.aero/schema/5.1"

    value: Optional[int] = field(default=None)
