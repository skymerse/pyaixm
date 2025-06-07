from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.runway_contamination import RunwayContamination

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayContaminationPropertyType(AbstractAixmpropertyType):
    runway_contamination: Optional[RunwayContamination] = field(
        default=None,
        metadata={
            "name": "RunwayContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
