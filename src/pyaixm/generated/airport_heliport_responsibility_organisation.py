from dataclasses import dataclass

from pyaixm.generated.airport_heliport_responsibility_organisation_type import (
    AirportHeliportResponsibilityOrganisationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportResponsibilityOrganisation(
    AirportHeliportResponsibilityOrganisationType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
