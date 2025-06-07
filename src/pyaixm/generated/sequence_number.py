from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SequenceNumber:
    """Used for the identification of the Time Slice concerned.

    See the AIXM Temporality model for details.
    """

    class Meta:
        name = "sequenceNumber"
        namespace = "http://www.aixm.aero/schema/5.1"

    value: Optional[int] = field(default=None)
