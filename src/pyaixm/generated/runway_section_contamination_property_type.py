from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.runway_section_contamination import (
    RunwaySectionContamination,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwaySectionContaminationPropertyType(AbstractAixmpropertyType):
    runway_section_contamination: Optional[RunwaySectionContamination] = field(
        default=None,
        metadata={
            "name": "RunwaySectionContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
