from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.code_obstacle_assessment_surface_type import (
    CodeObstacleAssessmentSurfaceType,
)
from pyaixm.generated.code_obstruction_id_surface_zone_type import (
    CodeObstructionIdSurfaceZoneType,
)
from pyaixm.generated.curve_property_type_2 import CurvePropertyType2
from pyaixm.generated.no_number_type import NoNumberType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstacle_assessment_area_type_extension import (
    ObstacleAssessmentAreaTypeExtension,
)
from pyaixm.generated.obstruction_property_type import ObstructionPropertyType
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_slope_type import ValSlopeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAssessmentAreaType(AbstractAixmobjectType):
    type_value: Optional[CodeObstacleAssessmentSurfaceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    section_number: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "sectionNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    assessed_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "assessedAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope_lower_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "slopeLowerAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    gradient_low_high: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "name": "gradientLowHigh",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_zone: Optional[CodeObstructionIdSurfaceZoneType] = field(
        default=None,
        metadata={
            "name": "surfaceZone",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    safety_regulation: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "safetyRegulation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft_category: Iterable[AircraftCharacteristicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "aircraftCategory",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_obstacle: Iterable[ObstructionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "significantObstacle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    starting_curve: Optional[CurvePropertyType2] = field(
        default=None,
        metadata={
            "name": "startingCurve",
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
    extension: Iterable[ObstacleAssessmentAreaTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
