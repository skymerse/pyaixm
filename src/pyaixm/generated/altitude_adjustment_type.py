from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.altitude_adjustment_type_extension import (
    AltitudeAdjustmentTypeExtension,
)
from pyaixm.generated.code_altitude_adjustment_type import (
    CodeAltitudeAdjustmentType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltitudeAdjustmentType(AbstractAixmobjectType):
    altitude_adjustment_type: Optional[CodeAltitudeAdjustmentType] = field(
        default=None,
        metadata={
            "name": "altitudeAdjustmentType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    primary_alternate_minimum: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "primaryAlternateMinimum",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_adjustment: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "altitudeAdjustment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    local_remote_code: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "localRemoteCode",
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
    extension: Iterable[AltitudeAdjustmentTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
