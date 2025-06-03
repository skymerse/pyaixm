from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_yes_no_type import CodeYesNoType
from generated.dmeproperty_type import DmepropertyType
from generated.note_property_type import NotePropertyType
from generated.route_dmetime_slice_type_extension import (
    RouteDmetimeSliceTypeExtension,
)
from generated.route_portion_property_type import RoutePortionPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteDmetimeSliceType(AbstractAixmtimeSliceType):
    class Meta:
        name = "RouteDMETimeSliceType"

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
    referenced_dme: Optional[DmepropertyType] = field(
        default=None,
        metadata={
            "name": "referencedDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    applicable_route_portion: Optional[RoutePortionPropertyType] = field(
        default=None,
        metadata={
            "name": "applicableRoutePortion",
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
    extension: Iterable[RouteDmetimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
