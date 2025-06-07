from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.fasdata_block import FasdataBlock

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FasdataBlockPropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "FASDataBlockPropertyType"

    fasdata_block: Optional[FasdataBlock] = field(
        default=None,
        metadata={
            "name": "FASDataBlock",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
