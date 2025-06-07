from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airport_heliport_usage import AirportHeliportUsage
from pyaixm.generated.apron_area_usage import ApronAreaUsage
from pyaixm.generated.manoeuvring_area_usage import ManoeuvringAreaUsage
from pyaixm.generated.service_usage import ServiceUsage

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UsageConditionPropertyType(AbstractAixmpropertyType):
    service_usage: Optional[ServiceUsage] = field(
        default=None,
        metadata={
            "name": "ServiceUsage",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    airport_heliport_usage: Optional[AirportHeliportUsage] = field(
        default=None,
        metadata={
            "name": "AirportHeliportUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_area_usage: Optional[ApronAreaUsage] = field(
        default=None,
        metadata={
            "name": "ApronAreaUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    manoeuvring_area_usage: Optional[ManoeuvringAreaUsage] = field(
        default=None,
        metadata={
            "name": "ManoeuvringAreaUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
