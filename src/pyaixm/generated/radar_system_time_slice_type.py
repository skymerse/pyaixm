from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_radar_service_type import CodeRadarServiceType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.radar_component_property_type import (
    RadarComponentPropertyType,
)
from pyaixm.generated.radar_system_time_slice_type_extension import (
    RadarSystemTimeSliceTypeExtension,
)
from pyaixm.generated.runway_property_type import RunwayPropertyType
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarSystemTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeRadarServiceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    model: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    general_terrain_monitor: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "generalTerrainMonitor",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    broadcast_identifier: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "broadcastIdentifier",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radar_equipment: Iterable[RadarComponentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "radarEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    office: Iterable[OrganisationAuthorityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    airport_heliport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "airportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    parrunway: Iterable[RunwayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PARRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
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
    extension: Iterable[RadarSystemTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
