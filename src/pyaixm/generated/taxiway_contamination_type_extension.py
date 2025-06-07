from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.surface_contamination_extension import (
    SurfaceContaminationExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayContaminationTypeExtension:
    class Meta:
        global_type = False

    surface_contamination_extension: Optional[
        SurfaceContaminationExtension
    ] = field(
        default=None,
        metadata={
            "name": "SurfaceContaminationExtension",
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
