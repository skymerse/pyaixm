from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.circle_sector_property_type import CircleSectorPropertyType
from generated.code_radio_frequency_area_type import CodeRadioFrequencyAreaType
from generated.code_radio_signal_type import CodeRadioSignalType
from generated.navaid_equipment_property_type import (
    NavaidEquipmentPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.precision_approach_radar_property_type import (
    PrecisionApproachRadarPropertyType,
)
from generated.radio_communication_channel_property_type import (
    RadioCommunicationChannelPropertyType,
)
from generated.radio_frequency_area_time_slice_type_extension import (
    RadioFrequencyAreaTimeSliceTypeExtension,
)
from generated.secondary_surveillance_radar_property_type import (
    SecondarySurveillanceRadarPropertyType,
)
from generated.special_navigation_station_property_type import (
    SpecialNavigationStationPropertyType,
)
from generated.surface_property_type_2 import SurfacePropertyType2
from generated.val_angle_type import ValAngleType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioFrequencyAreaTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeRadioFrequencyAreaType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_scallop: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "angleScallop",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    signal_type: Optional[CodeRadioSignalType] = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    equipment_navaid_equipment: Optional[NavaidEquipmentPropertyType] = field(
        default=None,
        metadata={
            "name": "equipment_navaidEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    equipment_frequency: Optional[RadioCommunicationChannelPropertyType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    equipment_special_navigation_station: Optional[
        SpecialNavigationStationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "equipment_specialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    equipment_precision_approach_radar: Optional[
        PrecisionApproachRadarPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "equipment_precisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    equipment_radar: Optional[SecondarySurveillanceRadarPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector: Iterable[CircleSectorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Iterable[SurfacePropertyType2] = field(
        default_factory=list,
        metadata={
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
    extension: Iterable[RadioFrequencyAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
