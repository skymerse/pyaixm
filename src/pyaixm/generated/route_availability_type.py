from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from pyaixm.generated.airspace_layer_property_type import (
    AirspaceLayerPropertyType,
)
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_direction_type import CodeDirectionType
from pyaixm.generated.code_route_availability_type import (
    CodeRouteAvailabilityType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.route_availability_type_extension import (
    RouteAvailabilityTypeExtension,
)
from pyaixm.generated.timesheet_property_type import TimesheetPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteAvailabilityType(AbstractPropertiesWithScheduleType):
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
    direction: Optional[CodeDirectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    status: Optional[CodeRouteAvailabilityType] = field(
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
    extension: Iterable[RouteAvailabilityTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
