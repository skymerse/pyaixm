from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.uom_light_intensity_type_value import (
    UomLightIntensityTypeValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ValLightIntensityType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    uom: Optional[Union[str, UomLightIntensityTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
