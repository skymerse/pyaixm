from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_yes_no_type import CodeYesNoType
from generated.note_property_type import NotePropertyType
from generated.surveillance_ground_station_type_extension import (
    SurveillanceGroundStationTypeExtension,
)
from generated.unit_property_type import UnitPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveillanceGroundStationType(AbstractAixmobjectType):
    video_map: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "videoMap",
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
    the_unit: Optional[UnitPropertyType] = field(
        default=None,
        metadata={
            "name": "theUnit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[SurveillanceGroundStationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
