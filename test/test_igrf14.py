# test_declination.py
import datetime

import pyIGRF14 as pyIGRF
import pytest
from dataclasses import dataclass

TEST_FLOAT_PRECISION = 7


@dataclass(frozen=True)
class GeoLocation:
    latitude: float
    longitude: float

    def as_tuple(self) -> tuple[float, float]:
        """Return the latitude and longitude as a tuple.
        # RFC 7946: (longitude, latitude)
        """
        return (
            round(self.longitude, TEST_FLOAT_PRECISION),
            round(self.latitude, TEST_FLOAT_PRECISION),
        )


def decimal_year(dt: datetime.datetime) -> float:
    dt_start = datetime.datetime(
        year=dt.year, month=1, day=1, hour=0, minute=0, second=0
    )
    dt_end = datetime.datetime(
        year=dt.year + 1, month=1, day=1, hour=0, minute=0, second=0
    )
    return round(
        dt.year + (dt - dt_start).total_seconds() / (dt_end - dt_start).total_seconds(),
        ndigits=2,
    )


def get_declination(location: GeoLocation, dt: datetime.datetime) -> float:
    declination, _, _, _, _, _, _ = pyIGRF.igrf_value(
        location.latitude,
        location.longitude,
        alt=0.0,
        year=decimal_year(dt),
    )
    return round(declination, 2)


@pytest.mark.parametrize(
    ("dt", "expected_result"),
    [
        (datetime.datetime(2025, 1, 1), 2025.0),  # Start of year
        (datetime.datetime(2025, 12, 31), 2025.99),  # End of the year
        (datetime.datetime(2025, 7, 2), 2025.5),  # non-leap year
        (datetime.datetime(2024, 7, 2), 2024.503),  # leap year
    ],
)
def test_start_of_year(dt: datetime.datetime, expected_result: float):
    result = decimal_year(dt)
    assert result == pytest.approx(expected_result, rel=1e-5)


class TestGeoLocation:
    def test_valid_coordinates(self):
        lat, long = (45.0, -120.0)
        loc = GeoLocation(latitude=lat, longitude=long)
        assert loc.latitude == lat
        assert loc.longitude == long


LOC_MX = GeoLocation(latitude=20.6296, longitude=-87.0739)  # Playa Del Carmen, QROO, MX
LOC_US = GeoLocation(latitude=29.8269, longitude=-82.5968)  # High Springs, FL, USA
LOC_FR = GeoLocation(latitude=44.2712, longitude=1.451100)  # Émergence du Ressel, FR
LOC_NZ = GeoLocation(latitude=-41.220, longitude=172.7619)  # Pearse Resurgence, NZ


@pytest.mark.parametrize(
    ("dt", "location", "expected_result"),
    [
        (datetime.datetime(2025, 1, 1), LOC_MX, -2.42),
        (datetime.datetime(1990, 7, 1), LOC_MX, 1.65),
        (datetime.datetime(2025, 1, 1), LOC_US, -6.25),
        (datetime.datetime(1990, 7, 1), LOC_US, -2.88),
        (datetime.datetime(2025, 1, 1), LOC_FR, 1.67),
        (datetime.datetime(1990, 7, 1), LOC_FR, -2.88),
        (datetime.datetime(2025, 1, 1), LOC_NZ, 22.83),
        (datetime.datetime(1990, 7, 1), LOC_NZ, 21.44),
    ],
)
def test_declination_calls_pyigrf(
    dt: datetime.datetime, location: GeoLocation, expected_result: float
):
    declination = get_declination(location, dt)
    assert declination == pytest.approx(expected_result, rel=5e-3)
