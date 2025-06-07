from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_primary_radar_type import CodePrimaryRadarType
from pyaixm.generated.code_standby_power_type import CodeStandbyPowerType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.contact_information_property_type import (
    ContactInformationPropertyType,
)
from pyaixm.generated.date_year_type import DateYearType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.primary_surveillance_radar_time_slice_type_extension import (
    PrimarySurveillanceRadarTimeSliceTypeExtension,
)
from pyaixm.generated.surveillance_ground_station_property_type import (
    SurveillanceGroundStationPropertyType,
)
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_magnetic_variation_type import (
    ValMagneticVariationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadarTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    serial_number: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    range: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    range_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "rangeAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    dual_channel: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "dualChannel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    moving_target_indicator: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "movingTargetIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    standby_power: Optional[CodeStandbyPowerType] = field(
        default=None,
        metadata={
            "name": "standbyPower",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    digital: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    military_use_only: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "militaryUseOnly",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    special_use_only: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "specialUseOnly",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    special_aircraft_only: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "specialAircraftOnly",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    magnetic_variation: Optional[ValMagneticVariationType] = field(
        default=None,
        metadata={
            "name": "magneticVariation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    magnetic_variation_accuracy: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "magneticVariationAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    date_magnetic_variation: Optional[DateYearType] = field(
        default=None,
        metadata={
            "name": "dateMagneticVariation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contact: Iterable[ContactInformationPropertyType] = field(
        default_factory=list,
        metadata={
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
    vertical_coverage_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "verticalCoverageAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_coverage_distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "verticalCoverageDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_coverage_azimuth: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "verticalCoverageAzimuth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    antenna_tilt_fixed: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "antennaTiltFixed",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    tilt_angle: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "tiltAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    automated_radar_terminal_system: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "name": "automatedRadarTerminalSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    ground_station: Iterable[SurveillanceGroundStationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "groundStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodePrimaryRadarType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[PrimarySurveillanceRadarTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
