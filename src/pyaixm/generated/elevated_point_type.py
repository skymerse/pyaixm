from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.code_vertical_datum_type import CodeVerticalDatumType
from pyaixm.generated.elevated_point_type_extension import (
    ElevatedPointTypeExtension,
)
from pyaixm.generated.point_type_2 import PointType2
from pyaixm.generated.val_distance_signed_type import ValDistanceSignedType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedPointType(PointType2):
    elevation: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    geoid_undulation: Optional[ValDistanceSignedType] = field(
        default=None,
        metadata={
            "name": "geoidUndulation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_datum: Optional[CodeVerticalDatumType] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "verticalAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ElevatedPointTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
