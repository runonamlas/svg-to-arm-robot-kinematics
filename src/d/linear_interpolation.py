def main(start_coord, end_coord, t):
    x1, y1 = start_coord
    x2, y2 = end_coord
    
    x_step = (x2 - x1) / t
    y_step = (y2 - y1) / t
    
    interpolated_coordinates = [(x1 + i * x_step, y1 + i * y_step) for i in range(t)]
    
    return interpolated_coordinates