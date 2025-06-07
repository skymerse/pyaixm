from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.authority_for_navaid_equipment_property_type import (
    AuthorityForNavaidEquipmentPropertyType,
)
from pyaixm.generated.code_dmechannel_type import CodeDmechannelType
from pyaixm.generated.code_dmetype import CodeDmetype
from pyaixm.generated.code_navaid_designator_type import (
    CodeNavaidDesignatorType,
)
from pyaixm.generated.code_radio_emission_type import CodeRadioEmissionType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.date_year_type import DateYearType
from pyaixm.generated.dmetime_slice_type_extension import (
    DmetimeSliceTypeExtension,
)
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
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_frequency_type import ValFrequencyType
from pyaixm.generated.val_magnetic_variation_type import (
    ValMagneticVariationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DmetimeSliceType(AbstractAixmtimeSliceType):
    class Meta:
        name = "DMETimeSliceType"

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
    type_value: Optional[CodeDmetype] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    channel: Optional[CodeDmechannelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    ghost_frequency: Optional[ValFrequencyType] = field(
        default=None,
        metadata={
            "name": "ghostFrequency",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    displace: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[DmetimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
