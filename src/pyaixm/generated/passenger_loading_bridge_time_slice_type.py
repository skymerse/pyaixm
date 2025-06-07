from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_stand_property_type import (
    AircraftStandPropertyType,
)
from pyaixm.generated.code_loading_bridge_type import CodeLoadingBridgeType
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.passenger_loading_bridge_time_slice_type_extension import (
    PassengerLoadingBridgeTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerLoadingBridgeTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeLoadingBridgeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_stand: Iterable[AircraftStandPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "associatedStand",
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
    extension: Iterable[PassengerLoadingBridgeTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
