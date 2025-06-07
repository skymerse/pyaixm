from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_ridge_type import CodeRidgeType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RidgeExtensionType(AbstractExtensionType):
    ridge_type: Optional[CodeRidgeType] = field(
        default=None,
        metadata={
            "name": "ridgeType",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
