from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.apron_property_type import ApronPropertyType
from pyaixm.generated.runway_property_type import RunwayPropertyType
from pyaixm.generated.taxiway_property_type import TaxiwayPropertyType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class TaxiwayExtensionType2(AbstractExtensionType):
    class Meta:
        name = "TaxiwayExtensionType"

    intersections_intersected_by_taxiway: Iterable[TaxiwayPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "Intersections_intersectedByTaxiway",
                "type": "Element",
                "namespace": "urn:us.gov.dot.faa.aim.fns",
                "nillable": True,
            },
        )
    )
    intersections_intersected_by_runway: Iterable[RunwayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "Intersections_intersectedByRunway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    intersections_intersected_by_apron: Iterable[ApronPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "Intersections_intersectedByApron",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
