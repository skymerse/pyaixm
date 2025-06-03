from dataclasses import dataclass, field
from typing import Optional, Union

from generated.actuate_type import ActuateType
from generated.dq_absolute_external_positional_accuracy import (
    DqAbsoluteExternalPositionalAccuracy,
)
from generated.dq_gridded_data_positional_accuracy import (
    DqGriddedDataPositionalAccuracy,
)
from generated.dq_relative_internal_positional_accuracy import (
    DqRelativeInternalPositionalAccuracy,
)
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.show_type import ShowType
from generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateOperationAccuracy:
    """Gml:coordinateOperationAccuracy is an association role to a
    DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or
    containing the definition of that positional accuracy.

    That object contains an estimate of the impact of this coordinate
    operation on point accuracy. That is, it gives position error
    estimates for the target coordinates of this coordinate operation,
    assuming no errors in the source coordinates.
    """

    class Meta:
        name = "coordinateOperationAccuracy"
        namespace = "http://www.opengis.net/gml/3.2"

    dq_absolute_external_positional_accuracy: Optional[
        DqAbsoluteExternalPositionalAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_AbsoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_gridded_data_positional_accuracy: Optional[
        DqGriddedDataPositionalAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_GriddedDataPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_relative_internal_positional_accuracy: Optional[
        DqRelativeInternalPositionalAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_RelativeInternalPositionalAccuracy",
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
