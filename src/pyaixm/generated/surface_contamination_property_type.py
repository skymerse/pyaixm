from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.aircraft_stand_contamination import (
    AircraftStandContamination,
)
from pyaixm.generated.airport_heliport_contamination import (
    AirportHeliportContamination,
)
from pyaixm.generated.apron_contamination import ApronContamination
from pyaixm.generated.runway_contamination import RunwayContamination
from pyaixm.generated.runway_section_contamination import (
    RunwaySectionContamination,
)
from pyaixm.generated.taxiway_contamination import TaxiwayContamination
from pyaixm.generated.touch_down_lift_off_contamination import (
    TouchDownLiftOffContamination,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceContaminationPropertyType(AbstractAixmpropertyType):
    airport_heliport_contamination: Optional[AirportHeliportContamination] = (
        field(
            default=None,
            metadata={
                "name": "AirportHeliportContamination",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    aircraft_stand_contamination: Optional[AircraftStandContamination] = field(
        default=None,
        metadata={
            "name": "AircraftStandContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_contamination: Optional[ApronContamination] = field(
        default=None,
        metadata={
            "name": "ApronContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_contamination: Optional[
        TouchDownLiftOffContamination
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_section_contamination: Optional[RunwaySectionContamination] = field(
        default=None,
        metadata={
            "name": "RunwaySectionContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_contamination: Optional[TaxiwayContamination] = field(
        default=None,
        metadata={
            "name": "TaxiwayContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_contamination: Optional[RunwayContamination] = field(
        default=None,
        metadata={
            "name": "RunwayContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
