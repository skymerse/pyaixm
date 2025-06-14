from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)
from pyaixm.generated.md_identifier_type import MdIdentifierPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicDescriptionType(AbstractExGeographicExtentType):
    class Meta:
        name = "EX_GeographicDescription_Type"

    geographic_identifier: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "geographicIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
