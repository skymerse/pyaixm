from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.actuate_type import ActuateType
from pyaixm.generated.code_type import CodeType
from pyaixm.generated.compass_point_enumeration import CompassPointEnumeration
from pyaixm.generated.direction_description_type import (
    DirectionDescriptionType,
)
from pyaixm.generated.direction_vector_type import DirectionVectorType
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.show_type import ShowType
from pyaixm.generated.string_or_ref_type import StringOrRefType
from pyaixm.generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectionPropertyType:
    direction_vector: Optional[DirectionVectorType] = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_description: Optional[DirectionDescriptionType] = field(
        default=None,
        metadata={
            "name": "DirectionDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compass_point: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "name": "CompassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_keyword: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DirectionKeyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_string: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "DirectionString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
