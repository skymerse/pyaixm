from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.code_standby_power_base_type_value import (
    CodeStandbyPowerBaseTypeValue,
)
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeStandbyPowerType:
    value: Union[str, CodeStandbyPowerBaseTypeValue] = field(
        default="",
        metadata={
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
