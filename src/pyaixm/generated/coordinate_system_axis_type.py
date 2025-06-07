from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.axis_abbrev import AxisAbbrev
from pyaixm.generated.axis_direction import AxisDirection
from pyaixm.generated.identified_object_type import IdentifiedObjectType
from pyaixm.generated.maximum_value import MaximumValue
from pyaixm.generated.minimum_value import MinimumValue
from pyaixm.generated.range_meaning import RangeMeaning

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemAxisType(IdentifiedObjectType):
    """
    :ivar axis_abbrev:
    :ivar axis_direction:
    :ivar minimum_value:
    :ivar maximum_value:
    :ivar range_meaning:
    :ivar uom: The uom attribute provides an identifier of the unit of
        measure used for this coordinate system axis. The value of this
        coordinate in a coordinate tuple shall be recorded using this
        unit of measure, whenever those coordinates use a coordinate
        reference system that uses a coordinate system that uses this
        axis.
    """

    axis_abbrev: Optional[AxisAbbrev] = field(
        default=None,
        metadata={
            "name": "axisAbbrev",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    axis_direction: Optional[AxisDirection] = field(
        default=None,
        metadata={
            "name": "axisDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    range_meaning: Optional[RangeMeaning] = field(
        default=None,
        metadata={
            "name": "rangeMeaning",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        },
    )
