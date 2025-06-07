from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RingPropertyType:
    """
    A property with the content model of gml:RingPropertyType encapsulates a ring
    to represent a component of a surface boundary.
    """

    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
