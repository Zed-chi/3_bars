"""
формат - src->
    features->
        i->
            geometry->
                coordinates->[x,y] 
                type->string
            properites->
                Attributes->
                    "Name"
                    "SeatsCount"
            type->
    type->
"""
import json,math



###funcs###

def load_data(filepath):
    try:
        with open(filepath,"r", encoding='utf-8') as f:
            return json.loads(f.read())
    except:
        print("invalid path")

def get_biggest_bar(data):
    if data is not None:
        biggest = [0,""]
        for i in data["features"]:
            name = i["properties"]["Attributes"]["Name"]
            seats_num = i["properties"]["Attributes"]["SeatsCount"]
            if biggest[0] < seats_num:
                biggest[0] = seats_num
                biggest[1] = name
        return biggest
    
def get_smallest_bar(data):
    if data is not None:
        smallest = []
        for i in data["features"]:
            name = i["properties"]["Attributes"]["Name"]
            seats_num = i["properties"]["Attributes"]["SeatsCount"]
            if len(smallest) == 0:
                smallest.append(seats_num)
                smallest.append(name)
                continue
            if smallest[0] > seats_num :
                smallest[0] = seats_num
                smallest[1] = name
        return smallest

def get_closest_bar(data, long, lat):
    if data!=None and long!=None and lat!=None:
        closest = []
        for i in data["features"]:
            name = i["properties"]["Attributes"]["Name"]
            coords = i["geometry"]["coordinates"]
            length = math.sqrt(abs(long-coords[0])**2 + abs(lat-coords[1])**2)
            if len(closest) == 0:
                closest.append(length)
                closest.append(name)
                continue
            if closest[0] > math.sqrt(abs(long-coords[0])**2 + abs(lat-coords[1])**2) :
                closest[0] = length
                closest[1] = name
        return closest

if __name__ == '__main__':
    data = load_data("1796.json")
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data,37.632015,55.737869))