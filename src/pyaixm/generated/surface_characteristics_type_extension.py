from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.surface_characteristics_extension import (
    SurfaceCharacteristicsExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceCharacteristicsTypeExtension:
    class Meta:
        global_type = False

    surface_characteristics_extension: Optional[
        SurfaceCharacteristicsExtension
    ] = field(
        default=None,
        metadata={
            "name": "SurfaceCharacteristicsExtension",
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
