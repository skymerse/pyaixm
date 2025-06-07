from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_side_type import CodeSideType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstacle_placement_type_extension import (
    ObstaclePlacementTypeExtension,
)
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstaclePlacementType(AbstractAixmobjectType):
    obstacle_bearing: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "obstacleBearing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstacle_distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "obstacleDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_type: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "pointType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstacle_placement: Optional[CodeSideType] = field(
        default=None,
        metadata={
            "name": "obstaclePlacement",
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
    extension: Iterable[ObstaclePlacementTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
