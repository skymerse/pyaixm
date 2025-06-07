from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_availability_property_type import (
    AirportHeliportAvailabilityPropertyType,
)
from pyaixm.generated.airport_heliport_contamination_property_type import (
    AirportHeliportContaminationPropertyType,
)
from pyaixm.generated.airport_heliport_responsibility_organisation_property_type import (
    AirportHeliportResponsibilityOrganisationPropertyType,
)
from pyaixm.generated.airport_heliport_time_slice_type_extension import (
    AirportHeliportTimeSliceTypeExtension,
)
from pyaixm.generated.altimeter_source_property_type import (
    AltimeterSourcePropertyType,
)
from pyaixm.generated.city_property_type import CityPropertyType
from pyaixm.generated.code_airport_heliport_designator_type import (
    CodeAirportHeliportDesignatorType,
)
from pyaixm.generated.code_airport_heliport_type import CodeAirportHeliportType
from pyaixm.generated.code_iatatype import CodeIatatype
from pyaixm.generated.code_icaotype import CodeIcaotype
from pyaixm.generated.code_military_operations_type import (
    CodeMilitaryOperationsType,
)
from pyaixm.generated.code_vertical_datum_type import CodeVerticalDatumType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.contact_information_property_type import (
    ContactInformationPropertyType,
)
from pyaixm.generated.date_type import DateType
from pyaixm.generated.date_year_type import DateYearType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_fltype import ValFltype
from pyaixm.generated.val_magnetic_variation_change_type import (
    ValMagneticVariationChangeType,
)
from pyaixm.generated.val_magnetic_variation_type import (
    ValMagneticVariationType,
)
from pyaixm.generated.val_temperature_type import ValTemperatureType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[CodeAirportHeliportDesignatorType] = field(
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
    location_indicator_icao: Optional[CodeIcaotype] = field(
        default=None,
        metadata={
            "name": "locationIndicatorICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator_iata: Optional[CodeIatatype] = field(
        default=None,
        metadata={
            "name": "designatorIATA",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeAirportHeliportType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    certified_icao: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "certifiedICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    private_use: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "privateUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    control_type: Optional[CodeMilitaryOperationsType] = field(
        default=None,
        metadata={
            "name": "controlType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    field_elevation: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "fieldElevation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    field_elevation_accuracy: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "fieldElevationAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_datum: Optional[CodeVerticalDatumType] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
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
    magnetic_variation_change: Optional[ValMagneticVariationChangeType] = (
        field(
            default=None,
            metadata={
                "name": "magneticVariationChange",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    reference_temperature: Optional[ValTemperatureType] = field(
        default=None,
        metadata={
            "name": "referenceTemperature",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altimeter_check_location: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "altimeterCheckLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    secondary_power_supply: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "secondaryPowerSupply",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    wind_direction_indicator: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "windDirectionIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    landing_direction_indicator: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "landingDirectionIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    transition_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "transitionAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    transition_level: Optional[ValFltype] = field(
        default=None,
        metadata={
            "name": "transitionLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lowest_temperature: Optional[ValTemperatureType] = field(
        default=None,
        metadata={
            "name": "lowestTemperature",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    abandoned: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    certification_date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "certificationDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    certification_expiration_date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "certificationExpirationDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contaminant: Iterable[AirportHeliportContaminationPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    served_city: Iterable[CityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "servedCity",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    responsible_organisation: Optional[
        AirportHeliportResponsibilityOrganisationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "responsibleOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    arp: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "ARP",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aviation_boundary: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "name": "aviationBoundary",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altimeter_source: Iterable[AltimeterSourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "altimeterSource",
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
    availability: Iterable[AirportHeliportAvailabilityPropertyType] = field(
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
    extension: Iterable[AirportHeliportTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
