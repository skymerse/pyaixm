from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ridge_extension import RidgeExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RidgeTypeExtension:
    class Meta:
        global_type = False

    ridge_extension: Optional[RidgeExtension] = field(
        default=None,
        metadata={
            "name": "RidgeExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
