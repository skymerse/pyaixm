from dataclasses import dataclass, field
from typing import Optional

from generated.apron_element_extension import ApronElementExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronElementTimeSliceTypeExtension:
    class Meta:
        global_type = False

    apron_element_extension: Optional[ApronElementExtension] = field(
        default=None,
        metadata={
            "name": "ApronElementExtension",
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
