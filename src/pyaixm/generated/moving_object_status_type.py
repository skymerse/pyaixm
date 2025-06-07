from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_time_slice_type import AbstractTimeSliceType
from generated.direction_property_type import DirectionPropertyType
from generated.geometry_array_property_type import GeometryPropertyType
from generated.location import Location
from generated.location_name import LocationName
from generated.location_reference import LocationReference
from generated.measure_type import MeasureType
from generated.pos import Pos
from generated.priority_location import PriorityLocation
from generated.status import Status
from generated.status_reference import StatusReference

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    position: Optional[GeometryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location_name: Optional[LocationName] = field(
        default=None,
        metadata={
            "name": "locationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    speed: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bearing: Optional[DirectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    acceleration: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevation: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    status_reference: Optional[StatusReference] = field(
        default=None,
        metadata={
            "name": "statusReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
