from dataclasses import dataclass, field
from typing import Optional

from generated.decimal_minutes import DecimalMinutes
from generated.degrees import Degrees
from generated.minutes import Minutes
from generated.seconds import Seconds

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
