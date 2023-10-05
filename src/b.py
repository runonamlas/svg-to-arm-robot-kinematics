import grafik
from shapely.geometry import Polygon

def scale_polygon(polygon, scale_factor):
    scaled_coords = []
    
    for x, y in polygon.exterior.coords:
        scaled_x = x * scale_factor
        scaled_y = y * scale_factor
        scaled_coords.append((scaled_x, scaled_y))
    
    return scaled_coords

# Örnek bir poligon
polygon = Polygon([(0, 0), (0, 5), (5, 5), (5, 0)])

# Poligonu 2 katı büyüt
scaled_polygon = scale_polygon(polygon, 2)

# Sonuçları yazdır
print("Orjinal Poligon:", polygon)
print("Ölçeklendirilmiş Poligon:", scaled_polygon)


# Sonuçları yazdır
grafik.plot_coordinates([(0, 0), (0, 5), (5, 5), (5, 0)])
grafik.plot_coordinates(scaled_polygon)