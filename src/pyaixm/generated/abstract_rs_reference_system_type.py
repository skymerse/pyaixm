from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.ex_extent_property_type import ExExtentPropertyType
from pyaixm.generated.rs_identifier_property_type import (
    RsIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractRsReferenceSystemType(AbstractObjectType):
    """
    Description of the spatial and temporal reference systems used in the dataset.
    """

    class Meta:
        name = "AbstractRS_ReferenceSystem_Type"

    name: Optional[RsIdentifierPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    domain_of_validity: Iterable[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
