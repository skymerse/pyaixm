from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_runway_marking_type import CodeRunwayMarkingType
from pyaixm.generated.code_status_operations_type import (
    CodeStatusOperationsType,
)
from pyaixm.generated.text_designator_type import TextDesignatorType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayMarkingExtensionType2(AbstractExtensionType):
    class Meta:
        name = "RunwayMarkingExtensionType"

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
    operational_status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    runway_marking_type: Optional[CodeRunwayMarkingType] = field(
        default=None,
        metadata={
            "name": "runwayMarkingType",
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
