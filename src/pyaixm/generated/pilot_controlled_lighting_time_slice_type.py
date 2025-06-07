from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_intensity_stand_by_type import CodeIntensityStandByType
from generated.code_pilot_controlled_lighting_type import (
    CodePilotControlledLightingType,
)
from generated.ground_light_system_property_type import (
    GroundLightSystemPropertyType,
)
from generated.light_activation_property_type import (
    LightActivationPropertyType,
)
from generated.no_number_type import NoNumberType
from generated.note_property_type import NotePropertyType
from generated.pilot_controlled_lighting_time_slice_type_extension import (
    PilotControlledLightingTimeSliceTypeExtension,
)
from generated.text_instruction_type import TextInstructionType
from generated.val_duration_type import ValDurationType
from generated.val_frequency_type import ValFrequencyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLightingTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodePilotControlledLightingType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    duration: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    intensity_steps: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "intensitySteps",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    stand_by_intensity: Optional[CodeIntensityStandByType] = field(
        default=None,
        metadata={
            "name": "standByIntensity",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radio_frequency: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "name": "radioFrequency",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    activation_instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "name": "activationInstruction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    controlled_light_intensity: Iterable[LightActivationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "controlledLightIntensity",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    activated_ground_lighting: Iterable[GroundLightSystemPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "activatedGroundLighting",
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
    extension: Iterable[PilotControlledLightingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
