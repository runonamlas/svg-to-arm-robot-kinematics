import re
import numpy as np

from src.svg import extract_d_attribute, parse_coordinates, split_by_letter
from src.d import linear_interpolation, calculate_coordinates_with_h, calculate_coordinates_with_v, calculate_bezier_curve_points, calculate_q_and_curve_points
from src.coordinates import calculate_coordinates_with_d
from src import inside

dlist = []
svg_file_path = 'data/e.svg'
coordinatLists = []
t= 100
infill =10

# d niteliklerini al
dlist = extract_d_attribute.main(svg_file_path)
coordinatLists = calculate_coordinates_with_d.main(dlist, t)

a = inside.scale_polygon(coordinatLists,2)

inside.insidePoints(a,infill)