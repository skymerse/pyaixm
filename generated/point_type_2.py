from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.note_property_type import NotePropertyType
from generated.point_type_1 import PointType1
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PointType2(PointType1):
    class Meta:
        name = "PointType"

    horizontal_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "horizontalAccuracy",
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
