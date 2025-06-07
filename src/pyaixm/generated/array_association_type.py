from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_general_operation_parameter_property_type import (
    OperationParameterGroup,
)
from pyaixm.generated.abstract_general_parameter_value_property_type import (
    ParameterValueGroup,
)
from pyaixm.generated.abstract_gmltype import AbstractGmltype
from pyaixm.generated.abstract_time_primitive_type import (
    TimeEdge,
    TimeInstant,
    TimeNode,
    TimePeriod,
)
from pyaixm.generated.aerial_refuelling import AerialRefuelling
from pyaixm.generated.aerial_refuelling_time_slice import (
    AerialRefuellingTimeSlice,
)
from pyaixm.generated.aeronautical_ground_light import AeronauticalGroundLight
from pyaixm.generated.aeronautical_ground_light_time_slice import (
    AeronauticalGroundLightTimeSlice,
)
from pyaixm.generated.affine_cs_1 import AffineCs1
from pyaixm.generated.affine_placement import AffinePlacement
from pyaixm.generated.air_traffic_control_service import (
    AirTrafficControlService,
)
from pyaixm.generated.air_traffic_control_service_time_slice import (
    AirTrafficControlServiceTimeSlice,
)
from pyaixm.generated.air_traffic_management_service import (
    AirTrafficManagementService,
)
from pyaixm.generated.air_traffic_management_service_time_slice import (
    AirTrafficManagementServiceTimeSlice,
)
from pyaixm.generated.aircraft_ground_service import AircraftGroundService
from pyaixm.generated.aircraft_ground_service_time_slice import (
    AircraftGroundServiceTimeSlice,
)
from pyaixm.generated.aircraft_stand import AircraftStand
from pyaixm.generated.aircraft_stand_time_slice import AircraftStandTimeSlice
from pyaixm.generated.airport_clearance_service import AirportClearanceService
from pyaixm.generated.airport_clearance_service_time_slice import (
    AirportClearanceServiceTimeSlice,
)
from pyaixm.generated.airport_heliport import AirportHeliport
from pyaixm.generated.airport_heliport_collocation import (
    AirportHeliportCollocation,
)
from pyaixm.generated.airport_heliport_collocation_time_slice import (
    AirportHeliportCollocationTimeSlice,
)
from pyaixm.generated.airport_heliport_time_slice import (
    AirportHeliportTimeSlice,
)
from pyaixm.generated.airport_hot_spot import AirportHotSpot
from pyaixm.generated.airport_hot_spot_time_slice import (
    AirportHotSpotTimeSlice,
)
from pyaixm.generated.airport_protection_area_marking import (
    AirportProtectionAreaMarking,
)
from pyaixm.generated.airport_protection_area_marking_time_slice import (
    AirportProtectionAreaMarkingTimeSlice,
)
from pyaixm.generated.airport_sign import AirportSign
from pyaixm.generated.airport_sign_time_slice import AirportSignTimeSlice
from pyaixm.generated.airport_supplies_service import AirportSuppliesService
from pyaixm.generated.airport_supplies_service_time_slice import (
    AirportSuppliesServiceTimeSlice,
)
from pyaixm.generated.airspace import Airspace
from pyaixm.generated.airspace_border_crossing import AirspaceBorderCrossing
from pyaixm.generated.airspace_border_crossing_time_slice import (
    AirspaceBorderCrossingTimeSlice,
)
from pyaixm.generated.airspace_time_slice import AirspaceTimeSlice
from pyaixm.generated.aixmbasic_message import AixmbasicMessage
from pyaixm.generated.altimeter_source import AltimeterSource
from pyaixm.generated.altimeter_source_time_slice import (
    AltimeterSourceTimeSlice,
)
from pyaixm.generated.angle_indication import AngleIndication
from pyaixm.generated.angle_indication_time_slice import (
    AngleIndicationTimeSlice,
)
from pyaixm.generated.approach_lighting_system import ApproachLightingSystem
from pyaixm.generated.approach_lighting_system_time_slice import (
    ApproachLightingSystemTimeSlice,
)
from pyaixm.generated.apron import Apron
from pyaixm.generated.apron_element import ApronElement
from pyaixm.generated.apron_element_time_slice import ApronElementTimeSlice
from pyaixm.generated.apron_light_system import ApronLightSystem
from pyaixm.generated.apron_light_system_time_slice import (
    ApronLightSystemTimeSlice,
)
from pyaixm.generated.apron_marking import ApronMarking
from pyaixm.generated.apron_marking_time_slice import ApronMarkingTimeSlice
from pyaixm.generated.apron_time_slice import ApronTimeSlice
from pyaixm.generated.arc import Arc
from pyaixm.generated.arc_by_bulge import ArcByBulge
from pyaixm.generated.arc_by_center_point import ArcByCenterPoint
from pyaixm.generated.arc_string import ArcString
from pyaixm.generated.arc_string_by_bulge import ArcStringByBulge
from pyaixm.generated.arresting_gear import ArrestingGear
from pyaixm.generated.arresting_gear_time_slice import ArrestingGearTimeSlice
from pyaixm.generated.arrival_feeder_leg import ArrivalFeederLeg
from pyaixm.generated.arrival_feeder_leg_time_slice import (
    ArrivalFeederLegTimeSlice,
)
from pyaixm.generated.arrival_leg import ArrivalLeg
from pyaixm.generated.arrival_leg_time_slice import ArrivalLegTimeSlice
from pyaixm.generated.authority_for_airspace import AuthorityForAirspace
from pyaixm.generated.authority_for_airspace_time_slice import (
    AuthorityForAirspaceTimeSlice,
)
from pyaixm.generated.azimuth import Azimuth
from pyaixm.generated.azimuth_time_slice import AzimuthTimeSlice
from pyaixm.generated.base_unit import BaseUnit
from pyaixm.generated.bezier import Bezier
from pyaixm.generated.boolean_1 import Boolean1
from pyaixm.generated.boolean_list import BooleanList
from pyaixm.generated.bspline import Bspline
from pyaixm.generated.cartesian_cs_1 import CartesianCs1
from pyaixm.generated.category import Category
from pyaixm.generated.category_extent import CategoryExtent
from pyaixm.generated.category_list import CategoryList
from pyaixm.generated.change_over_point import ChangeOverPoint
from pyaixm.generated.change_over_point_time_slice import (
    ChangeOverPointTimeSlice,
)
from pyaixm.generated.checkpoint_ins import CheckpointIns
from pyaixm.generated.checkpoint_instime_slice import CheckpointInstimeSlice
from pyaixm.generated.checkpoint_vor import CheckpointVor
from pyaixm.generated.checkpoint_vortime_slice import CheckpointVortimeSlice
from pyaixm.generated.circle import Circle
from pyaixm.generated.circle_by_center_point import CircleByCenterPoint
from pyaixm.generated.circling_area import CirclingArea
from pyaixm.generated.circling_area_time_slice import CirclingAreaTimeSlice
from pyaixm.generated.clothoid import Clothoid
from pyaixm.generated.conventional_unit import ConventionalUnit
from pyaixm.generated.coordinate_operation_property_type import (
    ConcatenatedOperation,
    PassThroughOperation,
)
from pyaixm.generated.coordinate_system_axis import CoordinateSystemAxis
from pyaixm.generated.count import Count
from pyaixm.generated.count_extent import CountExtent
from pyaixm.generated.count_list import CountList
from pyaixm.generated.coverage_function import CoverageFunction
from pyaixm.generated.coverage_mapping_rule import CoverageMappingRule
from pyaixm.generated.cubic_spline import CubicSpline
from pyaixm.generated.curve_property_type_1 import (
    CompositeCurve,
    Curve1,
    Curve2,
    ElevatedCurve,
    OffsetCurve,
    OrientableCurve,
)
from pyaixm.generated.cylindrical_cs_1 import CylindricalCs1
from pyaixm.generated.data_block import DataBlock
from pyaixm.generated.definition import Definition
from pyaixm.generated.definition_proxy import DefinitionProxy
from pyaixm.generated.deicing_area import DeicingArea
from pyaixm.generated.deicing_area_marking import DeicingAreaMarking
from pyaixm.generated.deicing_area_marking_time_slice import (
    DeicingAreaMarkingTimeSlice,
)
from pyaixm.generated.deicing_area_time_slice import DeicingAreaTimeSlice
from pyaixm.generated.departure_leg import DepartureLeg
from pyaixm.generated.departure_leg_time_slice import DepartureLegTimeSlice
from pyaixm.generated.derived_unit import DerivedUnit
from pyaixm.generated.designated_point import DesignatedPoint
from pyaixm.generated.designated_point_time_slice import (
    DesignatedPointTimeSlice,
)
from pyaixm.generated.dictionary_type import (
    DefinitionCollection,
    Dictionary,
)
from pyaixm.generated.direction_finder import DirectionFinder
from pyaixm.generated.direction_finder_time_slice import (
    DirectionFinderTimeSlice,
)
from pyaixm.generated.distance_indication import DistanceIndication
from pyaixm.generated.distance_indication_time_slice import (
    DistanceIndicationTimeSlice,
)
from pyaixm.generated.dme import Dme
from pyaixm.generated.dmetime_slice import DmetimeSlice
from pyaixm.generated.dynamic_feature import DynamicFeature
from pyaixm.generated.dynamic_feature_collection_type import (
    DynamicFeatureCollection,
)
from pyaixm.generated.elevated_point import ElevatedPoint
from pyaixm.generated.elevated_surface import ElevatedSurface
from pyaixm.generated.elevation import Elevation
from pyaixm.generated.elevation_time_slice import ElevationTimeSlice
from pyaixm.generated.ellipsoid_1 import Ellipsoid1
from pyaixm.generated.ellipsoidal_cs_1 import EllipsoidalCs1
from pyaixm.generated.envelope import Envelope
from pyaixm.generated.envelope_with_time_period import EnvelopeWithTimePeriod
from pyaixm.generated.event import Event
from pyaixm.generated.event_time_slice import EventTimeSlice
from pyaixm.generated.face_or_topo_solid_property_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from pyaixm.generated.feature_property_type import (
    DirectedObservation,
    DirectedObservationAtDistance,
    FeatureCollection,
    Observation,
)
from pyaixm.generated.file import File
from pyaixm.generated.final_leg import FinalLeg
from pyaixm.generated.final_leg_time_slice import FinalLegTimeSlice
from pyaixm.generated.fire_fighting_service import FireFightingService
from pyaixm.generated.fire_fighting_service_time_slice import (
    FireFightingServiceTimeSlice,
)
from pyaixm.generated.flight_restriction import FlightRestriction
from pyaixm.generated.flight_restriction_time_slice import (
    FlightRestrictionTimeSlice,
)
from pyaixm.generated.floating_dock_site import FloatingDockSite
from pyaixm.generated.floating_dock_site_time_slice import (
    FloatingDockSiteTimeSlice,
)
from pyaixm.generated.generic_meta_data import GenericMetaData
from pyaixm.generated.geo_border import GeoBorder
from pyaixm.generated.geo_border_time_slice import GeoBorderTimeSlice
from pyaixm.generated.geodesic import Geodesic
from pyaixm.generated.geodesic_string import GeodesicString
from pyaixm.generated.geometric_complex import GeometricComplex
from pyaixm.generated.geometry_array_property_type import MultiGeometry
from pyaixm.generated.glidepath import Glidepath
from pyaixm.generated.glidepath_time_slice import GlidepathTimeSlice
from pyaixm.generated.grid import Grid
from pyaixm.generated.grid_coverage import GridCoverage
from pyaixm.generated.grid_function import GridFunction
from pyaixm.generated.ground_traffic_control_service import (
    GroundTrafficControlService,
)
from pyaixm.generated.ground_traffic_control_service_time_slice import (
    GroundTrafficControlServiceTimeSlice,
)
from pyaixm.generated.guidance_line import GuidanceLine
from pyaixm.generated.guidance_line_light_system import GuidanceLineLightSystem
from pyaixm.generated.guidance_line_light_system_time_slice import (
    GuidanceLineLightSystemTimeSlice,
)
from pyaixm.generated.guidance_line_marking import GuidanceLineMarking
from pyaixm.generated.guidance_line_marking_time_slice import (
    GuidanceLineMarkingTimeSlice,
)
from pyaixm.generated.guidance_line_time_slice import GuidanceLineTimeSlice
from pyaixm.generated.holding_assessment import HoldingAssessment
from pyaixm.generated.holding_assessment_time_slice import (
    HoldingAssessmentTimeSlice,
)
from pyaixm.generated.holding_pattern import HoldingPattern
from pyaixm.generated.holding_pattern_time_slice import HoldingPatternTimeSlice
from pyaixm.generated.information_service import InformationService
from pyaixm.generated.information_service_time_slice import (
    InformationServiceTimeSlice,
)
from pyaixm.generated.initial_leg import InitialLeg
from pyaixm.generated.initial_leg_time_slice import InitialLegTimeSlice
from pyaixm.generated.instrument_approach_procedure import (
    InstrumentApproachProcedure,
)
from pyaixm.generated.instrument_approach_procedure_time_slice import (
    InstrumentApproachProcedureTimeSlice,
)
from pyaixm.generated.intermediate_leg import IntermediateLeg
from pyaixm.generated.intermediate_leg_time_slice import (
    IntermediateLegTimeSlice,
)
from pyaixm.generated.line_string import LineString
from pyaixm.generated.line_string_segment import LineStringSegment
from pyaixm.generated.linear_cs_1 import LinearCs1
from pyaixm.generated.linear_ring import LinearRing
from pyaixm.generated.localizer import Localizer
from pyaixm.generated.localizer_time_slice import LocalizerTimeSlice
from pyaixm.generated.marker_beacon import MarkerBeacon
from pyaixm.generated.marker_beacon_time_slice import MarkerBeaconTimeSlice
from pyaixm.generated.marking_buoy import MarkingBuoy
from pyaixm.generated.marking_buoy_time_slice import MarkingBuoyTimeSlice
from pyaixm.generated.member import Member
from pyaixm.generated.missed_approach_leg import MissedApproachLeg
from pyaixm.generated.missed_approach_leg_time_slice import (
    MissedApproachLegTimeSlice,
)
from pyaixm.generated.moving_object_status import MovingObjectStatus
from pyaixm.generated.multi_curve import MultiCurve
from pyaixm.generated.multi_curve_coverage import MultiCurveCoverage
from pyaixm.generated.multi_point import MultiPoint
from pyaixm.generated.multi_point_coverage import MultiPointCoverage
from pyaixm.generated.multi_solid import MultiSolid
from pyaixm.generated.multi_solid_coverage import MultiSolidCoverage
from pyaixm.generated.multi_surface import MultiSurface
from pyaixm.generated.multi_surface_coverage import MultiSurfaceCoverage
from pyaixm.generated.navaid import Navaid
from pyaixm.generated.navaid_time_slice import NavaidTimeSlice
from pyaixm.generated.navigation_area import NavigationArea
from pyaixm.generated.navigation_area_restriction import (
    NavigationAreaRestriction,
)
from pyaixm.generated.navigation_area_restriction_time_slice import (
    NavigationAreaRestrictionTimeSlice,
)
from pyaixm.generated.navigation_area_time_slice import NavigationAreaTimeSlice
from pyaixm.generated.ndb import Ndb
from pyaixm.generated.ndbtime_slice import NdbtimeSlice
from pyaixm.generated.non_movement_area import NonMovementArea
from pyaixm.generated.non_movement_area_time_slice import (
    NonMovementAreaTimeSlice,
)
from pyaixm.generated.oblique_cartesian_cs import ObliqueCartesianCs
from pyaixm.generated.obstacle_area import ObstacleArea
from pyaixm.generated.obstacle_area_time_slice import ObstacleAreaTimeSlice
from pyaixm.generated.operation_method import OperationMethod
from pyaixm.generated.operation_parameter_1 import OperationParameter1
from pyaixm.generated.organisation_authority import OrganisationAuthority
from pyaixm.generated.organisation_authority_time_slice import (
    OrganisationAuthorityTimeSlice,
)
from pyaixm.generated.parameter_value_1 import ParameterValue1
from pyaixm.generated.passenger_loading_bridge import PassengerLoadingBridge
from pyaixm.generated.passenger_loading_bridge_time_slice import (
    PassengerLoadingBridgeTimeSlice,
)
from pyaixm.generated.passenger_service import PassengerService
from pyaixm.generated.passenger_service_time_slice import (
    PassengerServiceTimeSlice,
)
from pyaixm.generated.pilot_controlled_lighting import PilotControlledLighting
from pyaixm.generated.pilot_controlled_lighting_time_slice import (
    PilotControlledLightingTimeSlice,
)
from pyaixm.generated.point_1 import Point1
from pyaixm.generated.point_2 import Point2
from pyaixm.generated.polar_cs_1 import PolarCs1
from pyaixm.generated.polygon import Polygon
from pyaixm.generated.polyhedral_surface import PolyhedralSurface
from pyaixm.generated.precision_approach_radar import PrecisionApproachRadar
from pyaixm.generated.precision_approach_radar_time_slice import (
    PrecisionApproachRadarTimeSlice,
)
from pyaixm.generated.primary_surveillance_radar import (
    PrimarySurveillanceRadar,
)
from pyaixm.generated.primary_surveillance_radar_time_slice import (
    PrimarySurveillanceRadarTimeSlice,
)
from pyaixm.generated.prime_meridian_1 import PrimeMeridian1
from pyaixm.generated.procedure_dme import ProcedureDme
from pyaixm.generated.procedure_dmetime_slice import ProcedureDmetimeSlice
from pyaixm.generated.quantity import Quantity
from pyaixm.generated.quantity_extent import QuantityExtent
from pyaixm.generated.quantity_list import QuantityList
from pyaixm.generated.radar_system import RadarSystem
from pyaixm.generated.radar_system_time_slice import RadarSystemTimeSlice
from pyaixm.generated.radio_communication_channel import (
    RadioCommunicationChannel,
)
from pyaixm.generated.radio_communication_channel_time_slice import (
    RadioCommunicationChannelTimeSlice,
)
from pyaixm.generated.radio_frequency_area import RadioFrequencyArea
from pyaixm.generated.radio_frequency_area_time_slice import (
    RadioFrequencyAreaTimeSlice,
)
from pyaixm.generated.rectified_grid import RectifiedGrid
from pyaixm.generated.rectified_grid_coverage import RectifiedGridCoverage
from pyaixm.generated.ring import Ring
from pyaixm.generated.road import Road
from pyaixm.generated.road_time_slice import RoadTimeSlice
from pyaixm.generated.route import Route
from pyaixm.generated.route_dme import RouteDme
from pyaixm.generated.route_dmetime_slice import RouteDmetimeSlice
from pyaixm.generated.route_segment import RouteSegment
from pyaixm.generated.route_segment_time_slice import RouteSegmentTimeSlice
from pyaixm.generated.route_time_slice import RouteTimeSlice
from pyaixm.generated.rules_procedures import RulesProcedures
from pyaixm.generated.rules_procedures_time_slice import (
    RulesProceduresTimeSlice,
)
from pyaixm.generated.runway import Runway
from pyaixm.generated.runway_blast_pad import RunwayBlastPad
from pyaixm.generated.runway_blast_pad_time_slice import (
    RunwayBlastPadTimeSlice,
)
from pyaixm.generated.runway_centreline_point import RunwayCentrelinePoint
from pyaixm.generated.runway_centreline_point_time_slice import (
    RunwayCentrelinePointTimeSlice,
)
from pyaixm.generated.runway_direction import RunwayDirection
from pyaixm.generated.runway_direction_light_system import (
    RunwayDirectionLightSystem,
)
from pyaixm.generated.runway_direction_light_system_time_slice import (
    RunwayDirectionLightSystemTimeSlice,
)
from pyaixm.generated.runway_direction_time_slice import (
    RunwayDirectionTimeSlice,
)
from pyaixm.generated.runway_element import RunwayElement
from pyaixm.generated.runway_element_time_slice import RunwayElementTimeSlice
from pyaixm.generated.runway_marking import RunwayMarking
from pyaixm.generated.runway_marking_time_slice import RunwayMarkingTimeSlice
from pyaixm.generated.runway_protect_area import RunwayProtectArea
from pyaixm.generated.runway_protect_area_light_system import (
    RunwayProtectAreaLightSystem,
)
from pyaixm.generated.runway_protect_area_light_system_time_slice import (
    RunwayProtectAreaLightSystemTimeSlice,
)
from pyaixm.generated.runway_protect_area_time_slice import (
    RunwayProtectAreaTimeSlice,
)
from pyaixm.generated.runway_time_slice import RunwayTimeSlice
from pyaixm.generated.runway_visual_range import RunwayVisualRange
from pyaixm.generated.runway_visual_range_time_slice import (
    RunwayVisualRangeTimeSlice,
)
from pyaixm.generated.safe_altitude_area import SafeAltitudeArea
from pyaixm.generated.safe_altitude_area_time_slice import (
    SafeAltitudeAreaTimeSlice,
)
from pyaixm.generated.sc_crs_property_type import (
    CompoundCrs,
    Conversion1,
    DerivedCrs,
    EngineeringCrs,
    EngineeringDatum1,
    GeocentricCrs,
    GeodeticCrs,
    GeodeticDatum1,
    GeographicCrs,
    ImageCrs,
    ImageDatum1,
    ProjectedCrs,
    TemporalCrs,
    TemporalDatum1,
    VerticalCrs,
    VerticalDatum1,
)
from pyaixm.generated.sdf import Sdf
from pyaixm.generated.sdftime_slice import SdftimeSlice
from pyaixm.generated.seaplane_landing_area import SeaplaneLandingArea
from pyaixm.generated.seaplane_landing_area_time_slice import (
    SeaplaneLandingAreaTimeSlice,
)
from pyaixm.generated.seaplane_ramp_site import SeaplaneRampSite
from pyaixm.generated.seaplane_ramp_site_time_slice import (
    SeaplaneRampSiteTimeSlice,
)
from pyaixm.generated.search_rescue_service import SearchRescueService
from pyaixm.generated.search_rescue_service_time_slice import (
    SearchRescueServiceTimeSlice,
)
from pyaixm.generated.secondary_surveillance_radar import (
    SecondarySurveillanceRadar,
)
from pyaixm.generated.secondary_surveillance_radar_time_slice import (
    SecondarySurveillanceRadarTimeSlice,
)
from pyaixm.generated.shell import Shell
from pyaixm.generated.significant_point_in_airspace import (
    SignificantPointInAirspace,
)
from pyaixm.generated.significant_point_in_airspace_time_slice import (
    SignificantPointInAirspaceTimeSlice,
)
from pyaixm.generated.solid import Solid
from pyaixm.generated.solid_property_type import CompositeSolid
from pyaixm.generated.special_date import SpecialDate
from pyaixm.generated.special_date_time_slice import SpecialDateTimeSlice
from pyaixm.generated.special_navigation_station import (
    SpecialNavigationStation,
)
from pyaixm.generated.special_navigation_station_time_slice import (
    SpecialNavigationStationTimeSlice,
)
from pyaixm.generated.special_navigation_system import SpecialNavigationSystem
from pyaixm.generated.special_navigation_system_time_slice import (
    SpecialNavigationSystemTimeSlice,
)
from pyaixm.generated.spherical_cs_1 import SphericalCs1
from pyaixm.generated.stand_marking import StandMarking
from pyaixm.generated.stand_marking_time_slice import StandMarkingTimeSlice
from pyaixm.generated.standard_instrument_arrival import (
    StandardInstrumentArrival,
)
from pyaixm.generated.standard_instrument_arrival_time_slice import (
    StandardInstrumentArrivalTimeSlice,
)
from pyaixm.generated.standard_instrument_departure import (
    StandardInstrumentDeparture,
)
from pyaixm.generated.standard_instrument_departure_time_slice import (
    StandardInstrumentDepartureTimeSlice,
)
from pyaixm.generated.standard_level_column import StandardLevelColumn
from pyaixm.generated.standard_level_column_time_slice import (
    StandardLevelColumnTimeSlice,
)
from pyaixm.generated.standard_level_sector import StandardLevelSector
from pyaixm.generated.standard_level_sector_time_slice import (
    StandardLevelSectorTimeSlice,
)
from pyaixm.generated.standard_level_table import StandardLevelTable
from pyaixm.generated.standard_level_table_time_slice import (
    StandardLevelTableTimeSlice,
)
from pyaixm.generated.surface_1 import Surface1
from pyaixm.generated.surface_2 import Surface2
from pyaixm.generated.surface_property_type_1 import (
    CompositeSurface,
    OrientableSurface,
)
from pyaixm.generated.survey_control_point import SurveyControlPoint
from pyaixm.generated.survey_control_point_time_slice import (
    SurveyControlPointTimeSlice,
)
from pyaixm.generated.tacan import Tacan
from pyaixm.generated.tacantime_slice import TacantimeSlice
from pyaixm.generated.taxi_holding_position import TaxiHoldingPosition
from pyaixm.generated.taxi_holding_position_light_system import (
    TaxiHoldingPositionLightSystem,
)
from pyaixm.generated.taxi_holding_position_light_system_time_slice import (
    TaxiHoldingPositionLightSystemTimeSlice,
)
from pyaixm.generated.taxi_holding_position_marking import (
    TaxiHoldingPositionMarking,
)
from pyaixm.generated.taxi_holding_position_marking_time_slice import (
    TaxiHoldingPositionMarkingTimeSlice,
)
from pyaixm.generated.taxi_holding_position_time_slice import (
    TaxiHoldingPositionTimeSlice,
)
from pyaixm.generated.taxiway import Taxiway
from pyaixm.generated.taxiway_element import TaxiwayElement
from pyaixm.generated.taxiway_element_time_slice import TaxiwayElementTimeSlice
from pyaixm.generated.taxiway_light_system import TaxiwayLightSystem
from pyaixm.generated.taxiway_light_system_time_slice import (
    TaxiwayLightSystemTimeSlice,
)
from pyaixm.generated.taxiway_marking import TaxiwayMarking
from pyaixm.generated.taxiway_marking_time_slice import TaxiwayMarkingTimeSlice
from pyaixm.generated.taxiway_time_slice import TaxiwayTimeSlice
from pyaixm.generated.temporal_cs import TemporalCs
from pyaixm.generated.terminal_arrival_area import TerminalArrivalArea
from pyaixm.generated.terminal_arrival_area_time_slice import (
    TerminalArrivalAreaTimeSlice,
)
from pyaixm.generated.time_calendar import TimeCalendar
from pyaixm.generated.time_clock import TimeClock
from pyaixm.generated.time_coordinate_system import TimeCoordinateSystem
from pyaixm.generated.time_cs_1 import TimeCs1
from pyaixm.generated.time_ordinal_reference_system import (
    TimeOrdinalReferenceSystem,
)
from pyaixm.generated.time_reference_system import TimeReferenceSystem
from pyaixm.generated.time_topology_complex import TimeTopologyComplex
from pyaixm.generated.tin import Tin
from pyaixm.generated.topo_complex_type import TopoComplex
from pyaixm.generated.touch_down_lift_off import TouchDownLiftOff
from pyaixm.generated.touch_down_lift_off_light_system import (
    TouchDownLiftOffLightSystem,
)
from pyaixm.generated.touch_down_lift_off_light_system_time_slice import (
    TouchDownLiftOffLightSystemTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_marking import (
    TouchDownLiftOffMarking,
)
from pyaixm.generated.touch_down_lift_off_marking_time_slice import (
    TouchDownLiftOffMarkingTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_safe_area import (
    TouchDownLiftOffSafeArea,
)
from pyaixm.generated.touch_down_lift_off_safe_area_time_slice import (
    TouchDownLiftOffSafeAreaTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_time_slice import (
    TouchDownLiftOffTimeSlice,
)
from pyaixm.generated.transformation import Transformation
from pyaixm.generated.triangulated_surface import TriangulatedSurface
from pyaixm.generated.unit import Unit
from pyaixm.generated.unit_definition import UnitDefinition
from pyaixm.generated.unit_time_slice import UnitTimeSlice
from pyaixm.generated.unplanned_holding import UnplannedHolding
from pyaixm.generated.unplanned_holding_time_slice import (
    UnplannedHoldingTimeSlice,
)
from pyaixm.generated.user_defined_cs_1 import UserDefinedCs1
from pyaixm.generated.value_array_property_type import (
    CompositeValue,
    ValueArray,
)
from pyaixm.generated.vertical_cs_1 import VerticalCs1
from pyaixm.generated.vertical_structure import VerticalStructure
from pyaixm.generated.vertical_structure_time_slice import (
    VerticalStructureTimeSlice,
)
from pyaixm.generated.visual_glide_slope_indicator import (
    VisualGlideSlopeIndicator,
)
from pyaixm.generated.visual_glide_slope_indicator_time_slice import (
    VisualGlideSlopeIndicatorTimeSlice,
)
from pyaixm.generated.vor import Vor
from pyaixm.generated.vortime_slice import VortimeSlice
from pyaixm.generated.wind_direction_indicator import WindDirectionIndicator
from pyaixm.generated.wind_direction_indicator_time_slice import (
    WindDirectionIndicatorTimeSlice,
)
from pyaixm.generated.work_area import WorkArea
from pyaixm.generated.work_area_time_slice import WorkAreaTimeSlice

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArrayAssociationType:
    generic_meta_data: Iterable[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value_group: Iterable[ParameterValueGroup] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value: Iterable[ParameterValue1] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_function: Iterable[GridFunction] = field(
        default_factory=list,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_mapping_rule: Iterable[CoverageMappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_function: Iterable[CoverageFunction] = field(
        default_factory=list,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    file: Iterable[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    data_block: Iterable[DataBlock] = field(
        default_factory=list,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_extent: Iterable[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    count_extent: Iterable[CountExtent] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    category_extent: Iterable[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_array: Iterable[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_value: Iterable[CompositeValue] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_list: Iterable[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    count_list: Iterable[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    category_list: Iterable[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    boolean_list: Iterable[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity: Iterable[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    count: Iterable[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    category: Iterable[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    boolean: Iterable[Boolean1] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    shell: Iterable[Shell] = field(
        default_factory=list,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_placement: Iterable[AffinePlacement] = field(
        default_factory=list,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodesic: Iterable[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodesic_string: Iterable[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    clothoid: Iterable[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    offset_curve: Iterable[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bezier: Iterable[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bspline: Iterable[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cubic_spline: Iterable[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    circle_by_center_point: Iterable[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_by_center_point: Iterable[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_by_bulge: Iterable[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_string_by_bulge: Iterable[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    circle: Iterable[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc: Iterable[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_string: Iterable[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string_segment: Iterable[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ring: Iterable[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_ring: Iterable[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope_with_time_period: Iterable[EnvelopeWithTimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope: Iterable[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    array: Iterable["Array"] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bag: Iterable["Bag"] = field(
        default_factory=list,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_complex: Iterable[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_solid: Iterable[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    face: Iterable[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    edge: Iterable[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    node: Iterable[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    airport_sign_time_slice: Iterable[AirportSignTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AirportSignTimeSlice",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    wind_direction_indicator_time_slice: Iterable[
        WindDirectionIndicatorTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "WindDirectionIndicatorTimeSlice",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    event_time_slice: Iterable[EventTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "EventTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    rules_procedures_time_slice: Iterable[RulesProceduresTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RulesProceduresTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aerial_refuelling_time_slice: Iterable[AerialRefuellingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AerialRefuellingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    change_over_point_time_slice: Iterable[ChangeOverPointTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ChangeOverPointTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_time_slice: Iterable[RouteTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RouteTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_dmetime_slice: Iterable[RouteDmetimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RouteDMETimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_segment_time_slice: Iterable[RouteSegmentTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RouteSegmentTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_restriction_time_slice: Iterable[FlightRestrictionTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "FlightRestrictionTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    airspace_border_crossing_time_slice: Iterable[
        AirspaceBorderCrossingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirspaceBorderCrossingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unplanned_holding_time_slice: Iterable[UnplannedHoldingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "UnplannedHoldingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_pattern_time_slice: Iterable[HoldingPatternTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "HoldingPatternTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    safe_altitude_area_time_slice: Iterable[SafeAltitudeAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "SafeAltitudeAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_dmetime_slice: Iterable[ProcedureDmetimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDMETimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    missed_approach_leg_time_slice: Iterable[MissedApproachLegTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "MissedApproachLegTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    intermediate_leg_time_slice: Iterable[IntermediateLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "IntermediateLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    initial_leg_time_slice: Iterable[InitialLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "InitialLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    final_leg_time_slice: Iterable[FinalLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "FinalLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    departure_leg_time_slice: Iterable[DepartureLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "DepartureLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_leg_time_slice: Iterable[ArrivalLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_feeder_leg_time_slice: Iterable[ArrivalFeederLegTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFeederLegTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_restriction_time_slice: Iterable[
        NavigationAreaRestrictionTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "NavigationAreaRestrictionTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_arrival_time_slice: Iterable[
        StandardInstrumentArrivalTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "StandardInstrumentArrivalTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_time_slice: Iterable[NavigationAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "NavigationAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_departure_time_slice: Iterable[
        StandardInstrumentDepartureTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "StandardInstrumentDepartureTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    instrument_approach_procedure_time_slice: Iterable[
        InstrumentApproachProcedureTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentApproachProcedureTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_arrival_area_time_slice: Iterable[
        TerminalArrivalAreaTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TerminalArrivalAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_area_time_slice: Iterable[CirclingAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "CirclingAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure_time_slice: Iterable[VerticalStructureTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "VerticalStructureTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    obstacle_area_time_slice: Iterable[ObstacleAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ObstacleAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit_time_slice: Iterable[UnitTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "UnitTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    organisation_authority_time_slice: Iterable[
        OrganisationAuthorityTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationAuthorityTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aeronautical_ground_light_time_slice: Iterable[
        AeronauticalGroundLightTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AeronauticalGroundLightTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    significant_point_in_airspace_time_slice: Iterable[
        SignificantPointInAirspaceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SignificantPointInAirspaceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    designated_point_time_slice: Iterable[DesignatedPointTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "DesignatedPointTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    direction_finder_time_slice: Iterable[DirectionFinderTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "DirectionFinderTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_system_time_slice: Iterable[
        SpecialNavigationSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tacantime_slice: Iterable[TacantimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "TACANTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vortime_slice: Iterable[VortimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "VORTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station_time_slice: Iterable[
        SpecialNavigationStationTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationStationTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ndbtime_slice: Iterable[NdbtimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "NDBTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    sdftime_slice: Iterable[SdftimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "SDFTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid_time_slice: Iterable[NavaidTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "NavaidTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marker_beacon_time_slice: Iterable[MarkerBeaconTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "MarkerBeaconTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    localizer_time_slice: Iterable[LocalizerTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "LocalizerTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    glidepath_time_slice: Iterable[GlidepathTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "GlidepathTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    elevation_time_slice: Iterable[ElevationTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ElevationTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    dmetime_slice: Iterable[DmetimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "DMETimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_vortime_slice: Iterable[CheckpointVortimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointVORTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_instime_slice: Iterable[CheckpointInstimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointINSTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    azimuth_time_slice: Iterable[AzimuthTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AzimuthTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    distance_indication_time_slice: Iterable[DistanceIndicationTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "DistanceIndicationTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    angle_indication_time_slice: Iterable[AngleIndicationTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AngleIndicationTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_supplies_service_time_slice: Iterable[
        AirportSuppliesServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirportSuppliesServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_clearance_service_time_slice: Iterable[
        AirportClearanceServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirportClearanceServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    fire_fighting_service_time_slice: Iterable[
        FireFightingServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "FireFightingServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_ground_service_time_slice: Iterable[
        AircraftGroundServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AircraftGroundServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_service_time_slice: Iterable[PassengerServiceTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "PassengerServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    search_rescue_service_time_slice: Iterable[
        SearchRescueServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SearchRescueServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_management_service_time_slice: Iterable[
        AirTrafficManagementServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirTrafficManagementServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_control_service_time_slice: Iterable[
        AirTrafficControlServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirTrafficControlServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_traffic_control_service_time_slice: Iterable[
        GroundTrafficControlServiceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "GroundTrafficControlServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    information_service_time_slice: Iterable[InformationServiceTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "InformationServiceTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    pilot_controlled_lighting_time_slice: Iterable[
        PilotControlledLightingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "PilotControlledLightingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_channel_time_slice: Iterable[
        RadioCommunicationChannelTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "RadioCommunicationChannelTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_date_time_slice: Iterable[SpecialDateTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "SpecialDateTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_frequency_area_time_slice: Iterable[RadioFrequencyAreaTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "RadioFrequencyAreaTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    standard_level_column_time_slice: Iterable[
        StandardLevelColumnTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelColumnTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_sector_time_slice: Iterable[
        StandardLevelSectorTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelSectorTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_table_time_slice: Iterable[StandardLevelTableTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "StandardLevelTableTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    holding_assessment_time_slice: Iterable[HoldingAssessmentTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "HoldingAssessmentTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    secondary_surveillance_radar_time_slice: Iterable[
        SecondarySurveillanceRadarTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SecondarySurveillanceRadarTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radar_system_time_slice: Iterable[RadarSystemTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RadarSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    primary_surveillance_radar_time_slice: Iterable[
        PrimarySurveillanceRadarTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "PrimarySurveillanceRadarTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    precision_approach_radar_time_slice: Iterable[
        PrecisionApproachRadarTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "PrecisionApproachRadarTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    geo_border_time_slice: Iterable[GeoBorderTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "GeoBorderTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_time_slice: Iterable[AirspaceTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AirspaceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    authority_for_airspace_time_slice: Iterable[
        AuthorityForAirspaceTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityForAirspaceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_hot_spot_time_slice: Iterable[AirportHotSpotTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AirportHotSpotTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source_time_slice: Iterable[AltimeterSourceTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AltimeterSourceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_time_slice: Iterable[AirportHeliportTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliportTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_collocation_time_slice: Iterable[
        AirportHeliportCollocationTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliportCollocationTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    non_movement_area_time_slice: Iterable[NonMovementAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "NonMovementAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    survey_control_point_time_slice: Iterable[SurveyControlPointTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "SurveyControlPointTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    work_area_time_slice: Iterable[WorkAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "WorkAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_ramp_site_time_slice: Iterable[SeaplaneRampSiteTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneRampSiteTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_landing_area_time_slice: Iterable[
        SeaplaneLandingAreaTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneLandingAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marking_buoy_time_slice: Iterable[MarkingBuoyTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "MarkingBuoyTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    floating_dock_site_time_slice: Iterable[FloatingDockSiteTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "FloatingDockSiteTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    stand_marking_time_slice: Iterable[StandMarkingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "StandMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_marking_time_slice: Iterable[
        TaxiHoldingPositionMarkingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPositionMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area_marking_time_slice: Iterable[DeicingAreaMarkingTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "DeicingAreaMarkingTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    guidance_line_marking_time_slice: Iterable[
        GuidanceLineMarkingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_marking_time_slice: Iterable[RunwayMarkingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RunwayMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_marking_time_slice: Iterable[
        TouchDownLiftOffMarkingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_protection_area_marking_time_slice: Iterable[
        AirportProtectionAreaMarkingTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirportProtectionAreaMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_marking_time_slice: Iterable[ApronMarkingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ApronMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_marking_time_slice: Iterable[TaxiwayMarkingTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    approach_lighting_system_time_slice: Iterable[
        ApproachLightingSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "ApproachLightingSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_light_system_time_slice: Iterable[
        TaxiHoldingPositionLightSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPositionLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area_light_system_time_slice: Iterable[
        RunwayProtectAreaLightSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "RunwayProtectAreaLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_light_system_time_slice: Iterable[
        GuidanceLineLightSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_light_system_time_slice: Iterable[
        TouchDownLiftOffLightSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction_light_system_time_slice: Iterable[
        RunwayDirectionLightSystemTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "RunwayDirectionLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_light_system_time_slice: Iterable[TaxiwayLightSystemTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "TaxiwayLightSystemTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    apron_light_system_time_slice: Iterable[ApronLightSystemTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ApronLightSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_time_slice: Iterable[TouchDownLiftOffTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "TouchDownLiftOffTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    touch_down_lift_off_safe_area_time_slice: Iterable[
        TouchDownLiftOffSafeAreaTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffSafeAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_loading_bridge_time_slice: Iterable[
        PassengerLoadingBridgeTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "PassengerLoadingBridgeTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area_time_slice: Iterable[DeicingAreaTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "DeicingAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    road_time_slice: Iterable[RoadTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RoadTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_stand_time_slice: Iterable[AircraftStandTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AircraftStandTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_element_time_slice: Iterable[ApronElementTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ApronElementTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_time_slice: Iterable[ApronTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ApronTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_time_slice: Iterable[GuidanceLineTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_element_time_slice: Iterable[TaxiwayElementTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayElementTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_time_slice: Iterable[TaxiwayTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_time_slice: Iterable[
        TaxiHoldingPositionTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPositionTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_blast_pad_time_slice: Iterable[RunwayBlastPadTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RunwayBlastPadTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_visual_range_time_slice: Iterable[RunwayVisualRangeTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "RunwayVisualRangeTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    visual_glide_slope_indicator_time_slice: Iterable[
        VisualGlideSlopeIndicatorTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "VisualGlideSlopeIndicatorTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_element_time_slice: Iterable[RunwayElementTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RunwayElementTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arresting_gear_time_slice: Iterable[ArrestingGearTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "ArrestingGearTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_time_slice: Iterable[RunwayTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RunwayTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_centreline_point_time_slice: Iterable[
        RunwayCentrelinePointTimeSlice
    ] = field(
        default_factory=list,
        metadata={
            "name": "RunwayCentrelinePointTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction_time_slice: Iterable[RunwayDirectionTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "RunwayDirectionTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area_time_slice: Iterable[RunwayProtectAreaTimeSlice] = (
        field(
            default_factory=list,
            metadata={
                "name": "RunwayProtectAreaTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    moving_object_status: Iterable[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    aixmbasic_message: Iterable[AixmbasicMessage] = field(
        default_factory=list,
        metadata={
            "name": "AIXMBasicMessage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/message",
        },
    )
    airport_sign: Iterable[AirportSign] = field(
        default_factory=list,
        metadata={
            "name": "AirportSign",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    wind_direction_indicator: Iterable[WindDirectionIndicator] = field(
        default_factory=list,
        metadata={
            "name": "WindDirectionIndicator",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    event: Iterable[Event] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    rules_procedures: Iterable[RulesProcedures] = field(
        default_factory=list,
        metadata={
            "name": "RulesProcedures",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aerial_refuelling: Iterable[AerialRefuelling] = field(
        default_factory=list,
        metadata={
            "name": "AerialRefuelling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    change_over_point: Iterable[ChangeOverPoint] = field(
        default_factory=list,
        metadata={
            "name": "ChangeOverPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route: Iterable[Route] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_dme: Iterable[RouteDme] = field(
        default_factory=list,
        metadata={
            "name": "RouteDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    route_segment: Iterable[RouteSegment] = field(
        default_factory=list,
        metadata={
            "name": "RouteSegment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_restriction: Iterable[FlightRestriction] = field(
        default_factory=list,
        metadata={
            "name": "FlightRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_border_crossing: Iterable[AirspaceBorderCrossing] = field(
        default_factory=list,
        metadata={
            "name": "AirspaceBorderCrossing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unplanned_holding: Iterable[UnplannedHolding] = field(
        default_factory=list,
        metadata={
            "name": "UnplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_pattern: Iterable[HoldingPattern] = field(
        default_factory=list,
        metadata={
            "name": "HoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    safe_altitude_area: Iterable[SafeAltitudeArea] = field(
        default_factory=list,
        metadata={
            "name": "SafeAltitudeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_dme: Iterable[ProcedureDme] = field(
        default_factory=list,
        metadata={
            "name": "ProcedureDME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    departure_leg: Iterable[DepartureLeg] = field(
        default_factory=list,
        metadata={
            "name": "DepartureLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_leg: Iterable[ArrivalLeg] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    missed_approach_leg: Iterable[MissedApproachLeg] = field(
        default_factory=list,
        metadata={
            "name": "MissedApproachLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    intermediate_leg: Iterable[IntermediateLeg] = field(
        default_factory=list,
        metadata={
            "name": "IntermediateLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    initial_leg: Iterable[InitialLeg] = field(
        default_factory=list,
        metadata={
            "name": "InitialLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    final_leg: Iterable[FinalLeg] = field(
        default_factory=list,
        metadata={
            "name": "FinalLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arrival_feeder_leg: Iterable[ArrivalFeederLeg] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFeederLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navigation_area_restriction: Iterable[NavigationAreaRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NavigationAreaRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_arrival: Iterable[StandardInstrumentArrival] = field(
        default_factory=list,
        metadata={
            "name": "StandardInstrumentArrival",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_instrument_departure: Iterable[StandardInstrumentDeparture] = (
        field(
            default_factory=list,
            metadata={
                "name": "StandardInstrumentDeparture",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
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
            },
        )
    )
    navigation_area: Iterable[NavigationArea] = field(
        default_factory=list,
        metadata={
            "name": "NavigationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_arrival_area: Iterable[TerminalArrivalArea] = field(
        default_factory=list,
        metadata={
            "name": "TerminalArrivalArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_area: Iterable[CirclingArea] = field(
        default_factory=list,
        metadata={
            "name": "CirclingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure: Iterable[VerticalStructure] = field(
        default_factory=list,
        metadata={
            "name": "VerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    obstacle_area: Iterable[ObstacleArea] = field(
        default_factory=list,
        metadata={
            "name": "ObstacleArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit: Iterable[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    organisation_authority: Iterable[OrganisationAuthority] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationAuthority",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aeronautical_ground_light: Iterable[AeronauticalGroundLight] = field(
        default_factory=list,
        metadata={
            "name": "AeronauticalGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    significant_point_in_airspace: Iterable[SignificantPointInAirspace] = (
        field(
            default_factory=list,
            metadata={
                "name": "SignificantPointInAirspace",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    designated_point: Iterable[DesignatedPoint] = field(
        default_factory=list,
        metadata={
            "name": "DesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_system: Iterable[SpecialNavigationSystem] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station: Iterable[SpecialNavigationStation] = field(
        default_factory=list,
        metadata={
            "name": "SpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_vor: Iterable[CheckpointVor] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointVOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    checkpoint_ins: Iterable[CheckpointIns] = field(
        default_factory=list,
        metadata={
            "name": "CheckpointINS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    direction_finder: Iterable[DirectionFinder] = field(
        default_factory=list,
        metadata={
            "name": "DirectionFinder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tacan: Iterable[Tacan] = field(
        default_factory=list,
        metadata={
            "name": "TACAN",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vor: Iterable[Vor] = field(
        default_factory=list,
        metadata={
            "name": "VOR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ndb: Iterable[Ndb] = field(
        default_factory=list,
        metadata={
            "name": "NDB",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    sdf: Iterable[Sdf] = field(
        default_factory=list,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marker_beacon: Iterable[MarkerBeacon] = field(
        default_factory=list,
        metadata={
            "name": "MarkerBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    localizer: Iterable[Localizer] = field(
        default_factory=list,
        metadata={
            "name": "Localizer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    glidepath: Iterable[Glidepath] = field(
        default_factory=list,
        metadata={
            "name": "Glidepath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    elevation: Iterable[Elevation] = field(
        default_factory=list,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    dme: Iterable[Dme] = field(
        default_factory=list,
        metadata={
            "name": "DME",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    azimuth: Iterable[Azimuth] = field(
        default_factory=list,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid: Iterable[Navaid] = field(
        default_factory=list,
        metadata={
            "name": "Navaid",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    distance_indication: Iterable[DistanceIndication] = field(
        default_factory=list,
        metadata={
            "name": "DistanceIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    angle_indication: Iterable[AngleIndication] = field(
        default_factory=list,
        metadata={
            "name": "AngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    pilot_controlled_lighting: Iterable[PilotControlledLighting] = field(
        default_factory=list,
        metadata={
            "name": "PilotControlledLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_channel: Iterable[RadioCommunicationChannel] = field(
        default_factory=list,
        metadata={
            "name": "RadioCommunicationChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_supplies_service: Iterable[AirportSuppliesService] = field(
        default_factory=list,
        metadata={
            "name": "AirportSuppliesService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_clearance_service: Iterable[AirportClearanceService] = field(
        default_factory=list,
        metadata={
            "name": "AirportClearanceService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    fire_fighting_service: Iterable[FireFightingService] = field(
        default_factory=list,
        metadata={
            "name": "FireFightingService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_ground_service: Iterable[AircraftGroundService] = field(
        default_factory=list,
        metadata={
            "name": "AircraftGroundService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_service: Iterable[PassengerService] = field(
        default_factory=list,
        metadata={
            "name": "PassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    search_rescue_service: Iterable[SearchRescueService] = field(
        default_factory=list,
        metadata={
            "name": "SearchRescueService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    air_traffic_management_service: Iterable[AirTrafficManagementService] = (
        field(
            default_factory=list,
            metadata={
                "name": "AirTrafficManagementService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    air_traffic_control_service: Iterable[AirTrafficControlService] = field(
        default_factory=list,
        metadata={
            "name": "AirTrafficControlService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_traffic_control_service: Iterable[GroundTrafficControlService] = (
        field(
            default_factory=list,
            metadata={
                "name": "GroundTrafficControlService",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    information_service: Iterable[InformationService] = field(
        default_factory=list,
        metadata={
            "name": "InformationService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_date: Iterable[SpecialDate] = field(
        default_factory=list,
        metadata={
            "name": "SpecialDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_frequency_area: Iterable[RadioFrequencyArea] = field(
        default_factory=list,
        metadata={
            "name": "RadioFrequencyArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_column: Iterable[StandardLevelColumn] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_sector: Iterable[StandardLevelSector] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    standard_level_table: Iterable[StandardLevelTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardLevelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    holding_assessment: Iterable[HoldingAssessment] = field(
        default_factory=list,
        metadata={
            "name": "HoldingAssessment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radar_system: Iterable[RadarSystem] = field(
        default_factory=list,
        metadata={
            "name": "RadarSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    secondary_surveillance_radar: Iterable[SecondarySurveillanceRadar] = field(
        default_factory=list,
        metadata={
            "name": "SecondarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    primary_surveillance_radar: Iterable[PrimarySurveillanceRadar] = field(
        default_factory=list,
        metadata={
            "name": "PrimarySurveillanceRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    precision_approach_radar: Iterable[PrecisionApproachRadar] = field(
        default_factory=list,
        metadata={
            "name": "PrecisionApproachRadar",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    geo_border: Iterable[GeoBorder] = field(
        default_factory=list,
        metadata={
            "name": "GeoBorder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace: Iterable[Airspace] = field(
        default_factory=list,
        metadata={
            "name": "Airspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    authority_for_airspace: Iterable[AuthorityForAirspace] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityForAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_hot_spot: Iterable[AirportHotSpot] = field(
        default_factory=list,
        metadata={
            "name": "AirportHotSpot",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source: Iterable[AltimeterSource] = field(
        default_factory=list,
        metadata={
            "name": "AltimeterSource",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport: Iterable[AirportHeliport] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_collocation: Iterable[AirportHeliportCollocation] = field(
        default_factory=list,
        metadata={
            "name": "AirportHeliportCollocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_safe_area: Iterable[TouchDownLiftOffSafeArea] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffSafeArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_protect_area: Iterable[RunwayProtectArea] = field(
        default_factory=list,
        metadata={
            "name": "RunwayProtectArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    non_movement_area: Iterable[NonMovementArea] = field(
        default_factory=list,
        metadata={
            "name": "NonMovementArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    survey_control_point: Iterable[SurveyControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "SurveyControlPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    work_area: Iterable[WorkArea] = field(
        default_factory=list,
        metadata={
            "name": "WorkArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_ramp_site: Iterable[SeaplaneRampSite] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneRampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    seaplane_landing_area: Iterable[SeaplaneLandingArea] = field(
        default_factory=list,
        metadata={
            "name": "SeaplaneLandingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    marking_buoy: Iterable[MarkingBuoy] = field(
        default_factory=list,
        metadata={
            "name": "MarkingBuoy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    floating_dock_site: Iterable[FloatingDockSite] = field(
        default_factory=list,
        metadata={
            "name": "FloatingDockSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    stand_marking: Iterable[StandMarking] = field(
        default_factory=list,
        metadata={
            "name": "StandMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position_marking: Iterable[TaxiHoldingPositionMarking] = (
        field(
            default_factory=list,
            metadata={
                "name": "TaxiHoldingPositionMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    deicing_area_marking: Iterable[DeicingAreaMarking] = field(
        default_factory=list,
        metadata={
            "name": "DeicingAreaMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line_marking: Iterable[GuidanceLineMarking] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_marking: Iterable[RunwayMarking] = field(
        default_factory=list,
        metadata={
            "name": "RunwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_marking: Iterable[TouchDownLiftOffMarking] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOffMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_protection_area_marking: Iterable[AirportProtectionAreaMarking] = (
        field(
            default_factory=list,
            metadata={
                "name": "AirportProtectionAreaMarking",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    apron_marking: Iterable[ApronMarking] = field(
        default_factory=list,
        metadata={
            "name": "ApronMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_marking: Iterable[TaxiwayMarking] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayMarking",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    approach_lighting_system: Iterable[ApproachLightingSystem] = field(
        default_factory=list,
        metadata={
            "name": "ApproachLightingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
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
        },
    )
    guidance_line_light_system: Iterable[GuidanceLineLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLineLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off_light_system: Iterable[TouchDownLiftOffLightSystem] = (
        field(
            default_factory=list,
            metadata={
                "name": "TouchDownLiftOffLightSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
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
            },
        )
    )
    taxiway_light_system: Iterable[TaxiwayLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_light_system: Iterable[ApronLightSystem] = field(
        default_factory=list,
        metadata={
            "name": "ApronLightSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    visual_glide_slope_indicator: Iterable[VisualGlideSlopeIndicator] = field(
        default_factory=list,
        metadata={
            "name": "VisualGlideSlopeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    touch_down_lift_off: Iterable[TouchDownLiftOff] = field(
        default_factory=list,
        metadata={
            "name": "TouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    passenger_loading_bridge: Iterable[PassengerLoadingBridge] = field(
        default_factory=list,
        metadata={
            "name": "PassengerLoadingBridge",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    deicing_area: Iterable[DeicingArea] = field(
        default_factory=list,
        metadata={
            "name": "DeicingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    road: Iterable[Road] = field(
        default_factory=list,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    aircraft_stand: Iterable[AircraftStand] = field(
        default_factory=list,
        metadata={
            "name": "AircraftStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_element: Iterable[ApronElement] = field(
        default_factory=list,
        metadata={
            "name": "ApronElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron: Iterable[Apron] = field(
        default_factory=list,
        metadata={
            "name": "Apron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    guidance_line: Iterable[GuidanceLine] = field(
        default_factory=list,
        metadata={
            "name": "GuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway_element: Iterable[TaxiwayElement] = field(
        default_factory=list,
        metadata={
            "name": "TaxiwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxiway: Iterable[Taxiway] = field(
        default_factory=list,
        metadata={
            "name": "Taxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    taxi_holding_position: Iterable[TaxiHoldingPosition] = field(
        default_factory=list,
        metadata={
            "name": "TaxiHoldingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_blast_pad: Iterable[RunwayBlastPad] = field(
        default_factory=list,
        metadata={
            "name": "RunwayBlastPad",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_visual_range: Iterable[RunwayVisualRange] = field(
        default_factory=list,
        metadata={
            "name": "RunwayVisualRange",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_element: Iterable[RunwayElement] = field(
        default_factory=list,
        metadata={
            "name": "RunwayElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    arresting_gear: Iterable[ArrestingGear] = field(
        default_factory=list,
        metadata={
            "name": "ArrestingGear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway: Iterable[Runway] = field(
        default_factory=list,
        metadata={
            "name": "Runway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_centreline_point: Iterable[RunwayCentrelinePoint] = field(
        default_factory=list,
        metadata={
            "name": "RunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    runway_direction: Iterable[RunwayDirection] = field(
        default_factory=list,
        metadata={
            "name": "RunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    feature_collection: Iterable[FeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
        },
    )
    directed_observation: Iterable[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    observation: Iterable[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid_coverage: Iterable[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_coverage: Iterable[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_coverage: Iterable[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_coverage: Iterable[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_coverage: Iterable[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_coverage: Iterable[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature_collection: Iterable[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: Iterable[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_topology_complex: Iterable[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_edge: Iterable[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_node: Iterable[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_period: Iterable[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_instant: Iterable[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid: Iterable[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid: Iterable[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geometric_complex: Iterable[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid: Iterable[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface: Iterable[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve: Iterable[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point: Iterable[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_geometry: Iterable[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_solid: Iterable[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    solid: Iterable[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_surface: Iterable[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_surface: Iterable[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_surface: Iterable[ElevatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    surface: Iterable[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tin: Iterable[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    triangulated_surface: Iterable[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polyhedral_surface: Iterable[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_surface: Iterable[Surface1] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Iterable[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_curve: Iterable[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_curve: Iterable[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_curve: Iterable[ElevatedCurve] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedCurve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    curve: Iterable[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    opengis_net_gml_3_2_curve: Iterable[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: Iterable[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_point: Iterable[ElevatedPoint] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    point: Iterable[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    opengis_net_gml_3_2_point: Iterable[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition_proxy: Iterable[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition_collection: Iterable[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_ordinal_reference_system: Iterable[TimeOrdinalReferenceSystem] = (
        field(
            default_factory=list,
            metadata={
                "name": "TimeOrdinalReferenceSystem",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            },
        )
    )
    time_clock: Iterable[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_calendar: Iterable[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_coordinate_system: Iterable[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_reference_system: Iterable[TimeReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter_group: Iterable[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter: Iterable[OperationParameter1] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_method: Iterable[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    concatenated_operation: Iterable[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    transformation: Iterable[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conversion: Iterable[Conversion1] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pass_through_operation: Iterable[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    prime_meridian: Iterable[PrimeMeridian1] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoid: Iterable[Ellipsoid1] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_datum: Iterable[TemporalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_datum: Iterable[VerticalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_datum: Iterable[ImageDatum1] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_datum: Iterable[EngineeringDatum1] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_datum: Iterable[GeodeticDatum1] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    oblique_cartesian_cs: Iterable[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_cs: Iterable[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_cs: Iterable[AffineCs1] = field(
        default_factory=list,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cylindrical_cs: Iterable[CylindricalCs1] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polar_cs: Iterable[PolarCs1] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    spherical_cs: Iterable[SphericalCs1] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    user_defined_cs: Iterable[UserDefinedCs1] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_cs: Iterable[LinearCs1] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_cs: Iterable[TimeCs1] = field(
        default_factory=list,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_cs: Iterable[VerticalCs1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: Iterable[CartesianCs1] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoidal_cs: Iterable[EllipsoidalCs1] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_system_axis: Iterable[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compound_crs: Iterable[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geocentric_crs: Iterable[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: Iterable[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: Iterable[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: Iterable[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: Iterable[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: Iterable[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: Iterable[GeodeticCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: Iterable[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: Iterable[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conventional_unit: Iterable[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_unit: Iterable[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    base_unit: Iterable[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    unit_definition: Iterable[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dictionary: Iterable[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition: Iterable[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
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


@dataclass
class Members(ArrayAssociationType):
    class Meta:
        name = "members"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArrayType(AbstractGmltype):
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class BagType(AbstractGmltype):
    member: Iterable[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class Array(ArrayType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Bag(BagType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
