from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.curve_property_type_1 import (
    Curve2,
    ElevatedCurve,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CurvePropertyType2(AbstractAixmpropertyType):
    class Meta:
        name = "CurvePropertyType"

    elevated_curve: Optional[ElevatedCurve] = field(
        default=None,
        metadata={
            "name": "ElevatedCurve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
