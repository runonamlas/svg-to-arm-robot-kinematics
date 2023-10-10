import math

def calculate_coordinates(theta1, theta2, l1, l2):
    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)
    return x, y

# Kol uzunlukları
l1 = 50  # Birinci kol uzunluğu (cm)
l2 = 65  # İkinci kol uzunluğu (cm)

# Kullanıcıdan theta1 ve theta2'yi alın
theta1 = 0.9272952180016122
theta2 = 2.342464091452323

# Koordinatları hesapla
x, y = calculate_coordinates(theta1, theta2, l1, l2)

# Sonuçları yazdır
print("Hesaplanan Koordinatlar:")
print("X:", x)
print("Y:", y)