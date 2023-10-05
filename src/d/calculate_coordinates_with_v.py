def main(start_coord, v_value, num_steps):
    x1,y1 = start_coord
    coordinates = []
    increment_per_step = v_value / num_steps
    for i in range(num_steps):
        new_y = y1 + (increment_per_step * (i + 1))
        coordinates.append((x1, new_y))
    return coordinates