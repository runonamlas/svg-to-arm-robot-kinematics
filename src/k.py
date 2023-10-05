import numpy as np
import matplotlib.pyplot as plt

# Bezier eğrisini hesapla
def cubic_bezier(t, p0, p1, p2, p3):
    return ((1 - t)**3) * p0 + 3 * ((1 - t)**2) * t * p1 + 3 * (1 - t) * (t**2) * p2 + (t**3) * p3

# Başlangıç ve kontrol noktaları
start_x, start_y = 372.24, -26.36999999999997
control1_x, control1_y = 372.839, 38.234
control2_x, control2_y = 334.596, 0.0
end_x, end_y = 287.428, 0.0

# Parametre değerlerini oluştur
t_values = np.linspace(0, 1, 1000)

# Bezier eğrisini hesapla
x_values = cubic_bezier(t_values, start_x, control1_x, control2_x, end_x)
y_values = cubic_bezier(t_values, start_y, control1_y, control2_y, end_y)

# Bezier eğrisini görselleştir
plt.plot(x_values, y_values, color='blue')  # Eğriyi çiz
plt.gca().invert_yaxis()
plt.scatter([start_x, control1_x, control2_x, end_x], [start_y, control1_y, control2_y, end_y], color='red')  # Kontrol noktalarını göster
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mutlak Bezier Eğrisi')
plt.show()
