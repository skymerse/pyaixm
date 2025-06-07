from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.decimal_minutes import DecimalMinutes
from pyaixm.generated.degrees import Degrees
from pyaixm.generated.minutes import Minutes
from pyaixm.generated.seconds import Seconds

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsangleType:
    class Meta:
        name = "DMSAngleType"

    degrees: Optional[Degrees] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    decimal_minutes: Optional[DecimalMinutes] = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    minutes: Optional[Minutes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    seconds: Optional[Seconds] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
