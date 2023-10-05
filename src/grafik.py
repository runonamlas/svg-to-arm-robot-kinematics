import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    # x ve y değerlerini çıkar
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # Grafik oluşturma
    plt.figure()
    plt.scatter(x_values,y_values)  # x ve y değerlerini scatter plot ile gösterme
    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Koordinat Sistemi')
    plt.grid(True)  # Izgara ekleme
    plt.axis('equal')
    plt.gca().invert_yaxis()
    plt.show()

# Koordinatları göster
#plot_coordinates(coordinates)
