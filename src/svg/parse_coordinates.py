import re

def main(coord_str):
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