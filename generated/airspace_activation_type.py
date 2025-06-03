from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from generated.airspace_activation_type_extension import (
    AirspaceActivationTypeExtension,
)
from generated.airspace_layer_property_type import AirspaceLayerPropertyType
from generated.code_airspace_activity_type import CodeAirspaceActivityType
from generated.code_status_airspace_type import CodeStatusAirspaceType
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from generated.timesheet_property_type import TimesheetPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceActivationType(AbstractPropertiesWithScheduleType):
    time_interval: Iterable[TimesheetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeInterval",
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
    special_date_authority: Iterable[OrganisationAuthorityPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "specialDateAuthority",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    activity: Optional[CodeAirspaceActivityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    status: Optional[CodeStatusAirspaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    levels: Iterable[AirspaceLayerPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    user: Iterable[OrganisationAuthorityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft: Iterable[AircraftCharacteristicPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AirspaceActivationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
