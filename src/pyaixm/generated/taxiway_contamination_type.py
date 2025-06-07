from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_surface_contamination_type import (
    AbstractSurfaceContaminationType,
)
from generated.code_friction_device_type import CodeFrictionDeviceType
from generated.code_friction_estimate_type import CodeFrictionEstimateType
from generated.code_yes_no_type import CodeYesNoType
from generated.date_time_type import DateTimeType
from generated.note_property_type import NotePropertyType
from generated.ridge_property_type import RidgePropertyType
from generated.surface_contamination_layer_property_type import (
    SurfaceContaminationLayerPropertyType,
)
from generated.taxiway_contamination_type_extension import (
    TaxiwayContaminationTypeExtension,
)
from generated.time_type_2 import TimeType2
from generated.val_depth_type import ValDepthType
from generated.val_distance_type import ValDistanceType
from generated.val_friction_type import ValFrictionType
from generated.val_percent_type import ValPercentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayContaminationType(AbstractSurfaceContaminationType):
    observation_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "observationTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    depth: Optional[ValDepthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    friction_coefficient: Optional[ValFrictionType] = field(
        default=None,
        metadata={
            "name": "frictionCoefficient",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    friction_estimation: Optional[CodeFrictionEstimateType] = field(
        default=None,
        metadata={
            "name": "frictionEstimation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    friction_device: Optional[CodeFrictionDeviceType] = field(
        default=None,
        metadata={
            "name": "frictionDevice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obscured_lights: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "obscuredLights",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    further_clearance_time: Optional[TimeType2] = field(
        default=None,
        metadata={
            "name": "furtherClearanceTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    further_total_clearance: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "furtherTotalClearance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    next_observation_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "nextObservationTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    proportion: Optional[ValPercentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    critical_ridge: Iterable[RidgePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "criticalRidge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    layer: Iterable[SurfaceContaminationLayerPropertyType] = field(
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
    cleared_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "clearedWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TaxiwayContaminationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
