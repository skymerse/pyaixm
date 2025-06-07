from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.taxiway_contamination import TaxiwayContamination

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayContaminationPropertyType(AbstractAixmpropertyType):
    taxiway_contamination: Optional[TaxiwayContamination] = field(
        default=None,
        metadata={
            "name": "TaxiwayContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
