from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.curve_property_type_1 import ElevatedCurve

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedCurvePropertyType(AbstractAixmpropertyType):
    elevated_curve: Optional[ElevatedCurve] = field(
        default=None,
        metadata={
            "name": "ElevatedCurve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
