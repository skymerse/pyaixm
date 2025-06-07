from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_apron_section_type import CodeApronSectionType
from generated.code_cardinal_direction_type import CodeCardinalDirectionType
from generated.code_crack_type import CodeCrackType
from generated.code_frost_heave_type import CodeFrostHeaveType
from generated.code_runway_section_type import CodeRunwaySectionType
from generated.code_taxiway_section_type import CodeTaxiwaySectionType
from generated.code_yes_no_type import CodeYesNoType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceCharacteristicsExtensionType(AbstractExtensionType):
    numerous_defects: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "numerousDefects",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    crack_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "crackWidth",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    crack_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "crackDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    crack_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "crackLength",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    soft_edges: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "softEdges",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    crack_type: Optional[CodeCrackType] = field(
        default=None,
        metadata={
            "name": "crackType",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    affected_distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "affectedDistance",
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
    frost_heave: Optional[CodeFrostHeaveType] = field(
        default=None,
        metadata={
            "name": "frostHeave",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    soft: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    irregular_surface: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "irregularSurface",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    runway_warning_section: Optional[CodeRunwaySectionType] = field(
        default=None,
        metadata={
            "name": "runwayWarningSection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    apron_warning_section: Optional[CodeApronSectionType] = field(
        default=None,
        metadata={
            "name": "apronWarningSection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    taxiway_warning_section: Optional[CodeTaxiwaySectionType] = field(
        default=None,
        metadata={
            "name": "taxiwayWarningSection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
