from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_feature_type import AbstractFeatureType
from generated.actuate_type import ActuateType
from generated.aerial_refuelling import AerialRefuelling
from generated.aeronautical_ground_light import AeronauticalGroundLight
from generated.air_traffic_control_service import AirTrafficControlService
from generated.air_traffic_management_service import (
    AirTrafficManagementService,
)
from generated.aircraft_ground_service import AircraftGroundService
from generated.aircraft_stand import AircraftStand
from generated.airport_clearance_service import AirportClearanceService
from generated.airport_heliport import AirportHeliport
from generated.airport_heliport_collocation import AirportHeliportCollocation
from generated.airport_hot_spot import AirportHotSpot
from generated.airport_protection_area_marking import (
    AirportProtectionAreaMarking,
)
from generated.airport_sign import AirportSign
from generated.airport_supplies_service import AirportSuppliesService
from generated.airspace import Airspace
from generated.airspace_border_crossing import AirspaceBorderCrossing
from generated.aixmbasic_message import AixmbasicMessage
from generated.altimeter_source import AltimeterSource
from generated.angle_indication import AngleIndication
from generated.approach_lighting_system import ApproachLightingSystem
from generated.apron import Apron
from generated.apron_element import ApronElement
from generated.apron_light_system import ApronLightSystem
from generated.apron_marking import ApronMarking
from generated.arresting_gear import ArrestingGear
from generated.arrival_feeder_leg import ArrivalFeederLeg
from generated.arrival_leg import ArrivalLeg
from generated.authority_for_airspace import AuthorityForAirspace
from generated.azimuth import Azimuth
from generated.change_over_point import ChangeOverPoint
from generated.checkpoint_ins import CheckpointIns
from generated.checkpoint_vor import CheckpointVor
from generated.circling_area import CirclingArea
from generated.curve_property_type_1 import (
    CompositeCurve,
    Curve1,
    Curve2,
    ElevatedCurve,
    OrientableCurve,
)
from generated.deicing_area import DeicingArea
from generated.deicing_area_marking import DeicingAreaMarking
from generated.departure_leg import DepartureLeg
from generated.designated_point import DesignatedPoint
from generated.direction import Direction
from generated.direction_finder import DirectionFinder
from generated.distance_indication import DistanceIndication
from generated.dme import Dme
from generated.dynamic_feature import DynamicFeature
from generated.dynamic_feature_collection_type import DynamicFeatureCollection
from generated.elevated_point import ElevatedPoint
from generated.elevated_surface import ElevatedSurface
from generated.elevation import Elevation
from generated.event import Event
from generated.final_leg import FinalLeg
from generated.fire_fighting_service import FireFightingService
from generated.flight_restriction import FlightRestriction
from generated.floating_dock_site import FloatingDockSite
from generated.geo_border import GeoBorder
from generated.geometric_complex import GeometricComplex
from generated.geometry_array_property_type import MultiGeometry
from generated.glidepath import Glidepath
from generated.grid import Grid
from generated.grid_coverage import GridCoverage
from generated.ground_traffic_control_service import (
    GroundTrafficControlService,
)
from generated.guidance_line import GuidanceLine
from generated.guidance_line_light_system import GuidanceLineLightSystem
from generated.guidance_line_marking import GuidanceLineMarking
from generated.holding_assessment import HoldingAssessment
from generated.holding_pattern import HoldingPattern
from generated.information_service import InformationService
from generated.initial_leg import InitialLeg
from generated.instrument_approach_procedure import InstrumentApproachProcedure
from generated.intermediate_leg import IntermediateLeg
from generated.line_string import LineString
from generated.localizer import Localizer
from generated.marker_beacon import MarkerBeacon
from generated.marking_buoy import MarkingBuoy
from generated.measure_type import MeasureType
from generated.missed_approach_leg import MissedApproachLeg
from generated.multi_curve import MultiCurve
from generated.multi_curve_coverage import MultiCurveCoverage
from generated.multi_point import MultiPoint
from generated.multi_point_coverage import MultiPointCoverage
from generated.multi_solid import MultiSolid
from generated.multi_solid_coverage import MultiSolidCoverage
from generated.multi_surface import MultiSurface
from generated.multi_surface_coverage import MultiSurfaceCoverage
from generated.navaid import Navaid
from generated.navigation_area import NavigationArea
from generated.navigation_area_restriction import NavigationAreaRestriction
from generated.ndb import Ndb
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.non_movement_area import NonMovementArea
from generated.obstacle_area import ObstacleArea
from generated.organisation_authority import OrganisationAuthority
from generated.passenger_loading_bridge import PassengerLoadingBridge
from generated.passenger_service import PassengerService
from generated.pilot_controlled_lighting import PilotControlledLighting
from generated.point_1 import Point1
from generated.point_2 import Point2
from generated.polygon import Polygon
from generated.polyhedral_surface import PolyhedralSurface
from generated.precision_approach_radar import PrecisionApproachRadar
from generated.primary_surveillance_radar import PrimarySurveillanceRadar
from generated.procedure_dme import ProcedureDme
from generated.radar_system import RadarSystem
from generated.radio_communication_channel import RadioCommunicationChannel
from generated.radio_frequency_area import RadioFrequencyArea
from generated.rectified_grid import RectifiedGrid
from generated.rectified_grid_coverage import RectifiedGridCoverage
from generated.result_of import ResultOf
from generated.road import Road
from generated.route import Route
from generated.route_dme import RouteDme
from generated.route_segment import RouteSegment
from generated.rules_procedures import RulesProcedures
from generated.runway import Runway
from generated.runway_blast_pad import RunwayBlastPad
from generated.runway_centreline_point import RunwayCentrelinePoint
from generated.runway_direction import RunwayDirection
from generated.runway_direction_light_system import RunwayDirectionLightSystem
from generated.runway_element import RunwayElement
from generated.runway_marking import RunwayMarking
from generated.runway_protect_area import RunwayProtectArea
from generated.runway_protect_area_light_system import (
    RunwayProtectAreaLightSystem,
)
from generated.runway_visual_range import RunwayVisualRange
from generated.safe_altitude_area import SafeAltitudeArea
from generated.sdf import Sdf
from generated.seaplane_landing_area import SeaplaneLandingArea
from generated.seaplane_ramp_site import SeaplaneRampSite
from generated.search_rescue_service import SearchRescueService
from generated.secondary_surveillance_radar import SecondarySurveillanceRadar
from generated.show_type import ShowType
from generated.significant_point_in_airspace import SignificantPointInAirspace
from generated.solid import Solid
from generated.solid_property_type import CompositeSolid
from generated.special_date import SpecialDate
from generated.special_navigation_station import SpecialNavigationStation
from generated.special_navigation_system import SpecialNavigationSystem
from generated.stand_marking import StandMarking
from generated.standard_instrument_arrival import StandardInstrumentArrival
from generated.standard_instrument_departure import StandardInstrumentDeparture
from generated.standard_level_column import StandardLevelColumn
from generated.standard_level_sector import StandardLevelSector
from generated.standard_level_table import StandardLevelTable
from generated.surface_1 import Surface1
from generated.surface_2 import Surface2
from generated.surface_property_type_1 import (
    CompositeSurface,
    OrientableSurface,
)
from generated.survey_control_point import SurveyControlPoint
from generated.tacan import Tacan
from generated.taxi_holding_position import TaxiHoldingPosition
from generated.taxi_holding_position_light_system import (
    TaxiHoldingPositionLightSystem,
)
from generated.taxi_holding_position_marking import TaxiHoldingPositionMarking
from generated.taxiway import Taxiway
from generated.taxiway_element import TaxiwayElement
from generated.taxiway_light_system import TaxiwayLightSystem
from generated.taxiway_marking import TaxiwayMarking
from generated.terminal_arrival_area import TerminalArrivalArea
from generated.tin import Tin
from generated.touch_down_lift_off import TouchDownLiftOff
from generated.touch_down_lift_off_light_system import (
    TouchDownLiftOffLightSystem,
)
from generated.touch_down_lift_off_marking import TouchDownLiftOffMarking
from generated.touch_down_lift_off_safe_area import TouchDownLiftOffSafeArea
from generated.triangulated_surface import TriangulatedSurface
from generated.type_type import TypeType
from generated.unit import Unit
from generated.unplanned_holding import UnplannedHolding
from generated.valid_time import ValidTime
from generated.vertical_structure import VerticalStructure
from generated.visual_glide_slope_indicator import VisualGlideSlopeIndicator
from generated.vor import Vor
from generated.wind_direction_indicator import WindDirectionIndicator
from generated.work_area import WorkArea

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class FeaturePropertyType:
    aixmbasic_message: Optional[AixmbasicMessage] = field(
        default=None,
        metadata={
            "name": "AIXMBasicMessage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/message",
        },
    )
    airport_sign: Optional[AirportSign] = field(
        default=None,
        metadata={
            "name": "AirportSign",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    wind_direction_indicator: Optional[WindDirectionIndicator] = field(
        default=None,
        metadata={
            "name": "WindDirectionIndicator",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    event: Optional[Event] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    rules_procedures: Optional[RulesProcedures] = field(
        default=None,
        metadata={
            "name": "RulesProcedures",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aerial_refuelling: Optional[AerialRefuelling] = field(
        default=None,
        metadata={
            "name": "AerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    change_over_point: Optional[ChangeOverPoint] = field(
        default=None,
        metadata={
            "name": "ChangeOverPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route: Optional[Route] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_dme: Optional[RouteDme] = field(
        default=None,
        metadata={
            "name": "RouteDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_segment: Optional[RouteSegment] = field(
        default=None,
        metadata={
            "name": "RouteSegment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_restriction: Optional[FlightRestriction] = field(
        default=None,
        metadata={
            "name": "FlightRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_border_crossing: Optional[AirspaceBorderCrossing] = field(
        default=None,
        metadata={
            "name": "AirspaceBorderCrossing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unplanned_holding: Optional[UnplannedHolding] = field(
        default=None,
        metadata={
            "name": "UnplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_pattern: Optional[HoldingPattern] = field(
        default=None,
        metadata={
            "name": "HoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    safe_altitude_area: Optional[SafeAltitudeArea] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_dme: Optional[ProcedureDme] = field(
        default=None,
        metadata={
            "name": "ProcedureDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    departure_leg: Optional[DepartureLeg] = field(
        default=None,
        metadata={
            "name": "DepartureLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_leg: Optional[ArrivalLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    missed_approach_leg: Optional[MissedApproachLeg] = field(
        default=None,
        metadata={
            "name": "MissedApproachLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    intermediate_leg: Optional[IntermediateLeg] = field(
        default=None,
        metadata={
            "name": "IntermediateLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    initial_leg: Optional[InitialLeg] = field(
        default=None,
        metadata={
            "name": "InitialLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    final_leg: Optional[FinalLeg] = field(
        default=None,
        metadata={
            "name": "FinalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_feeder_leg: Optional[ArrivalFeederLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalFeederLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_restriction: Optional[NavigationAreaRestriction] = field(
        default=None,
        metadata={
            "name": "NavigationAreaRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_arrival: Optional[StandardInstrumentArrival] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentArrival",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_departure: Optional[StandardInstrumentDeparture] = (
        field(
            default=None,
            metadata={
                "name": "StandardInstrumentDeparture",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    instrument_approach_procedure: Optional[InstrumentApproachProcedure] = (
        field(
            default=None,
            metadata={
                "name": "InstrumentApproachProcedure",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    navigation_area: Optional[NavigationArea] = field(
        default=None,
        metadata={
            "name": "NavigationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_arrival_area: Optional[TerminalArrivalArea] = field(
        default=None,
        metadata={
            "name": "TerminalArrivalArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_area: Optional[CirclingArea] = field(
        default=None,
        metadata={
            "name": "CirclingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure: Optional[VerticalStructure] = field(
        default=None,
        metadata={
            "name": "VerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    obstacle_area: Optional[ObstacleArea] = field(
        default=None,
        metadata={
            "name": "ObstacleArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    organisation_authority: Optional[OrganisationAuthority] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthority",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aeronautical_ground_light: Optional[AeronauticalGroundLight] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    significant_point_in_airspace: Optional[SignificantPointInAirspace] = (
        field(
            default=None,
            metadata={
                "name": "SignificantPointInAirspace",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    designated_point: Optional[DesignatedPoint] = field(
        default=None,
        metadata={
            "name": "DesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_system: Optional[SpecialNavigationSystem] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station: Optional[SpecialNavigationStation] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_vor: Optional[CheckpointVor] = field(
        default=None,
        metadata={
            "name": "CheckpointVOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_ins: Optional[CheckpointIns] = field(
        default=None,
        metadata={
            "name": "CheckpointINS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    direction_finder: Optional[DirectionFinder] = field(
        default=None,
        metadata={
            "name": "DirectionFinder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tacan: Optional[Tacan] = field(
        default=None,
        metadata={
            "name": "TACAN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vor: Optional[Vor] = field(
        default=None,
        metadata={
            "name": "VOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ndb: Optional[Ndb] = field(
        default=None,
        metadata={
            "name": "NDB",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    sdf: Optional[Sdf] = field(
        default=None,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marker_beacon: Optional[MarkerBeacon] = field(
        default=None,
        metadata={
            "name": "MarkerBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    localizer: Optional[Localizer] = field(
        default=None,
        metadata={
            "name": "Localizer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    glidepath: Optional[Glidepath] = field(
        default=None,
        metadata={
            "name": "Glidepath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    elevation: Optional[Elevation] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    dme: Optional[Dme] = field(
        default=None,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    azimuth: Optional[Azimuth] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid: Optional[Navaid] = field(
        default=None,
        metadata={
            "name": "Navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    distance_indication: Optional[DistanceIndication] = field(
        default=None,
        metadata={
            "name": "DistanceIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    angle_indication: Optional[AngleIndication] = field(
        default=None,
        metadata={
            "name": "AngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    pilot_controlled_lighting: Optional[PilotControlledLighting] = field(
        default=None,
        metadata={
            "name": "PilotControlledLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_channel: Optional[RadioCommunicationChannel] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_supplies_service: Optional[AirportSuppliesService] = field(
        default=None,
        metadata={
            "name": "AirportSuppliesService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_clearance_service: Optional[AirportClearanceService] = field(
        default=None,
        metadata={
            "name": "AirportClearanceService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    fire_fighting_service: Optional[FireFightingService] = field(
        default=None,
        metadata={
            "name": "FireFightingService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_ground_service: Optional[AircraftGroundService] = field(
        default=None,
        metadata={
            "name": "AircraftGroundService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_service: Optional[PassengerService] = field(
        default=None,
        metadata={
            "name": "PassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    search_rescue_service: Optional[SearchRescueService] = field(
        default=None,
        metadata={
            "name": "SearchRescueService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_management_service: Optional[AirTrafficManagementService] = (
        field(
            default=None,
            metadata={
                "name": "AirTrafficManagementService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    air_traffic_control_service: Optional[AirTrafficControlService] = field(
        default=None,
        metadata={
            "name": "AirTrafficControlService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_traffic_control_service: Optional[GroundTrafficControlService] = (
        field(
            default=None,
            metadata={
                "name": "GroundTrafficControlService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    information_service: Optional[InformationService] = field(
        default=None,
        metadata={
            "name": "InformationService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_date: Optional[SpecialDate] = field(
        default=None,
        metadata={
            "name": "SpecialDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_frequency_area: Optional[RadioFrequencyArea] = field(
        default=None,
        metadata={
            "name": "RadioFrequencyArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_column: Optional[StandardLevelColumn] = field(
        default=None,
        metadata={
            "name": "StandardLevelColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_sector: Optional[StandardLevelSector] = field(
        default=None,
        metadata={
            "name": "StandardLevelSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_table: Optional[StandardLevelTable] = field(
        default=None,
        metadata={
            "name": "StandardLevelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_assessment: Optional[HoldingAssessment] = field(
        default=None,
        metadata={
            "name": "HoldingAssessment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radar_system: Optional[RadarSystem] = field(
        default=None,
        metadata={
            "name": "RadarSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    secondary_surveillance_radar: Optional[SecondarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "SecondarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    primary_surveillance_radar: Optional[PrimarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "PrimarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    precision_approach_radar: Optional[PrecisionApproachRadar] = field(
        default=None,
        metadata={
            "name": "PrecisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    geo_border: Optional[GeoBorder] = field(
        default=None,
        metadata={
            "name": "GeoBorder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace: Optional[Airspace] = field(
        default=None,
        metadata={
            "name": "Airspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    authority_for_airspace: Optional[AuthorityForAirspace] = field(
        default=None,
        metadata={
            "name": "AuthorityForAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_hot_spot: Optional[AirportHotSpot] = field(
        default=None,
        metadata={
            "name": "AirportHotSpot",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source: Optional[AltimeterSource] = field(
        default=None,
        metadata={
            "name": "AltimeterSource",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport: Optional[AirportHeliport] = field(
        default=None,
        metadata={
            "name": "AirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_collocation: Optional[AirportHeliportCollocation] = field(
        default=None,
        metadata={
            "name": "AirportHeliportCollocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_safe_area: Optional[TouchDownLiftOffSafeArea] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffSafeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area: Optional[RunwayProtectArea] = field(
        default=None,
        metadata={
            "name": "RunwayProtectArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    non_movement_area: Optional[NonMovementArea] = field(
        default=None,
        metadata={
            "name": "NonMovementArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    survey_control_point: Optional[SurveyControlPoint] = field(
        default=None,
        metadata={
            "name": "SurveyControlPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    work_area: Optional[WorkArea] = field(
        default=None,
        metadata={
            "name": "WorkArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_ramp_site: Optional[SeaplaneRampSite] = field(
        default=None,
        metadata={
            "name": "SeaplaneRampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_landing_area: Optional[SeaplaneLandingArea] = field(
        default=None,
        metadata={
            "name": "SeaplaneLandingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marking_buoy: Optional[MarkingBuoy] = field(
        default=None,
        metadata={
            "name": "MarkingBuoy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    floating_dock_site: Optional[FloatingDockSite] = field(
        default=None,
        metadata={
            "name": "FloatingDockSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    stand_marking: Optional[StandMarking] = field(
        default=None,
        metadata={
            "name": "StandMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_marking: Optional[TaxiHoldingPositionMarking] = (
        field(
            default=None,
            metadata={
                "name": "TaxiHoldingPositionMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    deicing_area_marking: Optional[DeicingAreaMarking] = field(
        default=None,
        metadata={
            "name": "DeicingAreaMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_marking: Optional[GuidanceLineMarking] = field(
        default=None,
        metadata={
            "name": "GuidanceLineMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_marking: Optional[RunwayMarking] = field(
        default=None,
        metadata={
            "name": "RunwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_marking: Optional[TouchDownLiftOffMarking] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_protection_area_marking: Optional[AirportProtectionAreaMarking] = (
        field(
            default=None,
            metadata={
                "name": "AirportProtectionAreaMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    apron_marking: Optional[ApronMarking] = field(
        default=None,
        metadata={
            "name": "ApronMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_marking: Optional[TaxiwayMarking] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    approach_lighting_system: Optional[ApproachLightingSystem] = field(
        default=None,
        metadata={
            "name": "ApproachLightingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_light_system: Optional[
        TaxiHoldingPositionLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area_light_system: Optional[
        RunwayProtectAreaLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "RunwayProtectAreaLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_light_system: Optional[GuidanceLineLightSystem] = field(
        default=None,
        metadata={
            "name": "GuidanceLineLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_light_system: Optional[TouchDownLiftOffLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "TouchDownLiftOffLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    runway_direction_light_system: Optional[RunwayDirectionLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "RunwayDirectionLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    taxiway_light_system: Optional[TaxiwayLightSystem] = field(
        default=None,
        metadata={
            "name": "TaxiwayLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_light_system: Optional[ApronLightSystem] = field(
        default=None,
        metadata={
            "name": "ApronLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    visual_glide_slope_indicator: Optional[VisualGlideSlopeIndicator] = field(
        default=None,
        metadata={
            "name": "VisualGlideSlopeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off: Optional[TouchDownLiftOff] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_loading_bridge: Optional[PassengerLoadingBridge] = field(
        default=None,
        metadata={
            "name": "PassengerLoadingBridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area: Optional[DeicingArea] = field(
        default=None,
        metadata={
            "name": "DeicingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    road: Optional[Road] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_stand: Optional[AircraftStand] = field(
        default=None,
        metadata={
            "name": "AircraftStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_element: Optional[ApronElement] = field(
        default=None,
        metadata={
            "name": "ApronElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron: Optional[Apron] = field(
        default=None,
        metadata={
            "name": "Apron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line: Optional[GuidanceLine] = field(
        default=None,
        metadata={
            "name": "GuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_element: Optional[TaxiwayElement] = field(
        default=None,
        metadata={
            "name": "TaxiwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway: Optional[Taxiway] = field(
        default=None,
        metadata={
            "name": "Taxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position: Optional[TaxiHoldingPosition] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_blast_pad: Optional[RunwayBlastPad] = field(
        default=None,
        metadata={
            "name": "RunwayBlastPad",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_visual_range: Optional[RunwayVisualRange] = field(
        default=None,
        metadata={
            "name": "RunwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_element: Optional[RunwayElement] = field(
        default=None,
        metadata={
            "name": "RunwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arresting_gear: Optional[ArrestingGear] = field(
        default=None,
        metadata={
            "name": "ArrestingGear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway: Optional[Runway] = field(
        default=None,
        metadata={
            "name": "Runway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_centreline_point: Optional[RunwayCentrelinePoint] = field(
        default=None,
        metadata={
            "name": "RunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction: Optional[RunwayDirection] = field(
        default=None,
        metadata={
            "name": "RunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    feature_collection: Optional["FeatureCollection"] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation_at_distance: Optional[
        "DirectedObservationAtDistance"
    ] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation: Optional["DirectedObservation"] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    observation: Optional["Observation"] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class ObservationType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    using: Optional["Using"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    subject: Optional["Subject"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    target: Optional["Target"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    result_of: Optional[ResultOf] = field(
        default=None,
        metadata={
            "name": "resultOf",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class DirectedObservationType(ObservationType):
    direction: Optional[Direction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class Observation(ObservationType):
    """The content model is a straightforward extension of gml:AbstractFeatureType;
    it automatically has the gml:identifier, gml:description,
    gml:descriptionReference, gml:name, and gml:boundedBy properties.

    The gml:validTime element describes the time of the observation.
    Note that this may be a time instant or a time period. The gml:using
    property contains or references a description of a sensor,
    instrument or procedure used for the observation. The gml:target
    property contains or references the specimen, region or station
    which is the object of the observation. This property is
    particularly useful for remote observations, such as photographs,
    where a generic location property might apply to the location of the
    camera or the location of the field of view, and thus may be
    ambiguous. The gml:subject element is provided as a convenient
    synonym for gml:target. This is the term commonly used in
    phtotography. The gml:resultOf property indicates the result of the
    observation.  The value may be inline, or a reference to a value
    elsewhere.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureMember(FeaturePropertyType):
    class Meta:
        name = "featureMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedObservation(DirectedObservationType):
    """A gml:DirectedObservation is the same as an observation except that it adds
    an additional gml:direction property.

    This is the direction in which the observation was acquired. Clearly
    this applies only to certain types of observations such as visual
    observations by people, or observations obtained from terrestrial
    cameras.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedObservationAtDistanceType(DirectedObservationType):
    distance: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class DirectedObservationAtDistance(DirectedObservationAtDistanceType):
    """Gml:DirectedObservationAtDistance adds an additional distance property.

    This is the distance from the observer to the subject of the
    observation. Clearly this applies only to certain types of
    observations such as visual observations by people, or observations
    obtained from terrestrial cameras.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureArrayPropertyType:
    aixmbasic_message: Iterable[AixmbasicMessage] = field(
        default_factory=list,
        metadata={
            "name": "AIXMBasicMessage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/message",
            "sequence": 1,
        },
    )
    airport_sign: Iterable[AirportSign] = field(
        default_factory=list,
        metadata={
            "name": "AirportSign",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "sequence": 1,
        },
    )
    wind_direction_indicator: Iterable[WindDirectionIndicator] = field(
        default_factory=list,
        metadata={
            "name": "WindDirectionIndicator",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "sequence": 1,
        },
    )
    event: Iterable[Event] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "sequence": 1,
        },
    )
    rules_procedures: Iterable[RulesProcedures] = field(
        default_factory=list,
        metadata={
            "name": "RulesProcedures",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    aerial_refuelling: Iterable[AerialRefuelling] = field(
        default_factory=list,
        metadata={
            "name": "AerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    change_over_point: Iterable[ChangeOverPoint] = field(
        default_factory=list,
        metadata={
            "name": "ChangeOverPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    route: Iterable[Route] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    route_dme: Iterable[RouteDme] = field(
        default_factory=list,
        metadata={
            "name": "RouteDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    route_segment: Iterable[RouteSegment] = field(
        default_factory=list,
        metadata={
            "name": "RouteSegment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    flight_restriction: Iterable[FlightRestriction] = field(
        default_factory=list,
        metadata={
            "name": "FlightRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airspace_border_crossing: Iterable[AirspaceBorderCrossing] = field(
        default_factory=list,
        metadata={
            "name": "AirspaceBorderCrossing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    unplanned_holding: Iterable[UnplannedHolding] = field(
        default_factory=list,
        metadata={
            "name": "UnplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    holding_pattern: Iterable[HoldingPattern] = field(
        default_factory=list,
        metadata={
            "name": "HoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    safe_altitude_area: Iterable[SafeAltitudeArea] = field(
        default_factory=list,
        metadata={
            "name": "SafeAltitudeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    procedure_dme: Iterable[ProcedureDme] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    departure_leg: Iterable[DepartureLeg] = field(
        default_factory=list,
        metadata={
            "name": "DepartureLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    arrival_leg: Iterable[ArrivalLeg] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    missed_approach_leg: Iterable[MissedApproachLeg] = field(
        default_factory=list,
        metadata={
            "name": "MissedApproachLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    intermediate_leg: Iterable[IntermediateLeg] = field(
        default_factory=list,
        metadata={
            "name": "IntermediateLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    initial_leg: Iterable[InitialLeg] = field(
        default_factory=list,
        metadata={
            "name": "InitialLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    final_leg: Iterable[FinalLeg] = field(
        default_factory=list,
        metadata={
            "name": "FinalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    arrival_feeder_leg: Iterable[ArrivalFeederLeg] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFeederLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    navigation_area_restriction: Iterable[NavigationAreaRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NavigationAreaRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    standard_instrument_arrival: Iterable[StandardInstrumentArrival] = field(
        default_factory=list,
        metadata={
            "name": "StandardInstrumentArrival",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    standard_instrument_departure: Iterable[StandardInstrumentDeparture] = (
        field(
            default_factory=list,
            metadata={
                "name": "StandardInstrumentDeparture",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    instrument_approach_procedure: Iterable[InstrumentApproachProcedure] = (
        field(
            default_factory=list,
            metadata={
                "name": "InstrumentApproachProcedure",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    navigation_area: Iterable[NavigationArea] = field(
        default_factory=list,
        metadata={
            "name": "NavigationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    terminal_arrival_area: Iterable[TerminalArrivalArea] = field(
        default_factory=list,
        metadata={
            "name": "TerminalArrivalArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    circling_area: Iterable[CirclingArea] = field(
        default_factory=list,
        metadata={
            "name": "CirclingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    vertical_structure: Iterable[VerticalStructure] = field(
        default_factory=list,
        metadata={
            "name": "VerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    obstacle_area: Iterable[ObstacleArea] = field(
        default_factory=list,
        metadata={
            "name": "ObstacleArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    unit: Iterable[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    organisation_authority: Iterable[OrganisationAuthority] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationAuthority",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    aeronautical_ground_light: Iterable[AeronauticalGroundLight] = field(
        default_factory=list,
        metadata={
            "name": "AeronauticalGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    significant_point_in_airspace: Iterable[SignificantPointInAirspace] = (
        field(
            default_factory=list,
            metadata={
                "name": "SignificantPointInAirspace",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    designated_point: Iterable[DesignatedPoint] = field(
        default_factory=list,
        metadata={
            "name": "DesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    special_navigation_system: Iterable[SpecialNavigationSystem] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    special_navigation_station: Iterable[SpecialNavigationStation] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    checkpoint_vor: Iterable[CheckpointVor] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointVOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    checkpoint_ins: Iterable[CheckpointIns] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointINS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    direction_finder: Iterable[DirectionFinder] = field(
        default_factory=list,
        metadata={
            "name": "DirectionFinder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    tacan: Iterable[Tacan] = field(
        default_factory=list,
        metadata={
            "name": "TACAN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    vor: Iterable[Vor] = field(
        default_factory=list,
        metadata={
            "name": "VOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    ndb: Iterable[Ndb] = field(
        default_factory=list,
        metadata={
            "name": "NDB",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    sdf: Iterable[Sdf] = field(
        default_factory=list,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    marker_beacon: Iterable[MarkerBeacon] = field(
        default_factory=list,
        metadata={
            "name": "MarkerBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    localizer: Iterable[Localizer] = field(
        default_factory=list,
        metadata={
            "name": "Localizer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    glidepath: Iterable[Glidepath] = field(
        default_factory=list,
        metadata={
            "name": "Glidepath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    elevation: Iterable[Elevation] = field(
        default_factory=list,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    dme: Iterable[Dme] = field(
        default_factory=list,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    azimuth: Iterable[Azimuth] = field(
        default_factory=list,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    navaid: Iterable[Navaid] = field(
        default_factory=list,
        metadata={
            "name": "Navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    distance_indication: Iterable[DistanceIndication] = field(
        default_factory=list,
        metadata={
            "name": "DistanceIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    angle_indication: Iterable[AngleIndication] = field(
        default_factory=list,
        metadata={
            "name": "AngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    pilot_controlled_lighting: Iterable[PilotControlledLighting] = field(
        default_factory=list,
        metadata={
            "name": "PilotControlledLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    radio_communication_channel: Iterable[RadioCommunicationChannel] = field(
        default_factory=list,
        metadata={
            "name": "RadioCommunicationChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_supplies_service: Iterable[AirportSuppliesService] = field(
        default_factory=list,
        metadata={
            "name": "AirportSuppliesService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_clearance_service: Iterable[AirportClearanceService] = field(
        default_factory=list,
        metadata={
            "name": "AirportClearanceService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    fire_fighting_service: Iterable[FireFightingService] = field(
        default_factory=list,
        metadata={
            "name": "FireFightingService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    aircraft_ground_service: Iterable[AircraftGroundService] = field(
        default_factory=list,
        metadata={
            "name": "AircraftGroundService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    passenger_service: Iterable[PassengerService] = field(
        default_factory=list,
        metadata={
            "name": "PassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    search_rescue_service: Iterable[SearchRescueService] = field(
        default_factory=list,
        metadata={
            "name": "SearchRescueService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    air_traffic_management_service: Iterable[AirTrafficManagementService] = (
        field(
            default_factory=list,
            metadata={
                "name": "AirTrafficManagementService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    air_traffic_control_service: Iterable[AirTrafficControlService] = field(
        default_factory=list,
        metadata={
            "name": "AirTrafficControlService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    ground_traffic_control_service: Iterable[GroundTrafficControlService] = (
        field(
            default_factory=list,
            metadata={
                "name": "GroundTrafficControlService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    information_service: Iterable[InformationService] = field(
        default_factory=list,
        metadata={
            "name": "InformationService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    special_date: Iterable[SpecialDate] = field(
        default_factory=list,
        metadata={
            "name": "SpecialDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    radio_frequency_area: Iterable[RadioFrequencyArea] = field(
        default_factory=list,
        metadata={
            "name": "RadioFrequencyArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    standard_level_column: Iterable[StandardLevelColumn] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    standard_level_sector: Iterable[StandardLevelSector] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    standard_level_table: Iterable[StandardLevelTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    holding_assessment: Iterable[HoldingAssessment] = field(
        default_factory=list,
        metadata={
            "name": "HoldingAssessment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    radar_system: Iterable[RadarSystem] = field(
        default_factory=list,
        metadata={
            "name": "RadarSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    secondary_surveillance_radar: Iterable[SecondarySurveillanceRadar] = field(
        default_factory=list,
        metadata={
            "name": "SecondarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    primary_surveillance_radar: Iterable[PrimarySurveillanceRadar] = field(
        default_factory=list,
        metadata={
            "name": "PrimarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    precision_approach_radar: Iterable[PrecisionApproachRadar] = field(
        default_factory=list,
        metadata={
            "name": "PrecisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    geo_border: Iterable[GeoBorder] = field(
        default_factory=list,
        metadata={
            "name": "GeoBorder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airspace: Iterable[Airspace] = field(
        default_factory=list,
        metadata={
            "name": "Airspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    authority_for_airspace: Iterable[AuthorityForAirspace] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityForAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_hot_spot: Iterable[AirportHotSpot] = field(
        default_factory=list,
        metadata={
            "name": "AirportHotSpot",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    altimeter_source: Iterable[AltimeterSource] = field(
        default_factory=list,
        metadata={
            "name": "AltimeterSource",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_heliport: Iterable[AirportHeliport] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_heliport_collocation: Iterable[AirportHeliportCollocation] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliportCollocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    touch_down_lift_off_safe_area: Iterable[TouchDownLiftOffSafeArea] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffSafeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_protect_area: Iterable[RunwayProtectArea] = field(
        default_factory=list,
        metadata={
            "name": "RunwayProtectArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    non_movement_area: Iterable[NonMovementArea] = field(
        default_factory=list,
        metadata={
            "name": "NonMovementArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    survey_control_point: Iterable[SurveyControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "SurveyControlPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    work_area: Iterable[WorkArea] = field(
        default_factory=list,
        metadata={
            "name": "WorkArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    seaplane_ramp_site: Iterable[SeaplaneRampSite] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneRampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    seaplane_landing_area: Iterable[SeaplaneLandingArea] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneLandingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    marking_buoy: Iterable[MarkingBuoy] = field(
        default_factory=list,
        metadata={
            "name": "MarkingBuoy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    floating_dock_site: Iterable[FloatingDockSite] = field(
        default_factory=list,
        metadata={
            "name": "FloatingDockSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    stand_marking: Iterable[StandMarking] = field(
        default_factory=list,
        metadata={
            "name": "StandMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxi_holding_position_marking: Iterable[TaxiHoldingPositionMarking] = (
        field(
            default_factory=list,
            metadata={
                "name": "TaxiHoldingPositionMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    deicing_area_marking: Iterable[DeicingAreaMarking] = field(
        default_factory=list,
        metadata={
            "name": "DeicingAreaMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    guidance_line_marking: Iterable[GuidanceLineMarking] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_marking: Iterable[RunwayMarking] = field(
        default_factory=list,
        metadata={
            "name": "RunwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    touch_down_lift_off_marking: Iterable[TouchDownLiftOffMarking] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    airport_protection_area_marking: Iterable[AirportProtectionAreaMarking] = (
        field(
            default_factory=list,
            metadata={
                "name": "AirportProtectionAreaMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    apron_marking: Iterable[ApronMarking] = field(
        default_factory=list,
        metadata={
            "name": "ApronMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxiway_marking: Iterable[TaxiwayMarking] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    approach_lighting_system: Iterable[ApproachLightingSystem] = field(
        default_factory=list,
        metadata={
            "name": "ApproachLightingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxi_holding_position_light_system: Iterable[
        TaxiHoldingPositionLightSystem
    ] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPositionLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_protect_area_light_system: Iterable[
        RunwayProtectAreaLightSystem
    ] = field(
        default_factory=list,
        metadata={
            "name": "RunwayProtectAreaLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    guidance_line_light_system: Iterable[GuidanceLineLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    touch_down_lift_off_light_system: Iterable[TouchDownLiftOffLightSystem] = (
        field(
            default_factory=list,
            metadata={
                "name": "TouchDownLiftOffLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    runway_direction_light_system: Iterable[RunwayDirectionLightSystem] = (
        field(
            default_factory=list,
            metadata={
                "name": "RunwayDirectionLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "sequence": 1,
            },
        )
    )
    taxiway_light_system: Iterable[TaxiwayLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    apron_light_system: Iterable[ApronLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "ApronLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    visual_glide_slope_indicator: Iterable[VisualGlideSlopeIndicator] = field(
        default_factory=list,
        metadata={
            "name": "VisualGlideSlopeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    touch_down_lift_off: Iterable[TouchDownLiftOff] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    passenger_loading_bridge: Iterable[PassengerLoadingBridge] = field(
        default_factory=list,
        metadata={
            "name": "PassengerLoadingBridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    deicing_area: Iterable[DeicingArea] = field(
        default_factory=list,
        metadata={
            "name": "DeicingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    road: Iterable[Road] = field(
        default_factory=list,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    aircraft_stand: Iterable[AircraftStand] = field(
        default_factory=list,
        metadata={
            "name": "AircraftStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    apron_element: Iterable[ApronElement] = field(
        default_factory=list,
        metadata={
            "name": "ApronElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    apron: Iterable[Apron] = field(
        default_factory=list,
        metadata={
            "name": "Apron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    guidance_line: Iterable[GuidanceLine] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxiway_element: Iterable[TaxiwayElement] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxiway: Iterable[Taxiway] = field(
        default_factory=list,
        metadata={
            "name": "Taxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    taxi_holding_position: Iterable[TaxiHoldingPosition] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_blast_pad: Iterable[RunwayBlastPad] = field(
        default_factory=list,
        metadata={
            "name": "RunwayBlastPad",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_visual_range: Iterable[RunwayVisualRange] = field(
        default_factory=list,
        metadata={
            "name": "RunwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_element: Iterable[RunwayElement] = field(
        default_factory=list,
        metadata={
            "name": "RunwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    arresting_gear: Iterable[ArrestingGear] = field(
        default_factory=list,
        metadata={
            "name": "ArrestingGear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway: Iterable[Runway] = field(
        default_factory=list,
        metadata={
            "name": "Runway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_centreline_point: Iterable[RunwayCentrelinePoint] = field(
        default_factory=list,
        metadata={
            "name": "RunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    runway_direction: Iterable[RunwayDirection] = field(
        default_factory=list,
        metadata={
            "name": "RunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    feature_collection: Iterable["FeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    directed_observation_at_distance: Iterable[
        DirectedObservationAtDistance
    ] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    directed_observation: Iterable[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    observation: Iterable[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    rectified_grid_coverage: Iterable[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    grid_coverage: Iterable[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    multi_solid_coverage: Iterable[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    multi_surface_coverage: Iterable[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    multi_curve_coverage: Iterable[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    multi_point_coverage: Iterable[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    dynamic_feature_collection: Iterable[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    dynamic_feature: Iterable[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )


@dataclass
class FeatureMembers(FeatureArrayPropertyType):
    class Meta:
        name = "featureMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureCollectionType(AbstractFeatureType):
    feature_member: Iterable[FeatureMember] = field(
        default_factory=list,
        metadata={
            "name": "featureMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    feature_members: Optional[FeatureMembers] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class FeatureCollectionType(AbstractFeatureCollectionType):
    pass


@dataclass
class FeatureCollection(FeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ProcedurePropertyType1:
    class Meta:
        name = "ProcedurePropertyType"

    aixmbasic_message: Optional[AixmbasicMessage] = field(
        default=None,
        metadata={
            "name": "AIXMBasicMessage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/message",
        },
    )
    airport_sign: Optional[AirportSign] = field(
        default=None,
        metadata={
            "name": "AirportSign",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    wind_direction_indicator: Optional[WindDirectionIndicator] = field(
        default=None,
        metadata={
            "name": "WindDirectionIndicator",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    event: Optional[Event] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    rules_procedures: Optional[RulesProcedures] = field(
        default=None,
        metadata={
            "name": "RulesProcedures",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aerial_refuelling: Optional[AerialRefuelling] = field(
        default=None,
        metadata={
            "name": "AerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    change_over_point: Optional[ChangeOverPoint] = field(
        default=None,
        metadata={
            "name": "ChangeOverPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route: Optional[Route] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_dme: Optional[RouteDme] = field(
        default=None,
        metadata={
            "name": "RouteDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_segment: Optional[RouteSegment] = field(
        default=None,
        metadata={
            "name": "RouteSegment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_restriction: Optional[FlightRestriction] = field(
        default=None,
        metadata={
            "name": "FlightRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_border_crossing: Optional[AirspaceBorderCrossing] = field(
        default=None,
        metadata={
            "name": "AirspaceBorderCrossing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unplanned_holding: Optional[UnplannedHolding] = field(
        default=None,
        metadata={
            "name": "UnplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_pattern: Optional[HoldingPattern] = field(
        default=None,
        metadata={
            "name": "HoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    safe_altitude_area: Optional[SafeAltitudeArea] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_dme: Optional[ProcedureDme] = field(
        default=None,
        metadata={
            "name": "ProcedureDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    departure_leg: Optional[DepartureLeg] = field(
        default=None,
        metadata={
            "name": "DepartureLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_leg: Optional[ArrivalLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    missed_approach_leg: Optional[MissedApproachLeg] = field(
        default=None,
        metadata={
            "name": "MissedApproachLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    intermediate_leg: Optional[IntermediateLeg] = field(
        default=None,
        metadata={
            "name": "IntermediateLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    initial_leg: Optional[InitialLeg] = field(
        default=None,
        metadata={
            "name": "InitialLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    final_leg: Optional[FinalLeg] = field(
        default=None,
        metadata={
            "name": "FinalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_feeder_leg: Optional[ArrivalFeederLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalFeederLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_restriction: Optional[NavigationAreaRestriction] = field(
        default=None,
        metadata={
            "name": "NavigationAreaRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_arrival: Optional[StandardInstrumentArrival] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentArrival",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_departure: Optional[StandardInstrumentDeparture] = (
        field(
            default=None,
            metadata={
                "name": "StandardInstrumentDeparture",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    instrument_approach_procedure: Optional[InstrumentApproachProcedure] = (
        field(
            default=None,
            metadata={
                "name": "InstrumentApproachProcedure",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    navigation_area: Optional[NavigationArea] = field(
        default=None,
        metadata={
            "name": "NavigationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_arrival_area: Optional[TerminalArrivalArea] = field(
        default=None,
        metadata={
            "name": "TerminalArrivalArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_area: Optional[CirclingArea] = field(
        default=None,
        metadata={
            "name": "CirclingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure: Optional[VerticalStructure] = field(
        default=None,
        metadata={
            "name": "VerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    obstacle_area: Optional[ObstacleArea] = field(
        default=None,
        metadata={
            "name": "ObstacleArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    organisation_authority: Optional[OrganisationAuthority] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthority",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aeronautical_ground_light: Optional[AeronauticalGroundLight] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    significant_point_in_airspace: Optional[SignificantPointInAirspace] = (
        field(
            default=None,
            metadata={
                "name": "SignificantPointInAirspace",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    designated_point: Optional[DesignatedPoint] = field(
        default=None,
        metadata={
            "name": "DesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_system: Optional[SpecialNavigationSystem] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station: Optional[SpecialNavigationStation] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_vor: Optional[CheckpointVor] = field(
        default=None,
        metadata={
            "name": "CheckpointVOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_ins: Optional[CheckpointIns] = field(
        default=None,
        metadata={
            "name": "CheckpointINS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    direction_finder: Optional[DirectionFinder] = field(
        default=None,
        metadata={
            "name": "DirectionFinder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tacan: Optional[Tacan] = field(
        default=None,
        metadata={
            "name": "TACAN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vor: Optional[Vor] = field(
        default=None,
        metadata={
            "name": "VOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ndb: Optional[Ndb] = field(
        default=None,
        metadata={
            "name": "NDB",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    sdf: Optional[Sdf] = field(
        default=None,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marker_beacon: Optional[MarkerBeacon] = field(
        default=None,
        metadata={
            "name": "MarkerBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    localizer: Optional[Localizer] = field(
        default=None,
        metadata={
            "name": "Localizer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    glidepath: Optional[Glidepath] = field(
        default=None,
        metadata={
            "name": "Glidepath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    elevation: Optional[Elevation] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    dme: Optional[Dme] = field(
        default=None,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    azimuth: Optional[Azimuth] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid: Optional[Navaid] = field(
        default=None,
        metadata={
            "name": "Navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    distance_indication: Optional[DistanceIndication] = field(
        default=None,
        metadata={
            "name": "DistanceIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    angle_indication: Optional[AngleIndication] = field(
        default=None,
        metadata={
            "name": "AngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    pilot_controlled_lighting: Optional[PilotControlledLighting] = field(
        default=None,
        metadata={
            "name": "PilotControlledLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_channel: Optional[RadioCommunicationChannel] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_supplies_service: Optional[AirportSuppliesService] = field(
        default=None,
        metadata={
            "name": "AirportSuppliesService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_clearance_service: Optional[AirportClearanceService] = field(
        default=None,
        metadata={
            "name": "AirportClearanceService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    fire_fighting_service: Optional[FireFightingService] = field(
        default=None,
        metadata={
            "name": "FireFightingService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_ground_service: Optional[AircraftGroundService] = field(
        default=None,
        metadata={
            "name": "AircraftGroundService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_service: Optional[PassengerService] = field(
        default=None,
        metadata={
            "name": "PassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    search_rescue_service: Optional[SearchRescueService] = field(
        default=None,
        metadata={
            "name": "SearchRescueService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_management_service: Optional[AirTrafficManagementService] = (
        field(
            default=None,
            metadata={
                "name": "AirTrafficManagementService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    air_traffic_control_service: Optional[AirTrafficControlService] = field(
        default=None,
        metadata={
            "name": "AirTrafficControlService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_traffic_control_service: Optional[GroundTrafficControlService] = (
        field(
            default=None,
            metadata={
                "name": "GroundTrafficControlService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    information_service: Optional[InformationService] = field(
        default=None,
        metadata={
            "name": "InformationService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_date: Optional[SpecialDate] = field(
        default=None,
        metadata={
            "name": "SpecialDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_frequency_area: Optional[RadioFrequencyArea] = field(
        default=None,
        metadata={
            "name": "RadioFrequencyArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_column: Optional[StandardLevelColumn] = field(
        default=None,
        metadata={
            "name": "StandardLevelColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_sector: Optional[StandardLevelSector] = field(
        default=None,
        metadata={
            "name": "StandardLevelSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_table: Optional[StandardLevelTable] = field(
        default=None,
        metadata={
            "name": "StandardLevelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_assessment: Optional[HoldingAssessment] = field(
        default=None,
        metadata={
            "name": "HoldingAssessment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radar_system: Optional[RadarSystem] = field(
        default=None,
        metadata={
            "name": "RadarSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    secondary_surveillance_radar: Optional[SecondarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "SecondarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    primary_surveillance_radar: Optional[PrimarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "PrimarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    precision_approach_radar: Optional[PrecisionApproachRadar] = field(
        default=None,
        metadata={
            "name": "PrecisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    geo_border: Optional[GeoBorder] = field(
        default=None,
        metadata={
            "name": "GeoBorder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace: Optional[Airspace] = field(
        default=None,
        metadata={
            "name": "Airspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    authority_for_airspace: Optional[AuthorityForAirspace] = field(
        default=None,
        metadata={
            "name": "AuthorityForAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_hot_spot: Optional[AirportHotSpot] = field(
        default=None,
        metadata={
            "name": "AirportHotSpot",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source: Optional[AltimeterSource] = field(
        default=None,
        metadata={
            "name": "AltimeterSource",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport: Optional[AirportHeliport] = field(
        default=None,
        metadata={
            "name": "AirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_collocation: Optional[AirportHeliportCollocation] = field(
        default=None,
        metadata={
            "name": "AirportHeliportCollocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_safe_area: Optional[TouchDownLiftOffSafeArea] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffSafeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area: Optional[RunwayProtectArea] = field(
        default=None,
        metadata={
            "name": "RunwayProtectArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    non_movement_area: Optional[NonMovementArea] = field(
        default=None,
        metadata={
            "name": "NonMovementArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    survey_control_point: Optional[SurveyControlPoint] = field(
        default=None,
        metadata={
            "name": "SurveyControlPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    work_area: Optional[WorkArea] = field(
        default=None,
        metadata={
            "name": "WorkArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_ramp_site: Optional[SeaplaneRampSite] = field(
        default=None,
        metadata={
            "name": "SeaplaneRampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_landing_area: Optional[SeaplaneLandingArea] = field(
        default=None,
        metadata={
            "name": "SeaplaneLandingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marking_buoy: Optional[MarkingBuoy] = field(
        default=None,
        metadata={
            "name": "MarkingBuoy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    floating_dock_site: Optional[FloatingDockSite] = field(
        default=None,
        metadata={
            "name": "FloatingDockSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    stand_marking: Optional[StandMarking] = field(
        default=None,
        metadata={
            "name": "StandMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_marking: Optional[TaxiHoldingPositionMarking] = (
        field(
            default=None,
            metadata={
                "name": "TaxiHoldingPositionMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    deicing_area_marking: Optional[DeicingAreaMarking] = field(
        default=None,
        metadata={
            "name": "DeicingAreaMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_marking: Optional[GuidanceLineMarking] = field(
        default=None,
        metadata={
            "name": "GuidanceLineMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_marking: Optional[RunwayMarking] = field(
        default=None,
        metadata={
            "name": "RunwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_marking: Optional[TouchDownLiftOffMarking] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_protection_area_marking: Optional[AirportProtectionAreaMarking] = (
        field(
            default=None,
            metadata={
                "name": "AirportProtectionAreaMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    apron_marking: Optional[ApronMarking] = field(
        default=None,
        metadata={
            "name": "ApronMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_marking: Optional[TaxiwayMarking] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    approach_lighting_system: Optional[ApproachLightingSystem] = field(
        default=None,
        metadata={
            "name": "ApproachLightingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_light_system: Optional[
        TaxiHoldingPositionLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area_light_system: Optional[
        RunwayProtectAreaLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "RunwayProtectAreaLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_light_system: Optional[GuidanceLineLightSystem] = field(
        default=None,
        metadata={
            "name": "GuidanceLineLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_light_system: Optional[TouchDownLiftOffLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "TouchDownLiftOffLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    runway_direction_light_system: Optional[RunwayDirectionLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "RunwayDirectionLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    taxiway_light_system: Optional[TaxiwayLightSystem] = field(
        default=None,
        metadata={
            "name": "TaxiwayLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_light_system: Optional[ApronLightSystem] = field(
        default=None,
        metadata={
            "name": "ApronLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    visual_glide_slope_indicator: Optional[VisualGlideSlopeIndicator] = field(
        default=None,
        metadata={
            "name": "VisualGlideSlopeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off: Optional[TouchDownLiftOff] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_loading_bridge: Optional[PassengerLoadingBridge] = field(
        default=None,
        metadata={
            "name": "PassengerLoadingBridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area: Optional[DeicingArea] = field(
        default=None,
        metadata={
            "name": "DeicingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    road: Optional[Road] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_stand: Optional[AircraftStand] = field(
        default=None,
        metadata={
            "name": "AircraftStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_element: Optional[ApronElement] = field(
        default=None,
        metadata={
            "name": "ApronElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron: Optional[Apron] = field(
        default=None,
        metadata={
            "name": "Apron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line: Optional[GuidanceLine] = field(
        default=None,
        metadata={
            "name": "GuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_element: Optional[TaxiwayElement] = field(
        default=None,
        metadata={
            "name": "TaxiwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway: Optional[Taxiway] = field(
        default=None,
        metadata={
            "name": "Taxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position: Optional[TaxiHoldingPosition] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_blast_pad: Optional[RunwayBlastPad] = field(
        default=None,
        metadata={
            "name": "RunwayBlastPad",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_visual_range: Optional[RunwayVisualRange] = field(
        default=None,
        metadata={
            "name": "RunwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_element: Optional[RunwayElement] = field(
        default=None,
        metadata={
            "name": "RunwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arresting_gear: Optional[ArrestingGear] = field(
        default=None,
        metadata={
            "name": "ArrestingGear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway: Optional[Runway] = field(
        default=None,
        metadata={
            "name": "Runway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_centreline_point: Optional[RunwayCentrelinePoint] = field(
        default=None,
        metadata={
            "name": "RunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction: Optional[RunwayDirection] = field(
        default=None,
        metadata={
            "name": "RunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation_at_distance: Optional[
        DirectedObservationAtDistance
    ] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation: Optional[DirectedObservation] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class TargetPropertyType:
    aixmbasic_message: Optional[AixmbasicMessage] = field(
        default=None,
        metadata={
            "name": "AIXMBasicMessage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/message",
        },
    )
    airport_sign: Optional[AirportSign] = field(
        default=None,
        metadata={
            "name": "AirportSign",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    wind_direction_indicator: Optional[WindDirectionIndicator] = field(
        default=None,
        metadata={
            "name": "WindDirectionIndicator",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    event: Optional[Event] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    rules_procedures: Optional[RulesProcedures] = field(
        default=None,
        metadata={
            "name": "RulesProcedures",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aerial_refuelling: Optional[AerialRefuelling] = field(
        default=None,
        metadata={
            "name": "AerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    change_over_point: Optional[ChangeOverPoint] = field(
        default=None,
        metadata={
            "name": "ChangeOverPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route: Optional[Route] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_dme: Optional[RouteDme] = field(
        default=None,
        metadata={
            "name": "RouteDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_segment: Optional[RouteSegment] = field(
        default=None,
        metadata={
            "name": "RouteSegment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_restriction: Optional[FlightRestriction] = field(
        default=None,
        metadata={
            "name": "FlightRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_border_crossing: Optional[AirspaceBorderCrossing] = field(
        default=None,
        metadata={
            "name": "AirspaceBorderCrossing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unplanned_holding: Optional[UnplannedHolding] = field(
        default=None,
        metadata={
            "name": "UnplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_pattern: Optional[HoldingPattern] = field(
        default=None,
        metadata={
            "name": "HoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    safe_altitude_area: Optional[SafeAltitudeArea] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_dme: Optional[ProcedureDme] = field(
        default=None,
        metadata={
            "name": "ProcedureDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    departure_leg: Optional[DepartureLeg] = field(
        default=None,
        metadata={
            "name": "DepartureLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_leg: Optional[ArrivalLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    missed_approach_leg: Optional[MissedApproachLeg] = field(
        default=None,
        metadata={
            "name": "MissedApproachLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    intermediate_leg: Optional[IntermediateLeg] = field(
        default=None,
        metadata={
            "name": "IntermediateLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    initial_leg: Optional[InitialLeg] = field(
        default=None,
        metadata={
            "name": "InitialLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    final_leg: Optional[FinalLeg] = field(
        default=None,
        metadata={
            "name": "FinalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_feeder_leg: Optional[ArrivalFeederLeg] = field(
        default=None,
        metadata={
            "name": "ArrivalFeederLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_restriction: Optional[NavigationAreaRestriction] = field(
        default=None,
        metadata={
            "name": "NavigationAreaRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_arrival: Optional[StandardInstrumentArrival] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentArrival",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_departure: Optional[StandardInstrumentDeparture] = (
        field(
            default=None,
            metadata={
                "name": "StandardInstrumentDeparture",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    instrument_approach_procedure: Optional[InstrumentApproachProcedure] = (
        field(
            default=None,
            metadata={
                "name": "InstrumentApproachProcedure",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    navigation_area: Optional[NavigationArea] = field(
        default=None,
        metadata={
            "name": "NavigationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_arrival_area: Optional[TerminalArrivalArea] = field(
        default=None,
        metadata={
            "name": "TerminalArrivalArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_area: Optional[CirclingArea] = field(
        default=None,
        metadata={
            "name": "CirclingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure: Optional[VerticalStructure] = field(
        default=None,
        metadata={
            "name": "VerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    obstacle_area: Optional[ObstacleArea] = field(
        default=None,
        metadata={
            "name": "ObstacleArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    organisation_authority: Optional[OrganisationAuthority] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthority",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aeronautical_ground_light: Optional[AeronauticalGroundLight] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    significant_point_in_airspace: Optional[SignificantPointInAirspace] = (
        field(
            default=None,
            metadata={
                "name": "SignificantPointInAirspace",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    designated_point: Optional[DesignatedPoint] = field(
        default=None,
        metadata={
            "name": "DesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_system: Optional[SpecialNavigationSystem] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station: Optional[SpecialNavigationStation] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_vor: Optional[CheckpointVor] = field(
        default=None,
        metadata={
            "name": "CheckpointVOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_ins: Optional[CheckpointIns] = field(
        default=None,
        metadata={
            "name": "CheckpointINS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    direction_finder: Optional[DirectionFinder] = field(
        default=None,
        metadata={
            "name": "DirectionFinder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tacan: Optional[Tacan] = field(
        default=None,
        metadata={
            "name": "TACAN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vor: Optional[Vor] = field(
        default=None,
        metadata={
            "name": "VOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ndb: Optional[Ndb] = field(
        default=None,
        metadata={
            "name": "NDB",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    sdf: Optional[Sdf] = field(
        default=None,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marker_beacon: Optional[MarkerBeacon] = field(
        default=None,
        metadata={
            "name": "MarkerBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    localizer: Optional[Localizer] = field(
        default=None,
        metadata={
            "name": "Localizer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    glidepath: Optional[Glidepath] = field(
        default=None,
        metadata={
            "name": "Glidepath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    elevation: Optional[Elevation] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    dme: Optional[Dme] = field(
        default=None,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    azimuth: Optional[Azimuth] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid: Optional[Navaid] = field(
        default=None,
        metadata={
            "name": "Navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    distance_indication: Optional[DistanceIndication] = field(
        default=None,
        metadata={
            "name": "DistanceIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    angle_indication: Optional[AngleIndication] = field(
        default=None,
        metadata={
            "name": "AngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    pilot_controlled_lighting: Optional[PilotControlledLighting] = field(
        default=None,
        metadata={
            "name": "PilotControlledLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_channel: Optional[RadioCommunicationChannel] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_supplies_service: Optional[AirportSuppliesService] = field(
        default=None,
        metadata={
            "name": "AirportSuppliesService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_clearance_service: Optional[AirportClearanceService] = field(
        default=None,
        metadata={
            "name": "AirportClearanceService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    fire_fighting_service: Optional[FireFightingService] = field(
        default=None,
        metadata={
            "name": "FireFightingService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_ground_service: Optional[AircraftGroundService] = field(
        default=None,
        metadata={
            "name": "AircraftGroundService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_service: Optional[PassengerService] = field(
        default=None,
        metadata={
            "name": "PassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    search_rescue_service: Optional[SearchRescueService] = field(
        default=None,
        metadata={
            "name": "SearchRescueService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_management_service: Optional[AirTrafficManagementService] = (
        field(
            default=None,
            metadata={
                "name": "AirTrafficManagementService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    air_traffic_control_service: Optional[AirTrafficControlService] = field(
        default=None,
        metadata={
            "name": "AirTrafficControlService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_traffic_control_service: Optional[GroundTrafficControlService] = (
        field(
            default=None,
            metadata={
                "name": "GroundTrafficControlService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    information_service: Optional[InformationService] = field(
        default=None,
        metadata={
            "name": "InformationService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_date: Optional[SpecialDate] = field(
        default=None,
        metadata={
            "name": "SpecialDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_frequency_area: Optional[RadioFrequencyArea] = field(
        default=None,
        metadata={
            "name": "RadioFrequencyArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_column: Optional[StandardLevelColumn] = field(
        default=None,
        metadata={
            "name": "StandardLevelColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_sector: Optional[StandardLevelSector] = field(
        default=None,
        metadata={
            "name": "StandardLevelSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_table: Optional[StandardLevelTable] = field(
        default=None,
        metadata={
            "name": "StandardLevelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_assessment: Optional[HoldingAssessment] = field(
        default=None,
        metadata={
            "name": "HoldingAssessment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radar_system: Optional[RadarSystem] = field(
        default=None,
        metadata={
            "name": "RadarSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    secondary_surveillance_radar: Optional[SecondarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "SecondarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    primary_surveillance_radar: Optional[PrimarySurveillanceRadar] = field(
        default=None,
        metadata={
            "name": "PrimarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    precision_approach_radar: Optional[PrecisionApproachRadar] = field(
        default=None,
        metadata={
            "name": "PrecisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    geo_border: Optional[GeoBorder] = field(
        default=None,
        metadata={
            "name": "GeoBorder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace: Optional[Airspace] = field(
        default=None,
        metadata={
            "name": "Airspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    authority_for_airspace: Optional[AuthorityForAirspace] = field(
        default=None,
        metadata={
            "name": "AuthorityForAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_hot_spot: Optional[AirportHotSpot] = field(
        default=None,
        metadata={
            "name": "AirportHotSpot",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source: Optional[AltimeterSource] = field(
        default=None,
        metadata={
            "name": "AltimeterSource",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport: Optional[AirportHeliport] = field(
        default=None,
        metadata={
            "name": "AirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_collocation: Optional[AirportHeliportCollocation] = field(
        default=None,
        metadata={
            "name": "AirportHeliportCollocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_safe_area: Optional[TouchDownLiftOffSafeArea] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffSafeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area: Optional[RunwayProtectArea] = field(
        default=None,
        metadata={
            "name": "RunwayProtectArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    non_movement_area: Optional[NonMovementArea] = field(
        default=None,
        metadata={
            "name": "NonMovementArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    survey_control_point: Optional[SurveyControlPoint] = field(
        default=None,
        metadata={
            "name": "SurveyControlPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    work_area: Optional[WorkArea] = field(
        default=None,
        metadata={
            "name": "WorkArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_ramp_site: Optional[SeaplaneRampSite] = field(
        default=None,
        metadata={
            "name": "SeaplaneRampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_landing_area: Optional[SeaplaneLandingArea] = field(
        default=None,
        metadata={
            "name": "SeaplaneLandingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marking_buoy: Optional[MarkingBuoy] = field(
        default=None,
        metadata={
            "name": "MarkingBuoy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    floating_dock_site: Optional[FloatingDockSite] = field(
        default=None,
        metadata={
            "name": "FloatingDockSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    stand_marking: Optional[StandMarking] = field(
        default=None,
        metadata={
            "name": "StandMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_marking: Optional[TaxiHoldingPositionMarking] = (
        field(
            default=None,
            metadata={
                "name": "TaxiHoldingPositionMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    deicing_area_marking: Optional[DeicingAreaMarking] = field(
        default=None,
        metadata={
            "name": "DeicingAreaMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_marking: Optional[GuidanceLineMarking] = field(
        default=None,
        metadata={
            "name": "GuidanceLineMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_marking: Optional[RunwayMarking] = field(
        default=None,
        metadata={
            "name": "RunwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_marking: Optional[TouchDownLiftOffMarking] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_protection_area_marking: Optional[AirportProtectionAreaMarking] = (
        field(
            default=None,
            metadata={
                "name": "AirportProtectionAreaMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    apron_marking: Optional[ApronMarking] = field(
        default=None,
        metadata={
            "name": "ApronMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_marking: Optional[TaxiwayMarking] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    approach_lighting_system: Optional[ApproachLightingSystem] = field(
        default=None,
        metadata={
            "name": "ApproachLightingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_light_system: Optional[
        TaxiHoldingPositionLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area_light_system: Optional[
        RunwayProtectAreaLightSystem
    ] = field(
        default=None,
        metadata={
            "name": "RunwayProtectAreaLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_light_system: Optional[GuidanceLineLightSystem] = field(
        default=None,
        metadata={
            "name": "GuidanceLineLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_light_system: Optional[TouchDownLiftOffLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "TouchDownLiftOffLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    runway_direction_light_system: Optional[RunwayDirectionLightSystem] = (
        field(
            default=None,
            metadata={
                "name": "RunwayDirectionLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    taxiway_light_system: Optional[TaxiwayLightSystem] = field(
        default=None,
        metadata={
            "name": "TaxiwayLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_light_system: Optional[ApronLightSystem] = field(
        default=None,
        metadata={
            "name": "ApronLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    visual_glide_slope_indicator: Optional[VisualGlideSlopeIndicator] = field(
        default=None,
        metadata={
            "name": "VisualGlideSlopeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off: Optional[TouchDownLiftOff] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_loading_bridge: Optional[PassengerLoadingBridge] = field(
        default=None,
        metadata={
            "name": "PassengerLoadingBridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area: Optional[DeicingArea] = field(
        default=None,
        metadata={
            "name": "DeicingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    road: Optional[Road] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_stand: Optional[AircraftStand] = field(
        default=None,
        metadata={
            "name": "AircraftStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_element: Optional[ApronElement] = field(
        default=None,
        metadata={
            "name": "ApronElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron: Optional[Apron] = field(
        default=None,
        metadata={
            "name": "Apron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line: Optional[GuidanceLine] = field(
        default=None,
        metadata={
            "name": "GuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_element: Optional[TaxiwayElement] = field(
        default=None,
        metadata={
            "name": "TaxiwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway: Optional[Taxiway] = field(
        default=None,
        metadata={
            "name": "Taxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position: Optional[TaxiHoldingPosition] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_blast_pad: Optional[RunwayBlastPad] = field(
        default=None,
        metadata={
            "name": "RunwayBlastPad",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_visual_range: Optional[RunwayVisualRange] = field(
        default=None,
        metadata={
            "name": "RunwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_element: Optional[RunwayElement] = field(
        default=None,
        metadata={
            "name": "RunwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arresting_gear: Optional[ArrestingGear] = field(
        default=None,
        metadata={
            "name": "ArrestingGear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway: Optional[Runway] = field(
        default=None,
        metadata={
            "name": "Runway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_centreline_point: Optional[RunwayCentrelinePoint] = field(
        default=None,
        metadata={
            "name": "RunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction: Optional[RunwayDirection] = field(
        default=None,
        metadata={
            "name": "RunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation_at_distance: Optional[
        DirectedObservationAtDistance
    ] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation: Optional[DirectedObservation] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_surface: Optional[ElevatedSurface] = field(
        default=None,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_curve: Optional[ElevatedCurve] = field(
        default=None,
        metadata={
            "name": "ElevatedCurve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    opengis_net_gml_3_2_curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_point: Optional[ElevatedPoint] = field(
        default=None,
        metadata={
            "name": "ElevatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    opengis_net_gml_3_2_point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class Subject(TargetPropertyType):
    class Meta:
        name = "subject"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Target(TargetPropertyType):
    class Meta:
        name = "target"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Using(ProcedurePropertyType1):
    class Meta:
        name = "using"
        namespace = "http://www.opengis.net/gml/3.2"
