from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.authority_for_special_navigation_station_property_type import (
    AuthorityForSpecialNavigationStationPropertyType,
)
from pyaixm.generated.code_radio_emission_type import CodeRadioEmissionType
from pyaixm.generated.code_special_navigation_station_type import (
    CodeSpecialNavigationStationType,
)
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.special_navigation_station_status_property_type import (
    SpecialNavigationStationStatusPropertyType,
)
from pyaixm.generated.special_navigation_station_time_slice_type_extension import (
    SpecialNavigationStationTimeSliceTypeExtension,
)
from pyaixm.generated.special_navigation_system_property_type import (
    SpecialNavigationSystemPropertyType,
)
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_frequency_type import ValFrequencyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeSpecialNavigationStationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    frequency: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    emission: Optional[CodeRadioEmissionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    system_chain: Optional[SpecialNavigationSystemPropertyType] = field(
        default=None,
        metadata={
            "name": "systemChain",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    responsible_organisation: Optional[
        AuthorityForSpecialNavigationStationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "responsibleOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    position: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[SpecialNavigationStationStatusPropertyType] = field(
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
    extension: Iterable[SpecialNavigationStationTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
