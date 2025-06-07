from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_base_type import (
    AbstractAixmtimeSliceBaseType,
)
from pyaixm.generated.correction_number import CorrectionNumber
from pyaixm.generated.feature_lifetime import FeatureLifetime
from pyaixm.generated.feature_time_slice_metadata_property_type import (
    FeatureTimeSliceMetadataPropertyType,
)
from pyaixm.generated.interpretation import Interpretation
from pyaixm.generated.sequence_number import SequenceNumber

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmtimeSliceType(AbstractAixmtimeSliceBaseType):
    """
    Adds in the AIXM specific properties, such as 'interpretation'.
    """

    class Meta:
        name = "AbstractAIXMTimeSliceType"

    interpretation: Optional[Interpretation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    sequence_number: Optional[SequenceNumber] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    correction_number: Optional[CorrectionNumber] = field(
        default=None,
        metadata={
            "name": "correctionNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    time_slice_metadata: Optional[FeatureTimeSliceMetadataPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "timeSliceMetadata",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    feature_lifetime: Optional[FeatureLifetime] = field(
        default=None,
        metadata={
            "name": "featureLifetime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
