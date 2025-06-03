from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.authority_for_navaid_equipment_property_type import (
    AuthorityForNavaidEquipmentPropertyType,
)
from generated.code_navaid_designator_type import CodeNavaidDesignatorType
from generated.code_radio_emission_type import CodeRadioEmissionType
from generated.code_yes_no_type import CodeYesNoType
from generated.date_year_type import DateYearType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.navaid_equipment_monitoring_property_type import (
    NavaidEquipmentMonitoringPropertyType,
)
from generated.navaid_operational_status_property_type import (
    NavaidOperationalStatusPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.sdftime_slice_type_extension import SdftimeSliceTypeExtension
from generated.text_name_type import TextNameType
from generated.val_angle_type import ValAngleType
from generated.val_bearing_type import ValBearingType
from generated.val_frequency_type import ValFrequencyType
from generated.val_magnetic_variation_type import ValMagneticVariationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SdftimeSliceType(AbstractAixmtimeSliceType):
    class Meta:
        name = "SDFTimeSliceType"

    designator: Optional[CodeNavaidDesignatorType] = field(
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
    emission_class: Optional[CodeRadioEmissionType] = field(
        default=None,
        metadata={
            "name": "emissionClass",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    mobile: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
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
    flight_checked: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flightChecked",
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
    authority: Iterable[AuthorityForNavaidEquipmentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    monitoring: Iterable[NavaidEquipmentMonitoringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[NavaidOperationalStatusPropertyType] = field(
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
    frequency: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    magnetic_bearing: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "magneticBearing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    true_bearing: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "trueBearing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[SdftimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
