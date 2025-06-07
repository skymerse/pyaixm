from dataclasses import dataclass, field
from typing import Optional, Union

from generated.character_string import CharacterString
from generated.ci_date_type_code import CiDateTypeCode
from generated.ci_on_line_function_code import CiOnLineFunctionCode
from generated.ci_presentation_form_code import CiPresentationFormCode
from generated.ci_role_code import CiRoleCode
from generated.country import Country
from generated.dq_evaluation_method_type_code import DqEvaluationMethodTypeCode
from generated.ds_association_type_code import DsAssociationTypeCode
from generated.ds_initiative_type_code import DsInitiativeTypeCode
from generated.language_code import LanguageCode
from generated.localised_character_string import LocalisedCharacterString
from generated.md_cell_geometry_code import MdCellGeometryCode
from generated.md_character_set_code import MdCharacterSetCode
from generated.md_classification_code import MdClassificationCode
from generated.md_coverage_content_type_code import MdCoverageContentTypeCode
from generated.md_datatype_code import MdDatatypeCode
from generated.md_dimension_name_type_code import MdDimensionNameTypeCode
from generated.md_distribution_units import MdDistributionUnits
from generated.md_geometric_object_type_code import MdGeometricObjectTypeCode
from generated.md_imaging_condition_code import MdImagingConditionCode
from generated.md_keyword_type_code import MdKeywordTypeCode
from generated.md_maintenance_frequency_code import MdMaintenanceFrequencyCode
from generated.md_medium_format_code import MdMediumFormatCode
from generated.md_medium_name_code import MdMediumNameCode
from generated.md_obligation_code import MdObligationCode
from generated.md_pixel_orientation_code import MdPixelOrientationCode
from generated.md_progress_code import MdProgressCode
from generated.md_restriction_code import MdRestrictionCode
from generated.md_scope_code import MdScopeCode
from generated.md_spatial_representation_type_code import (
    MdSpatialRepresentationTypeCode,
)
from generated.md_topic_category_code import MdTopicCategoryCode
from generated.md_topology_level_code import MdTopologyLevelCode
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class CharacterStringPropertyType:
    class Meta:
        name = "CharacterString_PropertyType"

    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    localised_character_string: Optional[LocalisedCharacterString] = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_evaluation_method_type_code: Optional[DqEvaluationMethodTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "DQ_EvaluationMethodTypeCode",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
            },
        )
    )
    ds_initiative_type_code: Optional[DsInitiativeTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_InitiativeTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_association_type_code: Optional[DsAssociationTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_keyword_type_code: Optional[MdKeywordTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_progress_code: Optional[MdProgressCode] = field(
        default=None,
        metadata={
            "name": "MD_ProgressCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_spatial_representation_type_code: Optional[
        MdSpatialRepresentationTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_character_set_code: Optional[MdCharacterSetCode] = field(
        default=None,
        metadata={
            "name": "MD_CharacterSetCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_topic_category_code: Optional[MdTopicCategoryCode] = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_scope_code: Optional[MdScopeCode] = field(
        default=None,
        metadata={
            "name": "MD_ScopeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_maintenance_frequency_code: Optional[MdMaintenanceFrequencyCode] = (
        field(
            default=None,
            metadata={
                "name": "MD_MaintenanceFrequencyCode",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
            },
        )
    )
    md_medium_name_code: Optional[MdMediumNameCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumNameCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_medium_format_code: Optional[MdMediumFormatCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumFormatCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_distribution_units: Optional[MdDistributionUnits] = field(
        default=None,
        metadata={
            "name": "MD_DistributionUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_restriction_code: Optional[MdRestrictionCode] = field(
        default=None,
        metadata={
            "name": "MD_RestrictionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_classification_code: Optional[MdClassificationCode] = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_imaging_condition_code: Optional[MdImagingConditionCode] = field(
        default=None,
        metadata={
            "name": "MD_ImagingConditionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_coverage_content_type_code: Optional[MdCoverageContentTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_CoverageContentTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_datatype_code: Optional[MdDatatypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DatatypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_obligation_code: Optional[MdObligationCode] = field(
        default=None,
        metadata={
            "name": "MD_ObligationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_dimension_name_type_code: Optional[MdDimensionNameTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DimensionNameTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_cell_geometry_code: Optional[MdCellGeometryCode] = field(
        default=None,
        metadata={
            "name": "MD_CellGeometryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_geometric_object_type_code: Optional[MdGeometricObjectTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_GeometricObjectTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_topology_level_code: Optional[MdTopologyLevelCode] = field(
        default=None,
        metadata={
            "name": "MD_TopologyLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_pixel_orientation_code: Optional[MdPixelOrientationCode] = field(
        default=None,
        metadata={
            "name": "MD_PixelOrientationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_date_type_code: Optional[CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_on_line_function_code: Optional[CiOnLineFunctionCode] = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_presentation_form_code: Optional[CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_role_code: Optional[CiRoleCode] = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    character_string: Optional[CharacterString] = field(
        default=None,
        metadata={
            "name": "CharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
