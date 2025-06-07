from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.apron_extension import ApronExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronTimeSliceTypeExtension:
    class Meta:
        global_type = False

    apron_extension: Optional[ApronExtension] = field(
        default=None,
        metadata={
            "name": "ApronExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
