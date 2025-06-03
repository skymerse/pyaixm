from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.ais_publication import AisPublication

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AisPublicationPropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "AIS_PublicationPropertyType"

    ais_publication: Optional[AisPublication] = field(
        default=None,
        metadata={
            "name": "AIS_Publication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "required": True,
        },
    )
