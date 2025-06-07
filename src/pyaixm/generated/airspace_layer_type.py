from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.airspace_layer_type_extension import AirspaceLayerTypeExtension
from generated.code_altitude_use_type import CodeAltitudeUseType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.note_property_type import NotePropertyType
from generated.standard_level_column_property_type import (
    StandardLevelColumnPropertyType,
)
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceLayerType(AbstractAixmobjectType):
    upper_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "upperLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "lowerLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_interpretation: Optional[CodeAltitudeUseType] = field(
        default=None,
        metadata={
            "name": "altitudeInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    discrete_level_series: Optional[StandardLevelColumnPropertyType] = field(
        default=None,
        metadata={
            "name": "discreteLevelSeries",
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
    extension: Iterable[AirspaceLayerTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
