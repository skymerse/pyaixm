from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_height_reference_type import CodeHeightReferenceType
from generated.code_minimum_altitude_type import CodeMinimumAltitudeType
from generated.code_minimum_height_type import CodeMinimumHeightType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.equipment_unavailable_adjustment_property_type import (
    EquipmentUnavailableAdjustmentPropertyType,
)
from generated.minima_type_extension import MinimaTypeExtension
from generated.note_property_type import NotePropertyType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MinimaType(AbstractAixmobjectType):
    altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_code: Optional[CodeMinimumAltitudeType] = field(
        default=None,
        metadata={
            "name": "altitudeCode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "altitudeReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    height: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    military_height: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "militaryHeight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radio_height: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "radioHeight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    height_code: Optional[CodeMinimumHeightType] = field(
        default=None,
        metadata={
            "name": "heightCode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    height_reference: Optional[CodeHeightReferenceType] = field(
        default=None,
        metadata={
            "name": "heightReference",
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
    military_visibility: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "militaryVisibility",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    mandatory_rvr: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "mandatoryRVR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    remote_altimeter_minima: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "remoteAltimeterMinima",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    adjustment_inop: Iterable[EquipmentUnavailableAdjustmentPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "adjustmentINOP",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[MinimaTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
