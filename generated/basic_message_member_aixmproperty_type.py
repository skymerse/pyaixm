from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_feature_member_type import AbstractFeatureMemberType
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
from generated.deicing_area import DeicingArea
from generated.deicing_area_marking import DeicingAreaMarking
from generated.departure_leg import DepartureLeg
from generated.designated_point import DesignatedPoint
from generated.direction_finder import DirectionFinder
from generated.distance_indication import DistanceIndication
from generated.dme import Dme
from generated.elevation import Elevation
from generated.event import Event
from generated.final_leg import FinalLeg
from generated.fire_fighting_service import FireFightingService
from generated.flight_restriction import FlightRestriction
from generated.floating_dock_site import FloatingDockSite
from generated.geo_border import GeoBorder
from generated.glidepath import Glidepath
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
from generated.localizer import Localizer
from generated.marker_beacon import MarkerBeacon
from generated.marking_buoy import MarkingBuoy
from generated.missed_approach_leg import MissedApproachLeg
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
from generated.precision_approach_radar import PrecisionApproachRadar
from generated.primary_surveillance_radar import PrimarySurveillanceRadar
from generated.procedure_dme import ProcedureDme
from generated.radar_system import RadarSystem
from generated.radio_communication_channel import RadioCommunicationChannel
from generated.radio_frequency_area import RadioFrequencyArea
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
from generated.special_date import SpecialDate
from generated.special_navigation_station import SpecialNavigationStation
from generated.special_navigation_system import SpecialNavigationSystem
from generated.stand_marking import StandMarking
from generated.standard_instrument_arrival import StandardInstrumentArrival
from generated.standard_instrument_departure import StandardInstrumentDeparture
from generated.standard_level_column import StandardLevelColumn
from generated.standard_level_sector import StandardLevelSector
from generated.standard_level_table import StandardLevelTable
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
from generated.touch_down_lift_off import TouchDownLiftOff
from generated.touch_down_lift_off_light_system import (
    TouchDownLiftOffLightSystem,
)
from generated.touch_down_lift_off_marking import TouchDownLiftOffMarking
from generated.touch_down_lift_off_safe_area import TouchDownLiftOffSafeArea
from generated.type_type import TypeType
from generated.unit import Unit
from generated.unplanned_holding import UnplannedHolding
from generated.vertical_structure import VerticalStructure
from generated.visual_glide_slope_indicator import VisualGlideSlopeIndicator
from generated.vor import Vor
from generated.wind_direction_indicator import WindDirectionIndicator
from generated.work_area import WorkArea

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/message"


@dataclass
class BasicMessageMemberAixmpropertyType(AbstractFeatureMemberType):
    class Meta:
        name = "BasicMessageMemberAIXMPropertyType"

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
