from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_meteo_conditions_type import CodeMeteoConditionsType
from pyaixm.generated.code_value_interpretation_type import (
    CodeValueInterpretationType,
)
from pyaixm.generated.meteorology_type_extension import (
    MeteorologyTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_distance_type import ValDistanceType

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
