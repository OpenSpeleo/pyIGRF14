from __future__ import annotations


from pathlib import Path


def load_coeffs(filepath: Path):
    """
    load igrf12 coeffs from file
    :param filename: file which save coeffs (str)
    :return: g and h list one by one (list(float))
    """
    gh = []
    gh2arr = []
    with filepath.open(mode="r") as f:
        text = f.readlines()
        for a in text:
            if a[:2] == "g " or a[:2] == "h ":
                b = a.split()[3:]
                b = [float(x) for x in b]
                gh2arr.append(b)
        gh2arr = [list(row) for row in zip(*gh2arr)]
        N = len(gh2arr)
        for i in range(N):
            if i < 19:
                for j in range(120):
                    gh.append(gh2arr[i][j])
            else:
                for p in gh2arr[i]:
                    gh.append(p)
        gh.append(0)
    return gh


IGRF_COEFFS = load_coeffs(Path(__file__).parent / "src/igrf14coeffs.txt")


def get_coeffs(date):
    """
    :param date: float
    :return: list: g, list: h
    """
    if date < 1900.0 or date > 2035.0:
        print("This subroutine will not work with a date of " + str(date))
        print("Date must be in the range 1900.0 <= date <= 2035.0")
        print("On return [], []")
        return [], []
    elif date >= 2025.0:
        if date > 2030.0:
            # not adapt for the model but can calculate
            print("This version of the IGRF is intended for use up to 2025.0.")
            print(
                "values for "
                + str(date)
                + " will be computed but may be of reduced accuracy"
            )
        t = date - 2025.0
        tc = 1.0
        #     pointer for last coefficient in pen-ultimate set of MF coefficients...
        ll = 3060 + 195 + 195
        nmx = 13
        nc = nmx * (nmx + 2)
    else:
        t = 0.2 * (date - 1900.0)
        ll = int(t)
        t = t - ll
        #     SH models before 1995.0 are only to degree 10
        if date < 1995.0:
            nmx = 10
            nc = nmx * (nmx + 2)
            ll = nc * ll
        else:
            nmx = 13
            nc = nmx * (nmx + 2)
            ll = int(0.2 * (date - 1995.0))
            #     19 is the number of SH models that extend to degree 10
            ll = 120 * 19 + nc * ll
        tc = 1.0 - t
    # print(tc, t)
    g, h = [], []
    temp = ll - 1
    for n in range(nmx + 1):
        g.append([])
        h.append([])
        if n == 0:
            g[0].append(None)
        for m in range(n + 1):
            if m != 0:
                g[n].append(tc * IGRF_COEFFS[temp] + t * IGRF_COEFFS[temp + nc])
                h[n].append(tc * IGRF_COEFFS[temp + 1] + t * IGRF_COEFFS[temp + nc + 1])
                temp += 2
                # print(n, m, g[n][m], h[n][m])
            else:
                g[n].append(tc * IGRF_COEFFS[temp] + t * IGRF_COEFFS[temp + nc])
                h[n].append(None)
                temp += 1
                # print(n, m, g[n][m], h[n][m])
    return g, h
