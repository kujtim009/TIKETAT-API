from cordinates import cordinates


line = "cordinates = ["
sitCount = 25
for cordinate in cordinates:
    # print("regionId:{}".format(cordinate['regionId']))
     
    
    if cordinate['regionId'] == "P103":
        sitID = sitCount  
        line += "{{'regionId': '{}', 'rowID': '{}', 'sitId': {}, 'cords': {}}}\n".format(cordinate['regionId'], cordinate['rowID'], sitID, cordinate['cords'])
        sitCount -= 1
        if sitCount <= 0:
            sitCount = 25
    else:
        sitID = cordinate['sitId'] 
        line += "{{'regionId': '{}', 'rowID': '{}', 'sitId': {}, 'cords': {}}}\n".format(cordinate['regionId'], cordinate['rowID'], sitID, cordinate['cords'],)

line = line + "]"
with open("cordinates2.py","w+") as f:
    f.write(line)