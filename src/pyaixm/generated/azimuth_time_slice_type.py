from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.authority_for_navaid_equipment_property_type import (
    AuthorityForNavaidEquipmentPropertyType,
)
from pyaixm.generated.azimuth_time_slice_type_extension import (
    AzimuthTimeSliceTypeExtension,
)
from pyaixm.generated.code_mlsazimuth_type import CodeMlsazimuthType
from pyaixm.generated.code_mlschannel_type import CodeMlschannelType
from pyaixm.generated.code_navaid_designator_type import (
    CodeNavaidDesignatorType,
)
from pyaixm.generated.code_radio_emission_type import CodeRadioEmissionType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.date_year_type import DateYearType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.navaid_equipment_monitoring_property_type import (
    NavaidEquipmentMonitoringPropertyType,
)
from pyaixm.generated.navaid_operational_status_property_type import (
    NavaidOperationalStatusPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_magnetic_variation_type import (
    ValMagneticVariationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AzimuthTimeSliceType(AbstractAixmtimeSliceType):
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
    type_value: Optional[CodeMlsazimuthType] = field(
        default=None,
        metadata={
            "name": "type",
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
    true_bearing_accuracy: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "trueBearingAccuracy",
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
    angle_proportional_left: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "angleProportionalLeft",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_proportional_right: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "angleProportionalRight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_cover_left: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "angleCoverLeft",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_cover_right: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "angleCoverRight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    channel: Optional[CodeMlschannelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AzimuthTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
