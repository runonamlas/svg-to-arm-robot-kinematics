import xml.etree.ElementTree as ET

def main(svg_path):
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