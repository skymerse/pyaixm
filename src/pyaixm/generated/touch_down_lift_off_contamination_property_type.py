from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.touch_down_lift_off_contamination import (
    TouchDownLiftOffContamination,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffContaminationPropertyType(AbstractAixmpropertyType):
    touch_down_lift_off_contamination: Optional[
        TouchDownLiftOffContamination
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
