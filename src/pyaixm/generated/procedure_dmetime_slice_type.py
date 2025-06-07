from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.dmeproperty_type import DmepropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.procedure_dmetime_slice_type_extension import (
    ProcedureDmetimeSliceTypeExtension,
)
from pyaixm.generated.segment_leg_property_type import SegmentLegPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureDmetimeSliceType(AbstractAixmtimeSliceType):
    class Meta:
        name = "ProcedureDMETimeSliceType"

    critical_dme: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "criticalDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    satisfactory: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    dme: Optional[DmepropertyType] = field(
        default=None,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    segment_leg: Optional[SegmentLegPropertyType] = field(
        default=None,
        metadata={
            "name": "segmentLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ProcedureDmetimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
