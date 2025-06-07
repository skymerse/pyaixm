from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_communication_channel_type import (
    CodeCommunicationChannelType,
)
from generated.code_communication_direction_type import (
    CodeCommunicationDirectionType,
)
from generated.code_communication_mode_type import CodeCommunicationModeType
from generated.code_facility_ranking_type import CodeFacilityRankingType
from generated.code_radio_emission_type import CodeRadioEmissionType
from generated.code_yes_no_type import CodeYesNoType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.note_property_type import NotePropertyType
from generated.radio_communication_channel_time_slice_type_extension import (
    RadioCommunicationChannelTimeSliceTypeExtension,
)
from generated.radio_communication_operational_status_property_type import (
    RadioCommunicationOperationalStatusPropertyType,
)
from generated.text_designator_type import TextDesignatorType
from generated.val_frequency_type import ValFrequencyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationChannelTimeSliceType(AbstractAixmtimeSliceType):
    mode: Optional[CodeCommunicationModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    rank: Optional[CodeFacilityRankingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    frequency_transmission: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "name": "frequencyTransmission",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    frequency_reception: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "name": "frequencyReception",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    channel: Optional[CodeCommunicationChannelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    logon: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    emission_type: Optional[CodeRadioEmissionType] = field(
        default=None,
        metadata={
            "name": "emissionType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    selective_call: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "selectiveCall",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_checked: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flightChecked",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    traffic_direction: Optional[CodeCommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "trafficDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Iterable[ElevatedPointPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[RadioCommunicationOperationalStatusPropertyType] = (
        field(
            default_factory=list,
            metadata={
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
    extension: Iterable[RadioCommunicationChannelTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
