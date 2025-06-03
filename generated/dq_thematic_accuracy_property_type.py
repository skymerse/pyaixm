from dataclasses import dataclass, field
from typing import Optional, Union

from generated.actuate_type import ActuateType
from generated.dq_non_quantitative_attribute_accuracy import (
    DqNonQuantitativeAttributeAccuracy,
)
from generated.dq_quantitative_attribute_accuracy import (
    DqQuantitativeAttributeAccuracy,
)
from generated.dq_thematic_classification_correctness import (
    DqThematicClassificationCorrectness,
)
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.show_type import ShowType
from generated.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqThematicAccuracyPropertyType:
    class Meta:
        name = "DQ_ThematicAccuracy_PropertyType"

    dq_thematic_classification_correctness: Optional[
        DqThematicClassificationCorrectness
    ] = field(
        default=None,
        metadata={
            "name": "DQ_ThematicClassificationCorrectness",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_non_quantitative_attribute_accuracy: Optional[
        DqNonQuantitativeAttributeAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_NonQuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_quantitative_attribute_accuracy: Optional[
        DqQuantitativeAttributeAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_QuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
