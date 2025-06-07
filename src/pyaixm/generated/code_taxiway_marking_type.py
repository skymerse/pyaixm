from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.code_taxiway_marking_base_type import (
    CodeTaxiwayMarkingBaseType,
)
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class CodeTaxiwayMarkingType:
    value: Optional[CodeTaxiwayMarkingBaseType] = field(
        default=None,
        metadata={
            "required": True,
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
