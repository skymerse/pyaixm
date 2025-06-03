from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.aerial_refuelling_anchor_property_type import (
    AerialRefuellingAnchorPropertyType,
)
from generated.aerial_refuelling_property_type import (
    AerialRefuellingPropertyType,
)
from generated.aerial_refuelling_time_slice_type_extension import (
    AerialRefuellingTimeSliceTypeExtension,
)
from generated.aerial_refuelling_track_property_type import (
    AerialRefuellingTrackPropertyType,
)
from generated.airspace_property_type import AirspacePropertyType
from generated.authority_for_aerial_refuelling_property_type import (
    AuthorityForAerialRefuellingPropertyType,
)
from generated.code_aerial_refuelling_prefix_type import (
    CodeAerialRefuellingPrefixType,
)
from generated.code_aerial_refuelling_type import CodeAerialRefuellingType
from generated.code_cardinal_direction_type import CodeCardinalDirectionType
from generated.code_direction_turn_type import CodeDirectionTurnType
from generated.code_tacanchannel_type import CodeTacanchannelType
from generated.code_yes_no_type import CodeYesNoType
from generated.no_number_type import NoNumberType
from generated.note_property_type import NotePropertyType
from generated.route_availability_property_type import (
    RouteAvailabilityPropertyType,
)
from generated.text_designator_type import TextDesignatorType
from generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTimeSliceType(AbstractAixmtimeSliceType):
    designator_prefix: Optional[CodeAerialRefuellingPrefixType] = field(
        default=None,
        metadata={
            "name": "designatorPrefix",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_number: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "designatorNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_suffix: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "designatorSuffix",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "designatorDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeAerialRefuellingType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radar_beacon_setting: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "radarBeaconSetting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    xband_radar_setting: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "xbandRadarSetting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    tanker_channel: Optional[CodeTacanchannelType] = field(
        default=None,
        metadata={
            "name": "tankerChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    receiver_channel: Optional[CodeTacanchannelType] = field(
        default=None,
        metadata={
            "name": "receiverChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    helicopter_route: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "helicopterRoute",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    special_refuelling: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "specialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    bidirectional_use: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "bidirectionalUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reverse_direction_turn: Optional[CodeDirectionTurnType] = field(
        default=None,
        metadata={
            "name": "reverseDirectionTurn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[RouteAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    protecting_airspace: Iterable[AirspacePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "protectingAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    track: Iterable[AerialRefuellingTrackPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    anchor: Iterable[AerialRefuellingAnchorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    opposite_track: Optional[AerialRefuellingPropertyType] = field(
        default=None,
        metadata={
            "name": "oppositeTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    managing_organisation: Iterable[
        AuthorityForAerialRefuellingPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "managingOrganisation",
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
    extension: Iterable[AerialRefuellingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
