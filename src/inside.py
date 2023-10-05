import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point

# Kenarları birleştirerek poligon oluştur
def insidePoints(coord, step_size):
    polygon = Polygon(coord)

    # En küçük ve en büyük x, y değerlerini al
    min_x, min_y = np.min(coord, axis=0)
    max_x, max_y = np.max(coord, axis=0)
    print(min_x,min_y)
    print(max_x,max_y)

    # İçerideki noktaları oluştur
    inner_points = []

    # X ve Y eksenlerinde belirli adımlarla iç kısıma doğru giderek noktaları yerleştir
    for x in np.arange(min_x, max_x, step_size):
        for y in np.arange(min_y, max_y, step_size):
            point = Point(x, y)

            # Eğer nokta poligonun içindeyse, listeye ekle
            if polygon.contains(point):
                inner_points.append((x, y))
    
    x_coords, y_coords = zip(*inner_points)
    plt.scatter(x_coords, y_coords, color='blue', label='Inner Points')
    plt.plot(*polygon.exterior.xy, color='red', label='Polygon')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Inner Points Inside Polygon')
    plt.show()

    return inner_points

def scale_polygon(polygon, scale_factor):
    scaled_coords = []
    
    for x, y in polygon:
        scaled_x = x * scale_factor
        scaled_y = y * scale_factor
        scaled_coords.append((scaled_x, scaled_y))
    
    return scaled_coords