from dataclasses import dataclass, field
from typing import Optional

from generated.marking_extension import MarkingExtension
from generated.taxiway_marking_extension_1 import TaxiwayMarkingExtension1
from generated.taxiway_marking_extension_2 import TaxiwayMarkingExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxiway_marking_extension: Optional[TaxiwayMarkingExtension2] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarkingExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_taxiway_marking_extension: Optional[
        TaxiwayMarkingExtension1
    ] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarkingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    marking_extension: Optional[MarkingExtension] = field(
        default=None,
        metadata={
            "name": "MarkingExtension",
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
