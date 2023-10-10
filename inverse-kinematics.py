import math

def inverse_kinematics(x, y, l1, l2):
    # İkinci açıyı hesapla
    c2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    s2 = math.sqrt(1 - c2**2)
    theta2 = math.atan2(s2, c2)

    # İlk açıyı hesapla
    k1 = l1 + l2 * math.cos(theta2)
    k2 = l2 * math.sin(theta2)
    theta1 = math.atan2(y, x) - math.atan2(k2, k1)

    return theta1, theta2

# Kol uzunlukları
l1 = 50  # Birinci kol uzunluğu (cm)
l2 = 65  # İkinci kol uzunluğu (cm)

# Hedef koordinatları kullanıcıdan alın
x_target = float(30)
y_target = float(40)

movement_duration = 5.0

# Başlangıç konumu (0, 0)
x_start, y_start = 0, 0

# Hedef konumdan başlangıç konumuna gitmek için gerekli açıları hesapla
theta1, theta2 = inverse_kinematics(x_target - x_start, y_target - y_start, l1, l2)

# Hedef konuma gitmek için gerekli açı hızlarını hesapla
theta1_speed = theta1 / movement_duration  # Theta1 açı hızı
theta2_speed = theta2 / movement_duration  # Theta2 açı hızı


# Sonuçları yazdır
print("Hesaplanan Açılar (radyan):")
print("Theta1:", theta1)
print("Theta2:", theta2)

print("\nAçı Hızları (radyan/sn):")
print("Theta1 Hızı:", theta1_speed)
print("Theta2 Hızı:", theta2_speed)