def main(start_coord, h_value, num_steps):
    x1, y1 = start_coord
    coordinates = []
    increment_per_step = h_value / num_steps
    for i in range(num_steps):
        new_x = x1 + (increment_per_step * (i + 1))
        coordinates.append((new_x, y1))
    return coordinates