from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.actuate_type import ActuateType
from pyaixm.generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from pyaixm.generated.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from pyaixm.generated.date_time_property_type import DateTimePropertyType
from pyaixm.generated.ex_extent_property_type import ExExtentPropertyType
from pyaixm.generated.md_identifier_type import CiCitationPropertyType
from pyaixm.generated.md_reference_system_property_type import (
    MdReferenceSystemPropertyType,
)
from pyaixm.generated.md_representative_fraction_property_type import (
    MdRepresentativeFractionPropertyType,
)
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.show_type import ShowType
from pyaixm.generated.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiProcessStepType(AbstractObjectType):
    class Meta:
        name = "LI_ProcessStep_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    rationale: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    processor: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: Iterable["LiSourcePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class LiProcessStep(LiProcessStepType):
    class Meta:
        name = "LI_ProcessStep"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiProcessStepPropertyType:
    class Meta:
        name = "LI_ProcessStep_PropertyType"

    li_process_step: Optional[LiProcessStep] = field(
        default=None,
        metadata={
            "name": "LI_ProcessStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class LiSourceType(AbstractObjectType):
    class Meta:
        name = "LI_Source_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    scale_denominator: Optional[MdRepresentativeFractionPropertyType] = field(
        default=None,
        metadata={
            "name": "scaleDenominator",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_reference_system: Optional[MdReferenceSystemPropertyType] = field(
        default=None,
        metadata={
            "name": "sourceReferenceSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_citation: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "sourceCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_extent: Iterable[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_step: Iterable[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class LiSource(LiSourceType):
    class Meta:
        name = "LI_Source"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiSourcePropertyType:
    class Meta:
        name = "LI_Source_PropertyType"

    li_source: Optional[LiSource] = field(
        default=None,
        metadata={
            "name": "LI_Source",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
