from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.aircraft_characteristic_type_extension import (
    AircraftCharacteristicTypeExtension,
)
from generated.code_aircraft_category_type import CodeAircraftCategoryType
from generated.code_aircraft_engine_number_type import (
    CodeAircraftEngineNumberType,
)
from generated.code_aircraft_engine_type import CodeAircraftEngineType
from generated.code_aircraft_icaotype import CodeAircraftIcaotype
from generated.code_aircraft_type import CodeAircraftType
from generated.code_aircraft_wingspan_class_type import (
    CodeAircraftWingspanClassType,
)
from generated.code_communication_mode_type import CodeCommunicationModeType
from generated.code_equipment_anti_collision_type import (
    CodeEquipmentAntiCollisionType,
)
from generated.code_navigation_equipment_type import (
    CodeNavigationEquipmentType,
)
from generated.code_navigation_specification_type import (
    CodeNavigationSpecificationType,
)
from generated.code_rvsmtype import CodeRvsmtype
from generated.code_transponder_type import CodeTransponderType
from generated.code_value_interpretation_type import (
    CodeValueInterpretationType,
)
from generated.code_wake_turbulence_type import CodeWakeTurbulenceType
from generated.no_number_type import NoNumberType
from generated.note_property_type import NotePropertyType
from generated.val_distance_type import ValDistanceType
from generated.val_speed_type import ValSpeedType
from generated.val_weight_type import ValWeightType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftCharacteristicType(AbstractAixmobjectType):
    type_value: Optional[CodeAircraftType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    engine: Optional[CodeAircraftEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    number_engine: Optional[CodeAircraftEngineNumberType] = field(
        default=None,
        metadata={
            "name": "numberEngine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_aircraft_icao: Optional[CodeAircraftIcaotype] = field(
        default=None,
        metadata={
            "name": "typeAircraftICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft_landing_category: Optional[CodeAircraftCategoryType] = field(
        default=None,
        metadata={
            "name": "aircraftLandingCategory",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    wing_span: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "wingSpan",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    wing_span_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "wingSpanInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    class_wing_span: Optional[CodeAircraftWingspanClassType] = field(
        default=None,
        metadata={
            "name": "classWingSpan",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    weight: Optional[ValWeightType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    weight_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "weightInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    passengers: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    passengers_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "passengersInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "speedInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    wake_turbulence: Optional[CodeWakeTurbulenceType] = field(
        default=None,
        metadata={
            "name": "wakeTurbulence",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    navigation_equipment: Optional[CodeNavigationEquipmentType] = field(
        default=None,
        metadata={
            "name": "navigationEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    navigation_specification: Optional[CodeNavigationSpecificationType] = (
        field(
            default=None,
            metadata={
                "name": "navigationSpecification",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    vertical_separation_capability: Optional[CodeRvsmtype] = field(
        default=None,
        metadata={
            "name": "verticalSeparationCapability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    anti_collision_and_separation_equipment: Optional[
        CodeEquipmentAntiCollisionType
    ] = field(
        default=None,
        metadata={
            "name": "antiCollisionAndSeparationEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    communication_equipment: Optional[CodeCommunicationModeType] = field(
        default=None,
        metadata={
            "name": "communicationEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surveillance_equipment: Optional[CodeTransponderType] = field(
        default=None,
        metadata={
            "name": "surveillanceEquipment",
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
    extension: Iterable[AircraftCharacteristicTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
