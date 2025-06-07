from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_meteo_conditions_type import CodeMeteoConditionsType
from generated.code_value_interpretation_type import (
    CodeValueInterpretationType,
)
from generated.meteorology_type_extension import MeteorologyTypeExtension
from generated.note_property_type import NotePropertyType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MeteorologyType(AbstractAixmobjectType):
    flight_conditions: Optional[CodeMeteoConditionsType] = field(
        default=None,
        metadata={
            "name": "flightConditions",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    visibility: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    visibility_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "visibilityInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    runway_visual_range: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "runwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    runway_visual_range_interpretation: Optional[
        CodeValueInterpretationType
    ] = field(
        default=None,
        metadata={
            "name": "runwayVisualRangeInterpretation",
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
    extension: Iterable[MeteorologyTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
