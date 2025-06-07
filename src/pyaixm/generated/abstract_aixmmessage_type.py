from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmmessage_base_type import (
    AbstractAixmmessageBaseType,
)
from pyaixm.generated.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmmessageType(AbstractAixmmessageBaseType):
    class Meta:
        name = "AbstractAIXMMessageType"

    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
