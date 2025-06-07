from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.aerial_refuelling_property_type import (
    AerialRefuellingPropertyType,
)
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.airspace_property_type import AirspacePropertyType
from generated.callsign_detail_property_type import CallsignDetailPropertyType
from generated.code_facility_ranking_type import CodeFacilityRankingType
from generated.code_flight_destination_type import CodeFlightDestinationType
from generated.code_service_information_type import CodeServiceInformationType
from generated.code_yes_no_type import CodeYesNoType
from generated.contact_information_property_type import (
    ContactInformationPropertyType,
)
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.holding_pattern_property_type import HoldingPatternPropertyType
from generated.information_service_time_slice_type_extension import (
    InformationServiceTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.procedure_property_type_2 import ProcedurePropertyType2
from generated.radio_communication_channel_property_type import (
    RadioCommunicationChannelPropertyType,
)
from generated.route_portion_property_type import RoutePortionPropertyType
from generated.service_operational_status_property_type import (
    ServiceOperationalStatusPropertyType,
)
from generated.text_name_type import TextNameType
from generated.unit_property_type import UnitPropertyType
from generated.vorproperty_type import VorpropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationServiceTimeSliceType(AbstractAixmtimeSliceType):
    flight_operations: Optional[CodeFlightDestinationType] = field(
        default=None,
        metadata={
            "name": "flightOperations",
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
    compliant_icao: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "compliantICAO",
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
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    service_provider: Optional[UnitPropertyType] = field(
        default=None,
        metadata={
            "name": "serviceProvider",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    call_sign: Iterable[CallsignDetailPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "call-sign",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radio_communication: Iterable[RadioCommunicationChannelPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "radioCommunication",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    ground_communication: Iterable[ContactInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "groundCommunication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[ServiceOperationalStatusPropertyType] = field(
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
    type_value: Optional[CodeServiceInformationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    voice: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    data_link: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "dataLink",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    recorded: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    navaid_broadcast: Iterable[VorpropertyType] = field(
        default_factory=list,
        metadata={
            "name": "navaidBroadcast",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_airspace: Iterable[AirspacePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "clientAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_airport: Iterable[AirportHeliportPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "clientAirport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_route: Iterable[RoutePortionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "clientRoute",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_procedure: Iterable[ProcedurePropertyType2] = field(
        default_factory=list,
        metadata={
            "name": "clientProcedure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_holding: Iterable[HoldingPatternPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "clientHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    client_aerial_refuelling: Iterable[AerialRefuellingPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "clientAerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[InformationServiceTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
