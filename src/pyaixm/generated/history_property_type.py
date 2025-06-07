from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.aerial_refuelling_time_slice import (
    AerialRefuellingTimeSlice,
)
from pyaixm.generated.aeronautical_ground_light_time_slice import (
    AeronauticalGroundLightTimeSlice,
)
from pyaixm.generated.air_traffic_control_service_time_slice import (
    AirTrafficControlServiceTimeSlice,
)
from pyaixm.generated.air_traffic_management_service_time_slice import (
    AirTrafficManagementServiceTimeSlice,
)
from pyaixm.generated.aircraft_ground_service_time_slice import (
    AircraftGroundServiceTimeSlice,
)
from pyaixm.generated.aircraft_stand_time_slice import AircraftStandTimeSlice
from pyaixm.generated.airport_clearance_service_time_slice import (
    AirportClearanceServiceTimeSlice,
)
from pyaixm.generated.airport_heliport_collocation_time_slice import (
    AirportHeliportCollocationTimeSlice,
)
from pyaixm.generated.airport_heliport_time_slice import (
    AirportHeliportTimeSlice,
)
from pyaixm.generated.airport_hot_spot_time_slice import (
    AirportHotSpotTimeSlice,
)
from pyaixm.generated.airport_protection_area_marking_time_slice import (
    AirportProtectionAreaMarkingTimeSlice,
)
from pyaixm.generated.airport_sign_time_slice import AirportSignTimeSlice
from pyaixm.generated.airport_supplies_service_time_slice import (
    AirportSuppliesServiceTimeSlice,
)
from pyaixm.generated.airspace_border_crossing_time_slice import (
    AirspaceBorderCrossingTimeSlice,
)
from pyaixm.generated.airspace_time_slice import AirspaceTimeSlice
from pyaixm.generated.altimeter_source_time_slice import (
    AltimeterSourceTimeSlice,
)
from pyaixm.generated.angle_indication_time_slice import (
    AngleIndicationTimeSlice,
)
from pyaixm.generated.approach_lighting_system_time_slice import (
    ApproachLightingSystemTimeSlice,
)
from pyaixm.generated.apron_element_time_slice import ApronElementTimeSlice
from pyaixm.generated.apron_light_system_time_slice import (
    ApronLightSystemTimeSlice,
)
from pyaixm.generated.apron_marking_time_slice import ApronMarkingTimeSlice
from pyaixm.generated.apron_time_slice import ApronTimeSlice
from pyaixm.generated.arresting_gear_time_slice import ArrestingGearTimeSlice
from pyaixm.generated.arrival_feeder_leg_time_slice import (
    ArrivalFeederLegTimeSlice,
)
from pyaixm.generated.arrival_leg_time_slice import ArrivalLegTimeSlice
from pyaixm.generated.authority_for_airspace_time_slice import (
    AuthorityForAirspaceTimeSlice,
)
from pyaixm.generated.azimuth_time_slice import AzimuthTimeSlice
from pyaixm.generated.change_over_point_time_slice import (
    ChangeOverPointTimeSlice,
)
from pyaixm.generated.checkpoint_instime_slice import CheckpointInstimeSlice
from pyaixm.generated.checkpoint_vortime_slice import CheckpointVortimeSlice
from pyaixm.generated.circling_area_time_slice import CirclingAreaTimeSlice
from pyaixm.generated.deicing_area_marking_time_slice import (
    DeicingAreaMarkingTimeSlice,
)
from pyaixm.generated.deicing_area_time_slice import DeicingAreaTimeSlice
from pyaixm.generated.departure_leg_time_slice import DepartureLegTimeSlice
from pyaixm.generated.designated_point_time_slice import (
    DesignatedPointTimeSlice,
)
from pyaixm.generated.direction_finder_time_slice import (
    DirectionFinderTimeSlice,
)
from pyaixm.generated.distance_indication_time_slice import (
    DistanceIndicationTimeSlice,
)
from pyaixm.generated.dmetime_slice import DmetimeSlice
from pyaixm.generated.elevation_time_slice import ElevationTimeSlice
from pyaixm.generated.event_time_slice import EventTimeSlice
from pyaixm.generated.final_leg_time_slice import FinalLegTimeSlice
from pyaixm.generated.fire_fighting_service_time_slice import (
    FireFightingServiceTimeSlice,
)
from pyaixm.generated.flight_restriction_time_slice import (
    FlightRestrictionTimeSlice,
)
from pyaixm.generated.floating_dock_site_time_slice import (
    FloatingDockSiteTimeSlice,
)
from pyaixm.generated.geo_border_time_slice import GeoBorderTimeSlice
from pyaixm.generated.glidepath_time_slice import GlidepathTimeSlice
from pyaixm.generated.ground_traffic_control_service_time_slice import (
    GroundTrafficControlServiceTimeSlice,
)
from pyaixm.generated.guidance_line_light_system_time_slice import (
    GuidanceLineLightSystemTimeSlice,
)
from pyaixm.generated.guidance_line_marking_time_slice import (
    GuidanceLineMarkingTimeSlice,
)
from pyaixm.generated.guidance_line_time_slice import GuidanceLineTimeSlice
from pyaixm.generated.holding_assessment_time_slice import (
    HoldingAssessmentTimeSlice,
)
from pyaixm.generated.holding_pattern_time_slice import HoldingPatternTimeSlice
from pyaixm.generated.information_service_time_slice import (
    InformationServiceTimeSlice,
)
from pyaixm.generated.initial_leg_time_slice import InitialLegTimeSlice
from pyaixm.generated.instrument_approach_procedure_time_slice import (
    InstrumentApproachProcedureTimeSlice,
)
from pyaixm.generated.intermediate_leg_time_slice import (
    IntermediateLegTimeSlice,
)
from pyaixm.generated.localizer_time_slice import LocalizerTimeSlice
from pyaixm.generated.marker_beacon_time_slice import MarkerBeaconTimeSlice
from pyaixm.generated.marking_buoy_time_slice import MarkingBuoyTimeSlice
from pyaixm.generated.missed_approach_leg_time_slice import (
    MissedApproachLegTimeSlice,
)
from pyaixm.generated.moving_object_status import MovingObjectStatus
from pyaixm.generated.navaid_time_slice import NavaidTimeSlice
from pyaixm.generated.navigation_area_restriction_time_slice import (
    NavigationAreaRestrictionTimeSlice,
)
from pyaixm.generated.navigation_area_time_slice import NavigationAreaTimeSlice
from pyaixm.generated.ndbtime_slice import NdbtimeSlice
from pyaixm.generated.non_movement_area_time_slice import (
    NonMovementAreaTimeSlice,
)
from pyaixm.generated.obstacle_area_time_slice import ObstacleAreaTimeSlice
from pyaixm.generated.organisation_authority_time_slice import (
    OrganisationAuthorityTimeSlice,
)
from pyaixm.generated.passenger_loading_bridge_time_slice import (
    PassengerLoadingBridgeTimeSlice,
)
from pyaixm.generated.passenger_service_time_slice import (
    PassengerServiceTimeSlice,
)
from pyaixm.generated.pilot_controlled_lighting_time_slice import (
    PilotControlledLightingTimeSlice,
)
from pyaixm.generated.precision_approach_radar_time_slice import (
    PrecisionApproachRadarTimeSlice,
)
from pyaixm.generated.primary_surveillance_radar_time_slice import (
    PrimarySurveillanceRadarTimeSlice,
)
from pyaixm.generated.procedure_dmetime_slice import ProcedureDmetimeSlice
from pyaixm.generated.radar_system_time_slice import RadarSystemTimeSlice
from pyaixm.generated.radio_communication_channel_time_slice import (
    RadioCommunicationChannelTimeSlice,
)
from pyaixm.generated.radio_frequency_area_time_slice import (
    RadioFrequencyAreaTimeSlice,
)
from pyaixm.generated.road_time_slice import RoadTimeSlice
from pyaixm.generated.route_dmetime_slice import RouteDmetimeSlice
from pyaixm.generated.route_segment_time_slice import RouteSegmentTimeSlice
from pyaixm.generated.route_time_slice import RouteTimeSlice
from pyaixm.generated.rules_procedures_time_slice import (
    RulesProceduresTimeSlice,
)
from pyaixm.generated.runway_blast_pad_time_slice import (
    RunwayBlastPadTimeSlice,
)
from pyaixm.generated.runway_centreline_point_time_slice import (
    RunwayCentrelinePointTimeSlice,
)
from pyaixm.generated.runway_direction_light_system_time_slice import (
    RunwayDirectionLightSystemTimeSlice,
)
from pyaixm.generated.runway_direction_time_slice import (
    RunwayDirectionTimeSlice,
)
from pyaixm.generated.runway_element_time_slice import RunwayElementTimeSlice
from pyaixm.generated.runway_marking_time_slice import RunwayMarkingTimeSlice
from pyaixm.generated.runway_protect_area_light_system_time_slice import (
    RunwayProtectAreaLightSystemTimeSlice,
)
from pyaixm.generated.runway_protect_area_time_slice import (
    RunwayProtectAreaTimeSlice,
)
from pyaixm.generated.runway_time_slice import RunwayTimeSlice
from pyaixm.generated.runway_visual_range_time_slice import (
    RunwayVisualRangeTimeSlice,
)
from pyaixm.generated.safe_altitude_area_time_slice import (
    SafeAltitudeAreaTimeSlice,
)
from pyaixm.generated.sdftime_slice import SdftimeSlice
from pyaixm.generated.seaplane_landing_area_time_slice import (
    SeaplaneLandingAreaTimeSlice,
)
from pyaixm.generated.seaplane_ramp_site_time_slice import (
    SeaplaneRampSiteTimeSlice,
)
from pyaixm.generated.search_rescue_service_time_slice import (
    SearchRescueServiceTimeSlice,
)
from pyaixm.generated.secondary_surveillance_radar_time_slice import (
    SecondarySurveillanceRadarTimeSlice,
)
from pyaixm.generated.significant_point_in_airspace_time_slice import (
    SignificantPointInAirspaceTimeSlice,
)
from pyaixm.generated.special_date_time_slice import SpecialDateTimeSlice
from pyaixm.generated.special_navigation_station_time_slice import (
    SpecialNavigationStationTimeSlice,
)
from pyaixm.generated.special_navigation_system_time_slice import (
    SpecialNavigationSystemTimeSlice,
)
from pyaixm.generated.stand_marking_time_slice import StandMarkingTimeSlice
from pyaixm.generated.standard_instrument_arrival_time_slice import (
    StandardInstrumentArrivalTimeSlice,
)
from pyaixm.generated.standard_instrument_departure_time_slice import (
    StandardInstrumentDepartureTimeSlice,
)
from pyaixm.generated.standard_level_column_time_slice import (
    StandardLevelColumnTimeSlice,
)
from pyaixm.generated.standard_level_sector_time_slice import (
    StandardLevelSectorTimeSlice,
)
from pyaixm.generated.standard_level_table_time_slice import (
    StandardLevelTableTimeSlice,
)
from pyaixm.generated.survey_control_point_time_slice import (
    SurveyControlPointTimeSlice,
)
from pyaixm.generated.tacantime_slice import TacantimeSlice
from pyaixm.generated.taxi_holding_position_light_system_time_slice import (
    TaxiHoldingPositionLightSystemTimeSlice,
)
from pyaixm.generated.taxi_holding_position_marking_time_slice import (
    TaxiHoldingPositionMarkingTimeSlice,
)
from pyaixm.generated.taxi_holding_position_time_slice import (
    TaxiHoldingPositionTimeSlice,
)
from pyaixm.generated.taxiway_element_time_slice import TaxiwayElementTimeSlice
from pyaixm.generated.taxiway_light_system_time_slice import (
    TaxiwayLightSystemTimeSlice,
)
from pyaixm.generated.taxiway_marking_time_slice import TaxiwayMarkingTimeSlice
from pyaixm.generated.taxiway_time_slice import TaxiwayTimeSlice
from pyaixm.generated.terminal_arrival_area_time_slice import (
    TerminalArrivalAreaTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_light_system_time_slice import (
    TouchDownLiftOffLightSystemTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_marking_time_slice import (
    TouchDownLiftOffMarkingTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_safe_area_time_slice import (
    TouchDownLiftOffSafeAreaTimeSlice,
)
from pyaixm.generated.touch_down_lift_off_time_slice import (
    TouchDownLiftOffTimeSlice,
)
from pyaixm.generated.unit_time_slice import UnitTimeSlice
from pyaixm.generated.unplanned_holding_time_slice import (
    UnplannedHoldingTimeSlice,
)
from pyaixm.generated.vertical_structure_time_slice import (
    VerticalStructureTimeSlice,
)
from pyaixm.generated.visual_glide_slope_indicator_time_slice import (
    VisualGlideSlopeIndicatorTimeSlice,
)
from pyaixm.generated.vortime_slice import VortimeSlice
from pyaixm.generated.wind_direction_indicator_time_slice import (
    WindDirectionIndicatorTimeSlice,
)
from pyaixm.generated.work_area_time_slice import WorkAreaTimeSlice

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class HistoryPropertyType:
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
