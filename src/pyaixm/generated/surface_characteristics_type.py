from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_pcnmethod_type import CodePcnmethodType
from pyaixm.generated.code_pcnpavement_type import CodePcnpavementType
from pyaixm.generated.code_pcnsubgrade_type import CodePcnsubgradeType
from pyaixm.generated.code_pcntyre_pressure_type import CodePcntyrePressureType
from pyaixm.generated.code_surface_composition_type import (
    CodeSurfaceCompositionType,
)
from pyaixm.generated.code_surface_condition_type import (
    CodeSurfaceConditionType,
)
from pyaixm.generated.code_surface_preparation_type import (
    CodeSurfacePreparationType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_type_extension import (
    SurfaceCharacteristicsTypeExtension,
)
from pyaixm.generated.val_lcntype import ValLcntype
from pyaixm.generated.val_pcntype import ValPcntype
from pyaixm.generated.val_pressure_type import ValPressureType
from pyaixm.generated.val_weight_type import ValWeightType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceCharacteristicsType(AbstractAixmobjectType):
    composition: Optional[CodeSurfaceCompositionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    preparation: Optional[CodeSurfacePreparationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_condition: Optional[CodeSurfaceConditionType] = field(
        default=None,
        metadata={
            "name": "surfaceCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    class_pcn: Optional[ValPcntype] = field(
        default=None,
        metadata={
            "name": "classPCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    pavement_type_pcn: Optional[CodePcnpavementType] = field(
        default=None,
        metadata={
            "name": "pavementTypePCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    pavement_subgrade_pcn: Optional[CodePcnsubgradeType] = field(
        default=None,
        metadata={
            "name": "pavementSubgradePCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    max_tyre_pressure_pcn: Optional[CodePcntyrePressureType] = field(
        default=None,
        metadata={
            "name": "maxTyrePressurePCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    evaluation_method_pcn: Optional[CodePcnmethodType] = field(
        default=None,
        metadata={
            "name": "evaluationMethodPCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    class_lcn: Optional[ValLcntype] = field(
        default=None,
        metadata={
            "name": "classLCN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    weight_siwl: Optional[ValWeightType] = field(
        default=None,
        metadata={
            "name": "weightSIWL",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    tyre_pressure_siwl: Optional[ValPressureType] = field(
        default=None,
        metadata={
            "name": "tyrePressureSIWL",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    weight_auw: Optional[ValWeightType] = field(
        default=None,
        metadata={
            "name": "weightAUW",
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
    extension: Iterable[SurfaceCharacteristicsTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
