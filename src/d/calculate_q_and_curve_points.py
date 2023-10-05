import numpy as np


def main(p0, p1, p2, num_points=100):
    """
    Quadratic Bezier eğrisi için eğri üzerindeki noktaları döndürür.
    """
    curve_points = []  # Eğri üzerindeki noktalar için liste

    for t in np.linspace(0, 1, num=num_points):
        # Quadratic Bezier eğrisinde q parametreleri hesapla

        # Belirli bir t değeri için eğri üzerindeki noktaların koordinatlarını hesapla
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        curve_points.append((x, y))

    return curve_points