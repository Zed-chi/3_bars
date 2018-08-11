import json
from math import sqrt


def load_data(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            return json.loads(f.read())
    except Exception:
        print("invalid path")


def get_biggest_bar(json_data):
    if json_data is not None:
        biggest = [0, ""]
        for bar in json_data["features"]:
            bar_name = bar["properties"]["Attributes"]["Name"]
            seats_num = bar["properties"]["Attributes"]["SeatsCount"]
            if biggest[0] < seats_num:
                biggest[0] = seats_num
                biggest[1] = bar_name
        return biggest


def get_smallest_bar(json_data):
    if json_data is not None:
        smallest = []
        for bar in json_data["features"]:
            bar_name = bar["properties"]["Attributes"]["Name"]
            seats_num = bar["properties"]["Attributes"]["SeatsCount"]
            if len(smallest) == 0:
                smallest.append(seats_num)
                smallest.append(bar_name)
                continue
            if smallest[0] > seats_num:
                smallest[0] = seats_num
                smallest[1] = bar_name
        return smallest


def get_closest_bar(json_data, long, lat):
    if json_data is not None and long is not None and lat is not None:
        closest = []
        for bar in json_data["features"]:
            bar_name = bar["properties"]["Attributes"]["Name"]
            coords = bar["geometry"]["coordinates"]
            length = sqrt(abs(long-coords[0])**2 + abs(lat-coords[1])**2)
            if len(closest) == 0:
                closest.append(length)
                closest.append(bar_name)
                continue
            if closest[0] > length:
                closest[0] = length
                closest[1] = bar_name
        return closest


if __name__ == '__main__':
    json_data = load_data("bars.json")
    # lon28,lat61
    lat = float(input("Введите широту: ").strip())
    long = float(input("Введите долготу: ").strip())
    big_bar = get_biggest_bar(json_data)
    small_bar = get_smallest_bar(json_data)
    closest_bar = get_closest_bar(json_data, long, lat)[1]
    print("Самый большой бар '{x[1]}' - {x[0]} мест".format(big_bar))
    print("Самый маленький бар '{x[1]}' - {x[0]} мест".format(small_bar))
    print("Самый близкий бар {x[1]}".format(closest_bar))
