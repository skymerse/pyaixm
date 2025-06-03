from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airspace_property_type import AirspacePropertyType
from generated.authority_for_airspace_time_slice_type_extension import (
    AuthorityForAirspaceTimeSliceTypeExtension,
)
from generated.code_authority_type import CodeAuthorityType
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAirspaceTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeAuthorityType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    responsible_organisation: Optional[OrganisationAuthorityPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "responsibleOrganisation",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    assigned_airspace: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "assignedAirspace",
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
    extension: Iterable[AuthorityForAirspaceTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
