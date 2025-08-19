import pyIGRF14

if __name__ == '__main__':
    lat = 40
    lon = 116
    alt = 300
    date = 2026
    print(pyIGRF14.igrf_value.__doc__)
    print(pyIGRF14.igrf_variation.__doc__)
    print(pyIGRF14.igrf_value(lat, lon, alt, date))
    print(pyIGRF14.igrf_variation(lat, lon, alt, date))
    g, h = pyIGRF14.loadCoeffs.get_coeffs(date)
