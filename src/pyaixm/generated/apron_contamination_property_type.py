from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.apron_contamination import ApronContamination

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronContaminationPropertyType(AbstractAixmpropertyType):
    apron_contamination: Optional[ApronContamination] = field(
        default=None,
        metadata={
            "name": "ApronContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
