from dataclasses import dataclass, field

from pyaixm.generated.arc_string_type import ArcStringType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcType1(ArcStringType):
    class Meta:
        name = "ArcType"

    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
