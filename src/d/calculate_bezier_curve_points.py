import numpy as np

# Bezier eğrisi için cubic_bezier fonksiyonunu tanımla
def cubic_bezier(t, p0, p1, p2, p3):
    return ((1 - t)**3) * p0 + 3 * ((1 - t)**2) * t * p1 + 3 * (1 - t) * (t**2) * p2 + (t**3) * p3

def main(start_x, start_y, control1_x, control1_y, control2_x, control2_y, end_x, end_y, t):
    # Bezier eğrisinin x ve y değerlerini hesapla
    t_values = np.linspace(0, 1, t)
    x_values = cubic_bezier(t_values, start_x, control1_x, control2_x, end_x)
    y_values = cubic_bezier(t_values, start_y, control1_y, control2_y, end_y)

    # (x, y) çiftlerini içeren bir liste oluştur
    points = [(x, y) for x, y in zip(x_values, y_values)]

    return points
