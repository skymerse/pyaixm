from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.authority_for_special_navigation_system_property_type import (
    AuthorityForSpecialNavigationSystemPropertyType,
)
from pyaixm.generated.code_special_navigation_chain_designator_type import (
    CodeSpecialNavigationChainDesignatorType,
)
from pyaixm.generated.code_special_navigation_system_type import (
    CodeSpecialNavigationSystemType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.special_navigation_system_time_slice_type_extension import (
    SpecialNavigationSystemTimeSliceTypeExtension,
)
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationSystemTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeSpecialNavigationSystemType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[CodeSpecialNavigationChainDesignatorType] = field(
        default=None,
        metadata={
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
    responsible_organisation: Optional[
        AuthorityForSpecialNavigationSystemPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "responsibleOrganisation",
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
    extension: Iterable[SpecialNavigationSystemTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
