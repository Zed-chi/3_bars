import json
import sys
from math import sqrt


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_seats(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_coords():
    try:
        lat = float(input("Введите широту: ").strip())
        long = float(input("Введите долготу: ").strip())
        return lat, long
    except ValueError:
        return None, None


def get_distance(long, lat, bar):
    return sqrt(
        abs(long-bar["geometry"]["coordinates"][0])**2
        + abs(lat-bar["geometry"]["coordinates"][1])**2)


def load_data(path_to_json):
    try:
        with open(path_to_json, "r", encoding="utf-8") as json_file:
            return json.loads(json_file.read())["features"]
    except ValueError:
        return None


def get_biggest_bar(bars_list):
    if bars_list is not None:
        biggest_bar = max(bars_list, key=get_seats)
        return biggest_bar


def get_smallest_bar(bars_list):
    if bars_list is not None:
        smallest_bar = min(bars_list, key=get_seats)
        return smallest_bar


def get_closest_bar(bars_list, long, lat):
    if bars_list is not None:
        closest = min(bars_list, key=lambda bar: get_distance(long, lat, bar))
        return closest


def main():
    if len(sys.argv) < 2:
        exit("Пустой путь")
    else:
        path_to_json = sys.argv[1]
    try:
        bars_list = load_data(path_to_json)
    except OSError as err:
        exit("{}".format(err))
    if bars_list is None:
        exit("Invalid JSON")
    big_bar = get_biggest_bar(bars_list)
    small_bar = get_smallest_bar(bars_list)
    long, lat = get_coords()
    if long is None or lat is None:
        exit("Invalid coordinates")
    closest_bar = get_closest_bar(bars_list, long, lat)
    print("Самый большой бар - {}".format(get_name(big_bar)))
    print("Самый маленький бар - {}".format(get_name(small_bar)))
    print("Самый близкий бар - {}".format(get_name(closest_bar)))


if __name__ == "__main__":
    main()

