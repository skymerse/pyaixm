from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.runway_contamination_property_type import (
    RunwayContaminationPropertyType,
)
from pyaixm.generated.runway_section_contamination_property_type import (
    RunwaySectionContaminationPropertyType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayDirectionExtensionType2(AbstractExtensionType):
    class Meta:
        name = "RunwayDirectionExtensionType"

    area_contaminant: Iterable[RunwaySectionContaminationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "areaContaminant",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    overall_contaminant: Iterable[RunwayContaminationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "overallContaminant",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
