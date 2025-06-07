from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airport_sign_time_slice_type_extension import (
    AirportSignTimeSliceTypeExtension,
)
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_sign_description_type import CodeSignDescriptionType
from pyaixm.generated.code_sign_status_type import CodeSignStatusType
from pyaixm.generated.code_sign_type import CodeSignType
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.point_property_type_2 import PointPropertyType2
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from pyaixm.generated.runway_property_type import RunwayPropertyType
from pyaixm.generated.taxiway_property_type import TaxiwayPropertyType
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportSignTimeSliceType(AbstractAixmtimeSliceType):
    description: Optional[CodeSignDescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    sign_type: Optional[CodeSignType] = field(
        default=None,
        metadata={
            "name": "signType",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    status: Optional[CodeSignStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    location_fix_designated_point: Optional[DesignatedPointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "location_fixDesignatedPoint",
                "type": "Element",
                "namespace": "urn:us.gov.dot.faa.aim.fns",
                "nillable": True,
            },
        )
    )
    location_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "location_navaidSystem",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    location_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "location_aimingPoint",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    location_runway_point: Optional[RunwayCentrelinePointPropertyType] = field(
        default=None,
        metadata={
            "name": "location_runwayPoint",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    location_airport_reference_point: Optional[AirportHeliportPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "location_airportReferencePoint",
                "type": "Element",
                "namespace": "urn:us.gov.dot.faa.aim.fns",
                "nillable": True,
            },
        )
    )
    location_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    associated_runway_direction: Optional[RunwayDirectionPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedRunwayDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    associated_runway: Optional[RunwayPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedRunway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    associated_taxiway: Optional[TaxiwayPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedTaxiway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    extension: Iterable[AirportSignTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
