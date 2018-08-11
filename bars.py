"""
Задача Бары
===функции===
- самый большой бар;
- самый маленький бар;
- самый близкий бар;

формат json
src->
  features->
    n_элемент_списка->
       geometry->
         coordinates->[долг,шир] 
       properites->
         Attributes->
           "Name"
           "SeatsCount"
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
    data = load_data("bars.json")
    #lon28,lat61
    lat = float(input("Введите широту: ").strip())
    long = float(input("Введите долготу: ").strip())
    
    print("\n:Самый большой бар '{x[1]}' - {x[0]} мест".format(x = get_biggest_bar(data)))
    print(":Самый маленький бар '{x[1]}' - {x[0]} мест".format(x = get_smallest_bar(data)))
    print(":Самый близкий бар {x[1]}".format(x=get_closest_bar(data,long,lat)))