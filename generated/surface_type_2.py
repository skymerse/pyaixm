from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.note_property_type import NotePropertyType
from generated.surface_type_1 import SurfaceType1
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceType2(SurfaceType1):
    class Meta:
        name = "SurfaceType"

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
