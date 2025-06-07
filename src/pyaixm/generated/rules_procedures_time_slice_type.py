from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airspace_property_type import AirspacePropertyType
from pyaixm.generated.code_rule_procedure_title_type import (
    CodeRuleProcedureTitleType,
)
from pyaixm.generated.code_rule_procedure_type import CodeRuleProcedureType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.rules_procedures_time_slice_type_extension import (
    RulesProceduresTimeSliceTypeExtension,
)
from pyaixm.generated.xhtmltype import Xhtmltype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RulesProceduresTimeSliceType(AbstractAixmtimeSliceType):
    category: Optional[CodeRuleProcedureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    title: Optional[CodeRuleProcedureTitleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    content: Optional[Xhtmltype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    affected_location: Iterable[AirportHeliportPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "affectedLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    affected_area: Iterable[AirspacePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "affectedArea",
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
    extension: Iterable[RulesProceduresTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
