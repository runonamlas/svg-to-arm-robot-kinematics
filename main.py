import xml.etree.ElementTree as ET
import re
import inside
import numpy as np

dlist = []
svg_file_path = 'e.svg'
coordinatLists = []
t= 100
infill =10

def extract_d_attribute(svg_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = root.findall('.//{http://www.w3.org/2000/svg}path')
        dlist = []
        for path in paths:
            d_attribute = path.get('d')
            dlist.append(d_attribute)
        return dlist
    except Exception as e:
        print('Hata:', str(e))

def parse_coordinates(coord_str):
    if type(coord_str) is str:
        con = coord_str.replace(' ', ',')
        # Koordinatları temizle: Sadece rakamlar, nokta ve virgül kabul edilecek
        cleaned_coord_str = re.sub(r'[^\d.,-]', '', con)

        # Sadece ilk '-' işaretini virgülle değiştir
        cleaned_coord_str = re.sub(r'-(?=\d)', ',-', cleaned_coord_str)
        result = re.sub(r',+', ',', cleaned_coord_str)

        # Virgülle ayrılan koordinatları al
        coordinates = tuple(map(float, filter(None, result.split(','))))
        return coordinates
    else:
        return coord_str

def split_by_letter(text):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pattern = f'(?<=[{letters}])(?=[^a-zA-Z])'
    splits = re.split(pattern, text)
    parsed_data = []
    current_letter = ''
    for split in splits:
        if split[-1] in letters:
            if current_letter:
                if current_letter =="Z" or current_letter =="z" :
                    parsed_data.append((current_letter,(0,0)))
                else:
                    parse = parse_coordinates(split[:len(split)-1])
                    if current_letter == "M" and len(parse) >2:
                        parsed_data.append((current_letter, parse[:2]))
                        parsed_data.append(("L", parse[2:]))
                    elif current_letter == "m" and len(parse) >2:
                        parsed_data.append((current_letter, parse[:2]))
                        parsed_data.append(("l", parse[2:]))
                    else:
                        parsed_data.append((current_letter, split[:len(split)-1]))
            current_letter = split[-1]
        if(split == splits[-1]):
            if current_letter =="Z" or current_letter =="z" :
                parsed_data.append((current_letter,(0,0)))
    return parsed_data

def linear_interpolation(start_coord, end_coord, t):
    x1, y1 = start_coord
    x2, y2 = end_coord
    
    x_step = (x2 - x1) / t
    y_step = (y2 - y1) / t
    
    interpolated_coordinates = [(x1 + i * x_step, y1 + i * y_step) for i in range(t)]
    
    return interpolated_coordinates


def calculate_coordinates_with_h(start_coord, h_value, num_steps):
    x1, y1 = start_coord
    coordinates = []
    increment_per_step = h_value / num_steps
    for i in range(num_steps):
        new_x = x1 + (increment_per_step * (i + 1))
        coordinates.append((new_x, y1))
    return coordinates

def calculate_coordinates_with_v(start_coord, v_value, num_steps):
    x1,y1 = start_coord
    coordinates = []
    increment_per_step = v_value / num_steps
    for i in range(num_steps):
        new_y = y1 + (increment_per_step * (i + 1))
        coordinates.append((x1, new_y))
    return coordinates

def calculate_bezier_curve_points(start_x, start_y, control1_x, control1_y, control2_x, control2_y, end_x, end_y, t):
    # Bezier eğrisinin x ve y değerlerini hesapla
    t_values = np.linspace(0, 1, t)
    x_values = cubic_bezier(t_values, start_x, control1_x, control2_x, end_x)
    y_values = cubic_bezier(t_values, start_y, control1_y, control2_y, end_y)

    # (x, y) çiftlerini içeren bir liste oluştur
    points = [(x, y) for x, y in zip(x_values, y_values)]

    return points

# Bezier eğrisi için cubic_bezier fonksiyonunu tanımla
def cubic_bezier(t, p0, p1, p2, p3):
    return ((1 - t)**3) * p0 + 3 * ((1 - t)**2) * t * p1 + 3 * (1 - t) * (t**2) * p2 + (t**3) * p3


def calculate_q_and_curve_points(p0, p1, p2, num_points=100):
    """
    Quadratic Bezier eğrisi için eğri üzerindeki noktaları döndürür.
    """
    curve_points = []  # Eğri üzerindeki noktalar için liste

    for t in np.linspace(0, 1, num=num_points):
        # Quadratic Bezier eğrisinde q parametreleri hesapla

        # Belirli bir t değeri için eğri üzerindeki noktaların koordinatlarını hesapla
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        curve_points.append((x, y))

    return curve_points

# d niteliklerini al
dlist = extract_d_attribute(svg_file_path)
for d in dlist:
    coordinatList =[]
    parsed_data = split_by_letter(d)
    for lo in parsed_data:
        coordinat = parse_coordinates(lo[1])
        if lo[0] == "M":
            coordinatList.append(coordinat)
        elif lo[0] == "L":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 2):
                    pair = coordinat[i:i+2]
                    returnCoor = linear_interpolation(coordinatList[-1], pair,t)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = linear_interpolation(coordinatList[-1], coordinat,t)
                coordinatList.extend(returnCoor)
        elif lo[0] == "H":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 1):
                    returnCoor = calculate_coordinates_with_h(coordinatList[-1], i[0]-coordinatList[-1][0],t*4)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = calculate_coordinates_with_h(coordinatList[-1], coordinat[0]-coordinatList[-1][0],t*4)
                coordinatList.extend(returnCoor) 
        elif lo[0] == "V":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 1):
                    returnCoor = calculate_coordinates_with_v(coordinatList[-1], i[0]-coordinatList[-1][0],t*4)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = calculate_coordinates_with_v(coordinatList[-1], coordinat[0]-coordinatList[-1][0],t*4)
                coordinatList.extend(returnCoor)
        elif lo[0] == "C":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 6):
                    pair = coordinat[i:i+2]
                    pair2 = coordinat[i+2:i+4]
                    pair3 = coordinat[i+4:i+6]
                    p0 = coordinatList[-1]
                    bezier_points = calculate_bezier_curve_points(p0[0], p0[1], pair[0], pair[1], pair2[0], pair2[1], pair3[0], pair3[1],int(t/2))
                    coordinatList.extend(bezier_points)
            else:
                p0 = (coordinatList[-1])
                p1 = (coordinat[0], coordinat[1])
                p2 = (coordinat[2], coordinat[3])    
                p3 = (coordinat[4], coordinat[5])
                bezier_points = calculate_bezier_curve_points(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],(t/2))
                coordinatList.extend(bezier_points)   
        elif lo[0] == "S":

            pass        
        elif lo[0] == "Q":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 4):
                    pair = coordinat[i:i+2]
                    pair2 = coordinat[i+2:i+4]
                    p0 = coordinatList[-1]
                    curve_points = calculate_q_and_curve_points(p0, pair, pair2,int(t/2))
                    coordinatList.extend(curve_points)
            else:
                p0 = coordinatList[-1]
                curve_points = calculate_q_and_curve_points(p0, pair, pair2,int(t/2))
                coordinatList.extend(curve_points)
        elif lo[0] == "T":

            pass    
        elif lo[0] == "A":

            pass
        elif lo[0] == "m":
            print(coordinat)
            print(coordinatList[-1])
            if len(coordinatList) < 1:
                coordinatList.append(coordinat)
            else:
                coordinatList.append((coordinatList[-1][0] + coordinat[0], coordinatList[-1][1] + coordinat[1]))
        elif lo[0] == "l":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 2):
                    pair = coordinat[i:i+2]
                    returnCoor = linear_interpolation(coordinatList[-1], (coordinatList[-1][0] + pair[0], coordinatList[-1][1] + pair[1]),t)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = linear_interpolation(coordinatList[-1], (coordinatList[-1][0] + coordinat[0], coordinatList[-1][1] + coordinat[1]),t)
                coordinatList.extend(returnCoor)   
        elif lo[0] == "h":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 1):
                    returnCoor = calculate_coordinates_with_h(coordinatList[-1], i[0],t*4)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = calculate_coordinates_with_h(coordinatList[-1], coordinat[0],t*4)
                coordinatList.extend(returnCoor)
        elif lo[0] == "v":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 1):
                    returnCoor = calculate_coordinates_with_v(coordinatList[-1], i[0],t*4)
                    coordinatList.extend(returnCoor)
            else:
                returnCoor = calculate_coordinates_with_v(coordinatList[-1], coordinat[0],t*4)
                coordinatList.extend(returnCoor)
        elif lo[0] == "c":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 6):
                    pair = coordinat[i:i+2]
                    pair2 = coordinat[i+2:i+4]
                    pair3 = coordinat[i+4:i+6]
                    p0 = coordinatList[-1]
                    p1 = (p0[0] + pair[0], p0[1] + pair[1])
                    p2 = (p0[0] + pair2[0], p0[1] + pair2[1])    
                    p3 = (p0[0] + pair3[0], p0[1] + pair3[1])
                    bezier_points = calculate_bezier_curve_points(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],int(t/2))
                    coordinatList.extend(bezier_points)
            else:
                p0 = (coordinatList[-1])
                p1 = (p0[0] + coordinat[0], p0[1] + coordinat[1])
                p2 = (p0[0] + coordinat[2], p0[1] + coordinat[3])    
                p3 = (p0[0] + coordinat[4], p0[1] + coordinat[5])
                bezier_points = calculate_bezier_curve_points(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],int(t/2))
                coordinatList.extend(bezier_points)       
        elif lo[0] == "s":

            pass
        elif lo[0] == "q":
            if(len(coordinat)>2):
                for i in range(0, len(coordinat), 4):
                    pair = coordinat[i:i+2]
                    pair2 = coordinat[i+2:i+4]
                    p0 = coordinatList[-1]
                    p1 = (p0[0]+pair[0],p0[1]+pair[1])
                    p2 = (p0[0]+pair2[0],p0[1]+pair2[1])
                    curve_points = calculate_q_and_curve_points(p0, p1, p2,int(t/2))
                    coordinatList.extend(curve_points)
            else:
                p0 = coordinatList[-1]
                p1 = (p0[0]+coordinat[0][0],p0[1]+coordinat[0][1])
                p2 = (p0[0]+coordinat[1][0],p0[1]+coordinat[1][1])
                curve_points = calculate_q_and_curve_points(p0, p1, p2,int(t/2))
                coordinatList.extend(curve_points)   
        elif lo[0] == "t":

            pass
        elif lo[0] == "a":

            pass
        elif lo[0] == "Z" or lo[0] == "z":
            if coordinat == coordinatList[0]:
                print("here")
            else:
                returnCoor = linear_interpolation(coordinatList[-1],coordinatList[0],t)
                coordinatList.extend(returnCoor)
        else:
            print("Bilinmeten komut: "+ lo[0])
    coordinatLists.extend(coordinatList)
a = inside.scale_polygon(coordinatLists,2)

inside.insidePoints(a,infill)