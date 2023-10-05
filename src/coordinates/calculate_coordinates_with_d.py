from src.svg import extract_d_attribute, parse_coordinates, split_by_letter
from src.d import linear_interpolation, calculate_coordinates_with_h, calculate_coordinates_with_v, calculate_bezier_curve_points, calculate_q_and_curve_points

def main(dlist, t):
    coordinatLists = []
    for d in dlist:
      coordinatList=[]
      parsed_data = split_by_letter.main(d)
      for lo in parsed_data:
        coordinat = parse_coordinates.main(lo[1])
        if lo[0] == "M":
          coordinatList.append(coordinat)
        elif lo[0] == "L":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 2):
              pair = coordinat[i:i+2]
              returnCoor = linear_interpolation.main(coordinatList[-1], pair,t)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = linear_interpolation.main(coordinatList[-1], coordinat,t)
            coordinatList.extend(returnCoor)
        elif lo[0] == "H":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 1):
              returnCoor = calculate_coordinates_with_h.main(coordinatList[-1], i[0]-coordinatList[-1][0],t*4)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = calculate_coordinates_with_h.main(coordinatList[-1], coordinat[0]-coordinatList[-1][0],t*4)
            coordinatList.extend(returnCoor) 
        elif lo[0] == "V":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 1):
              returnCoor = calculate_coordinates_with_v.main(coordinatList[-1], i[0]-coordinatList[-1][0],t*4)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = calculate_coordinates_with_v.main(coordinatList[-1], coordinat[0]-coordinatList[-1][0],t*4)
            coordinatList.extend(returnCoor)
        elif lo[0] == "C":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 6):
              pair = coordinat[i:i+2]
              pair2 = coordinat[i+2:i+4]
              pair3 = coordinat[i+4:i+6]
              p0 = coordinatList[-1]
              bezier_points = calculate_bezier_curve_points.main(p0[0], p0[1], pair[0], pair[1], pair2[0], pair2[1], pair3[0], pair3[1],int(t/2))
              coordinatList.extend(bezier_points)
          else:
            p0 = (coordinatList[-1])
            p1 = (coordinat[0], coordinat[1])
            p2 = (coordinat[2], coordinat[3])    
            p3 = (coordinat[4], coordinat[5])
            bezier_points = calculate_bezier_curve_points.main(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],(t/2))
            coordinatList.extend(bezier_points)   
        elif lo[0] == "S":

          pass        
        elif lo[0] == "Q":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 4):
              pair = coordinat[i:i+2]
              pair2 = coordinat[i+2:i+4]
              p0 = coordinatList[-1]
              curve_points = calculate_q_and_curve_points.main(p0, pair, pair2,int(t/2))
              coordinatList.extend(curve_points)
          else:
            p0 = coordinatList[-1]
            curve_points = calculate_q_and_curve_points.main(p0, pair, pair2,int(t/2))
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
              returnCoor = linear_interpolation.main(coordinatList[-1], (coordinatList[-1][0] + pair[0], coordinatList[-1][1] + pair[1]),t)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = linear_interpolation.main(coordinatList[-1], (coordinatList[-1][0] + coordinat[0], coordinatList[-1][1] + coordinat[1]),t)
            coordinatList.extend(returnCoor)   
        elif lo[0] == "h":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 1):
              returnCoor = calculate_coordinates_with_h.main(coordinatList[-1], i[0],t*4)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = calculate_coordinates_with_h.main(coordinatList[-1], coordinat[0],t*4)
            coordinatList.extend(returnCoor)
        elif lo[0] == "v":
          if(len(coordinat)>2):
            for i in range(0, len(coordinat), 1):
              returnCoor = calculate_coordinates_with_v.main(coordinatList[-1], i[0],t*4)
              coordinatList.extend(returnCoor)
          else:
            returnCoor = calculate_coordinates_with_v.main(coordinatList[-1], coordinat[0],t*4)
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
              bezier_points = calculate_bezier_curve_points.main(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],int(t/2))
              coordinatList.extend(bezier_points)
          else:
            p0 = (coordinatList[-1])
            p1 = (p0[0] + coordinat[0], p0[1] + coordinat[1])
            p2 = (p0[0] + coordinat[2], p0[1] + coordinat[3])    
            p3 = (p0[0] + coordinat[4], p0[1] + coordinat[5])
            bezier_points = calculate_bezier_curve_points.main(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],int(t/2))
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
              curve_points = calculate_q_and_curve_points.main(p0, p1, p2,int(t/2))
              coordinatList.extend(curve_points)
          else:
            p0 = coordinatList[-1]
            p1 = (p0[0]+coordinat[0][0],p0[1]+coordinat[0][1])
            p2 = (p0[0]+coordinat[1][0],p0[1]+coordinat[1][1])
            curve_points = calculate_q_and_curve_points.main(p0, p1, p2,int(t/2))
            coordinatList.extend(curve_points)   
        elif lo[0] == "t":

          pass
        elif lo[0] == "a":

          pass
        elif lo[0] == "Z" or lo[0] == "z":
          if coordinat == coordinatList[0]:
            print("here")
          else:
            returnCoor = linear_interpolation.main(coordinatList[-1],coordinatList[0],t)
            coordinatList.extend(returnCoor)
        else:
          print("Bilinmeten komut: "+ lo[0])
      coordinatLists.extend(coordinatList)

    return coordinatLists