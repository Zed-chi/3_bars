import json
from math import sqrt


def load_data(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            return json.loads(f.read())
    except OSError:
        print("invalid path")


def get_biggest_bar(json_data):
    def get_seat(x):
        return x["properties"]["Attributes"]["SeatsCount"]
    if json_data is not None:
        biggest_bar = max(json_data["features"], key=get_seat)
        bar_name = biggest_bar["properties"]["Attributes"]["Name"]
        seats = biggest_bar["properties"]["Attributes"]["SeatsCount"]
        return [seats, bar_name]


def get_smallest_bar(json_data):
    def get_seat(x):
        return x["properties"]["Attributes"]["SeatsCount"]
    if json_data is not None:
        smallest_bar = min(json_data["features"], key=get_seat)
        bar_name = smallest_bar["properties"]["Attributes"]["Name"]
        seats = smallest_bar["properties"]["Attributes"]["SeatsCount"]
        return [seats, bar_name]


def get_closest_bar(json_data, long, lat):
    def get_length(bar):
        coords = bar["geometry"]["coordinates"]
        length = sqrt(abs(long-coords[0])**2 + abs(lat-coords[1])**2)
        return length
    if json_data is not None and long is not None and lat is not None:
        closest = min(json_data["features"], key=get_length)
        bar_name = closest["properties"]["Attributes"]["Name"]
        return bar_name


if __name__ == '__main__':
    json_data = load_data("bars.json")
    # lon28,lat61
    lat = float(input("Введите широту: ").strip())
    long = float(input("Введите долготу: ").strip())
    big_bar = get_biggest_bar(json_data)
    small_bar = get_smallest_bar(json_data)
    closest_bar = get_closest_bar(json_data, long, lat)
    print("Самый большой бар '{x[1]}' - {x[0]} мест".format(x=big_bar))
    print("Самый маленький бар '{x[1]}' - {x[0]} мест".format(x=small_bar))
    print("Самый близкий бар '{}'".format(closest_bar))
