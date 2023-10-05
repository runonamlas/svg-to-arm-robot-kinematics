import re
from src.svg import parse_coordinates

def main(text):
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
                    parse = parse_coordinates.main(split[:len(split)-1])
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