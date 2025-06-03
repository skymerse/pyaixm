from dataclasses import dataclass, field
from typing import Optional, Union

from generated.actuate_type import ActuateType
from generated.affine_cs_1 import AffineCs1
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.show_type import ShowType
from generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AffineCspropertyType:
    """
    Gml:AffineCSPropertyType is a property type for association roles to an affine
    coordinate system, either referencing or containing the definition of that
    coordinate system.
    """

    class Meta:
        name = "AffineCSPropertyType"

    affine_cs: Optional[AffineCs1] = field(
        default=None,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
