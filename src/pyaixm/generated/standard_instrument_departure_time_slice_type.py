from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_design_standard_type import CodeDesignStandardType
from pyaixm.generated.code_procedure_coding_standard_type import (
    CodeProcedureCodingStandardType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.landing_takeoff_area_collection_property_type import (
    LandingTakeoffAreaCollectionPropertyType,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.procedure_availability_property_type import (
    ProcedureAvailabilityPropertyType,
)
from pyaixm.generated.procedure_transition_property_type import (
    ProcedureTransitionPropertyType,
)
from pyaixm.generated.radar_system_property_type import RadarSystemPropertyType
from pyaixm.generated.safe_altitude_area_property_type import (
    SafeAltitudeAreaPropertyType,
)
from pyaixm.generated.special_navigation_system_property_type import (
    SpecialNavigationSystemPropertyType,
)
from pyaixm.generated.standard_instrument_departure_time_slice_type_extension import (
    StandardInstrumentDepartureTimeSliceTypeExtension,
)
from pyaixm.generated.text_instruction_type import TextInstructionType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.text_sidstardesignator_type import (
    TextSidstardesignatorType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDepartureTimeSliceType(AbstractAixmtimeSliceType):
    communication_failure_instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "name": "communicationFailureInstruction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    design_criteria: Optional[CodeDesignStandardType] = field(
        default=None,
        metadata={
            "name": "designCriteria",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    coding_standard: Optional[CodeProcedureCodingStandardType] = field(
        default=None,
        metadata={
            "name": "codingStandard",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_checked: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flightChecked",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    rnav: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "RNAV",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[ProcedureAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    airport_heliport: Iterable[AirportHeliportPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "airportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft_characteristic: Iterable[AircraftCharacteristicPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "aircraftCharacteristic",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    flight_transition: Iterable[ProcedureTransitionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "flightTransition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    guidance_facility_navaid: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "guidanceFacility_navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    guidance_facility_special_navigation_system: Optional[
        SpecialNavigationSystemPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "guidanceFacility_specialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    guidance_facility_radar: Optional[RadarSystemPropertyType] = field(
        default=None,
        metadata={
            "name": "guidanceFacility_radar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    safe_altitude: Optional[SafeAltitudeAreaPropertyType] = field(
        default=None,
        metadata={
            "name": "safeAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[TextSidstardesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contingency_route: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "contingencyRoute",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    takeoff: Optional[LandingTakeoffAreaCollectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[StandardInstrumentDepartureTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
