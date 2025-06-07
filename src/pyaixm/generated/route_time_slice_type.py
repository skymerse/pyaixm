from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_flight_rule_type import CodeFlightRuleType
from pyaixm.generated.code_military_status_type import CodeMilitaryStatusType
from pyaixm.generated.code_military_training_type import (
    CodeMilitaryTrainingType,
)
from pyaixm.generated.code_route_designator_letter_type import (
    CodeRouteDesignatorLetterType,
)
from pyaixm.generated.code_route_designator_prefix_type import (
    CodeRouteDesignatorPrefixType,
)
from pyaixm.generated.code_route_origin_type import CodeRouteOriginType
from pyaixm.generated.code_route_type import CodeRouteType
from pyaixm.generated.code_upper_alpha_type import CodeUpperAlphaType
from pyaixm.generated.no_number_type import NoNumberType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.route_time_slice_type_extension import (
    RouteTimeSliceTypeExtension,
)
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteTimeSliceType(AbstractAixmtimeSliceType):
    designator_prefix: Optional[CodeRouteDesignatorPrefixType] = field(
        default=None,
        metadata={
            "name": "designatorPrefix",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_second_letter: Optional[CodeRouteDesignatorLetterType] = field(
        default=None,
        metadata={
            "name": "designatorSecondLetter",
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
    multiple_identifier: Optional[CodeUpperAlphaType] = field(
        default=None,
        metadata={
            "name": "multipleIdentifier",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location_designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "locationDesignator",
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
    type_value: Optional[CodeRouteType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_rule: Optional[CodeFlightRuleType] = field(
        default=None,
        metadata={
            "name": "flightRule",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    international_use: Optional[CodeRouteOriginType] = field(
        default=None,
        metadata={
            "name": "internationalUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    military_use: Optional[CodeMilitaryStatusType] = field(
        default=None,
        metadata={
            "name": "militaryUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    military_training_type: Optional[CodeMilitaryTrainingType] = field(
        default=None,
        metadata={
            "name": "militaryTrainingType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    user_organisation: Optional[OrganisationAuthorityPropertyType] = field(
        default=None,
        metadata={
            "name": "userOrganisation",
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
    extension: Iterable[RouteTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
