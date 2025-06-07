from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airport_heliport_responsibility_organisation import (
    AirportHeliportResponsibilityOrganisation,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportResponsibilityOrganisationPropertyType(
    AbstractAixmpropertyType
):
    airport_heliport_responsibility_organisation: Optional[
        AirportHeliportResponsibilityOrganisation
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportResponsibilityOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
