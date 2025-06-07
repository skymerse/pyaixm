from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.text_designator_type import TextDesignatorType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ProcedureExtensionType2(AbstractExtensionType):
    class Meta:
        name = "ProcedureExtensionType"

    printable_version_number: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "printableVersionNumber",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    legacy_control_number: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "legacyControlNumber",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
