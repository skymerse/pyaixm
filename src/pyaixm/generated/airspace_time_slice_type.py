from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airspace_activation_property_type import (
    AirspaceActivationPropertyType,
)
from pyaixm.generated.airspace_geometry_component_property_type import (
    AirspaceGeometryComponentPropertyType,
)
from pyaixm.generated.airspace_layer_class_property_type import (
    AirspaceLayerClassPropertyType,
)
from pyaixm.generated.airspace_time_slice_type_extension import (
    AirspaceTimeSliceTypeExtension,
)
from pyaixm.generated.code_airspace_designator_type import (
    CodeAirspaceDesignatorType,
)
from pyaixm.generated.code_airspace_type import CodeAirspaceType
from pyaixm.generated.code_military_operations_type import (
    CodeMilitaryOperationsType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.route_property_type import RoutePropertyType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_fltype import ValFltype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeAirspaceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[CodeAirspaceDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    local_type: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "localType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_icao: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "designatorICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    control_type: Optional[CodeMilitaryOperationsType] = field(
        default=None,
        metadata={
            "name": "controlType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_lower_separation: Optional[ValFltype] = field(
        default=None,
        metadata={
            "name": "upperLowerSeparation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    class_value: Iterable[AirspaceLayerClassPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    protected_route: Optional[RoutePropertyType] = field(
        default=None,
        metadata={
            "name": "protectedRoute",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    geometry_component: Iterable[AirspaceGeometryComponentPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "geometryComponent",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    activation: Iterable[AirspaceActivationPropertyType] = field(
        default_factory=list,
        metadata={
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
    extension: Iterable[AirspaceTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
