from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from generated.code_logical_operator_type import CodeLogicalOperatorType
from generated.condition_combination_type_extension import (
    ConditionCombinationTypeExtension,
)
from generated.flight_characteristic_property_type import (
    FlightCharacteristicPropertyType,
)
from generated.meteorology_property_type import MeteorologyPropertyType
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from generated.timesheet_property_type import TimesheetPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ConditionCombinationPropertyType(AbstractAixmpropertyType):
    condition_combination: Optional["ConditionCombination"] = field(
        default=None,
        metadata={
            "name": "ConditionCombination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )


@dataclass
class ConditionCombinationType(AbstractPropertiesWithScheduleType):
    time_interval: Iterable[TimesheetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeInterval",
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
    special_date_authority: Iterable[OrganisationAuthorityPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "specialDateAuthority",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    logical_operator: Optional[CodeLogicalOperatorType] = field(
        default=None,
        metadata={
            "name": "logicalOperator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    weather: Iterable[MeteorologyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft: Iterable[AircraftCharacteristicPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight: Iterable[FlightCharacteristicPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sub_condition: Iterable[ConditionCombinationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "subCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ConditionCombinationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )


@dataclass
class ConditionCombination(ConditionCombinationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
