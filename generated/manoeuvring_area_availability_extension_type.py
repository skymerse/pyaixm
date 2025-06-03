from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_apron_section_type import CodeApronSectionType
from generated.code_barrier_type import CodeBarrierType
from generated.code_cardinal_direction_type import CodeCardinalDirectionType
from generated.code_yes_no_type import CodeYesNoType
from generated.text_designator_type import TextDesignatorType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ManoeuvringAreaAvailabilityExtensionType(AbstractExtensionType):
    warning_adjacent: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "warningAdjacent",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_section: Optional[CodeApronSectionType] = field(
        default=None,
        metadata={
            "name": "warningSection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_barrier: Optional[CodeBarrierType] = field(
        default=None,
        metadata={
            "name": "warningBarrier",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    at_runway: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "atRunway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    at_taxiway: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "atTaxiway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "warningLength",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "warningDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
