from dataclasses import dataclass

from generated.airport_sign_time_slice_type import AirportSignTimeSliceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportSignTimeSlice(AirportSignTimeSliceType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
