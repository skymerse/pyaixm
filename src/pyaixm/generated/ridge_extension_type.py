from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_ridge_type import CodeRidgeType

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
