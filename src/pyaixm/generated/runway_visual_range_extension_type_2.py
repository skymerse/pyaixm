from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_status_operations_type import (
    CodeStatusOperationsType,
)
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayVisualRangeExtensionType2(AbstractExtensionType):
    class Meta:
        name = "RunwayVisualRangeExtensionType"

    operational_status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
