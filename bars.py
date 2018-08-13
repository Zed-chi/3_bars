import json
from math import sqrt


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_seats(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_coords():
    lat = float(input("Введите широту: ").strip())
    long = float(input("Введите долготу: ").strip())
    return lat, long


def get_distance(long, lat, bar=None):
    if bar is None:
        return lambda bar: sqrt(
            abs(long-bar["geometry"]["coordinates"][0])**2
            + abs(lat-bar["geometry"]["coordinates"][1])**2)


def load_data(path_to_json):
    with open(path_to_json, "r", encoding="utf-8") as json_file:
        return json.loads(json_file.read())["features"]


def get_biggest_bar(decoded_json):
    if decoded_json is not None:
        biggest_bar = max(decoded_json, key=get_seats)
        return biggest_bar


def get_smallest_bar(decoded_json):
    if decoded_json is not None:
        smallest_bar = min(decoded_json, key=get_seats)
        return smallest_bar


def get_closest_bar(decoded_json, long, lat):
    if decoded_json is not None and long is not None and lat is not None:
        closest = min(decoded_json, key=get_distance(long, lat))
        return closest


def main():
    try:
        path_to_json = input("Введите путь до json файла: ")
        decoded_json = load_data(path_to_json)
        big_bar = get_biggest_bar(decoded_json)
        small_bar = get_smallest_bar(decoded_json)
        long, lat = get_coords()
        closest_bar = get_closest_bar(decoded_json, long, lat)
    except OSError as err:
        print("{}".format(err))
    except ValueError as err:
        print("{}".format(err))
    else:
        print("Самый большой бар - {}".format(get_name(big_bar)))
        print("Самый маленький бар - {}".format(get_name(small_bar)))
        print("Самый близкий бар - {}".format(get_name(closest_bar)))


if __name__ == "__main__":
    main()

