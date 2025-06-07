from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airport_supplies_service_time_slice_type_extension import (
    AirportSuppliesServiceTimeSliceTypeExtension,
)
from pyaixm.generated.callsign_detail_property_type import (
    CallsignDetailPropertyType,
)
from pyaixm.generated.code_facility_ranking_type import CodeFacilityRankingType
from pyaixm.generated.code_flight_destination_type import (
    CodeFlightDestinationType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.contact_information_property_type import (
    ContactInformationPropertyType,
)
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.fuel_property_type import FuelPropertyType
from pyaixm.generated.nitrogen_property_type import NitrogenPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.oil_property_type import OilPropertyType
from pyaixm.generated.oxygen_property_type import OxygenPropertyType
from pyaixm.generated.radio_communication_channel_property_type import (
    RadioCommunicationChannelPropertyType,
)
from pyaixm.generated.service_operational_status_property_type import (
    ServiceOperationalStatusPropertyType,
)
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.unit_property_type import UnitPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesServiceTimeSliceType(AbstractAixmtimeSliceType):
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
    airport_heliport: Iterable[AirportHeliportPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "airportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    fuel_supply: Iterable[FuelPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "fuelSupply",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    oil_supply: Iterable[OilPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "oilSupply",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    nitrogen_supply: Iterable[NitrogenPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "nitrogenSupply",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    oxygen_supply: Iterable[OxygenPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "oxygenSupply",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AirportSuppliesServiceTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
