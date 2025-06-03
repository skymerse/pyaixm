from dataclasses import dataclass, field
from typing import Optional

from generated.fuel_extension import FuelExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FuelTypeExtension:
    class Meta:
        global_type = False

    fuel_extension: Optional[FuelExtension] = field(
        default=None,
        metadata={
            "name": "FuelExtension",
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
