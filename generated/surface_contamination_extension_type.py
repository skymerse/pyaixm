from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_clearance_method_type import CodeClearanceMethodType
from generated.code_coverage_type import CodeCoverageType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceContaminationExtensionType(AbstractExtensionType):
    coverage: Optional[CodeCoverageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    clearance_method: Optional[CodeClearanceMethodType] = field(
        default=None,
        metadata={
            "name": "clearanceMethod",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cleared_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "clearedWidth",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    contaminant_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "contaminantWidth",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
