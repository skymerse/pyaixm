from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxiway_extension_1 import TaxiwayExtension1
from pyaixm.generated.taxiway_extension_2 import TaxiwayExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxiway_extension: Optional[TaxiwayExtension2] = field(
        default=None,
        metadata={
            "name": "TaxiwayExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_taxiway_extension: Optional[
        TaxiwayExtension1
    ] = field(
        default=None,
        metadata={
            "name": "TaxiwayExtension",
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
