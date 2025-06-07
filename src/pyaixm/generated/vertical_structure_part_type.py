from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from pyaixm.generated.code_colour_type import CodeColourType
from pyaixm.generated.code_status_construction_type import (
    CodeStatusConstructionType,
)
from pyaixm.generated.code_vertical_structure_marking_type import (
    CodeVerticalStructureMarkingType,
)
from pyaixm.generated.code_vertical_structure_material_type import (
    CodeVerticalStructureMaterialType,
)
from pyaixm.generated.code_vertical_structure_type import (
    CodeVerticalStructureType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.elevated_curve_property_type import (
    ElevatedCurvePropertyType,
)
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.light_element_property_type import (
    LightElementPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.timesheet_property_type import TimesheetPropertyType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.vertical_structure_part_type_extension import (
    VerticalStructurePartTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructurePartType(AbstractPropertiesWithScheduleType):
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
    vertical_extent: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "verticalExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_extent_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "verticalExtentAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeVerticalStructureType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    construction_status: Optional[CodeStatusConstructionType] = field(
        default=None,
        metadata={
            "name": "constructionStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marking_pattern: Optional[CodeVerticalStructureMarkingType] = field(
        default=None,
        metadata={
            "name": "markingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marking_first_colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
            "name": "markingFirstColour",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marking_second_colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
            "name": "markingSecondColour",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    mobile: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    frangible: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    visible_material: Optional[CodeVerticalStructureMaterialType] = field(
        default=None,
        metadata={
            "name": "visibleMaterial",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    horizontal_projection_location: Optional[ElevatedPointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "horizontalProjection_location",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    horizontal_projection_linear_extent: Optional[
        ElevatedCurvePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "horizontalProjection_linearExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    horizontal_projection_surface_extent: Optional[
        ElevatedSurfacePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "horizontalProjection_surfaceExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lighting: Iterable[LightElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[VerticalStructurePartTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
