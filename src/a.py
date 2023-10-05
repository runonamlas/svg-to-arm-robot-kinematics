import re
import matplotlib.pyplot as plt
def parse_svg_path_d(path_d):
    commands = []
    current_x, current_y = 0, 0  # Başlangıç koordinatları
    
    # Regular expression to extract command and coordinates
    pattern = r'([MmLl])\s*([\d.-]+)\s*([\d.-]+)'
    matches = re.findall(pattern, path_d)
    
    for match in matches:
        command, x, y = match
        x, y = float(x), float(y)
        
        if command == 'M':
            current_x, current_y = x, y
        elif command == 'm':
            current_x, current_y = current_x + x, current_y + y
        elif command == 'L':
            commands.append((current_x, current_y, x, y))
            current_x, current_y = x, y
        elif command == 'l':
            commands.append((current_x, current_y, current_x + x, current_y + y))
            current_x, current_y = current_x + x, current_y + y
    
    return commands

# Örnek SVG path d değeri
svg_path_d = "M100,200 L200,200 L200,300 L100,300 Z"

# SVG path d değerini analiz et
parsed_commands = parse_svg_path_d(svg_path_d)

# Poligonu oluştur
polygon = []
for command in parsed_commands:
    polygon.extend([(command[0], command[1]), (command[2], command[3])])

print("Polygon vertices:", polygon)
x_coords, y_coords = zip(*polygon)
plt.scatter(x_coords, y_coords, color='blue', label='Inner Points')
plt.plot(*polygon, color='red', label='Polygon')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Inner Points Inside Polygon')
plt.show()
