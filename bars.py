import json
import sys
import requests
from math import sqrt


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_seats(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_coords():
    lat = float(input("Введите широту: ").strip())
    long = float(input("Введите долготу: ").strip())
    return lat, long


def get_distance(long=None, lat=None, bar=None):
    if lat is None and bar is None:
        return lambda lat, bar: sqrt(
            abs(long-bar["geometry"]["coordinates"][0])**2
            + abs(lat-bar["geometry"]["coordinates"][1])**2)
    elif bar is None:
        return lambda bar: sqrt(
            abs(long-bar["geometry"]["coordinates"][0])**2
            + abs(lat-bar["geometry"]["coordinates"][1])**2)


def load_data():
    try:
        path_to_json = sys.argv[1]
        with open(path_to_json, "r", encoding="utf-8") as json_file:
            return json.loads(json_file.read())["features"]
    except IndexError:
        url = ("https://devman.org/media/filer_public/" +
               "95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json")
        res = requests.get(url)
        return json.loads(res.text)["features"]
    except ValueError:
        raise ValueError("Invalid JSON")


def get_biggest_bar(json_content):
    if json_content is not None:
        biggest_bar = max(json_content, key=get_seats)
        return biggest_bar


def get_smallest_bar(json_content):
    if json_content is not None:
        smallest_bar = min(json_content, key=get_seats)
        return smallest_bar


def get_closest_bar(json_content, long, lat):
    if json_content is not None and long is not None and lat is not None:
        closest = min(json_content, key=get_distance(long, lat))
        return closest


def main():
    try:
        json_content = load_data()
        big_bar = get_biggest_bar(json_content)
        small_bar = get_smallest_bar(json_content)
        long, lat = get_coords()
        closest_bar = get_closest_bar(json_content, long, lat)
        print("Самый большой бар \"{}\"".format(get_name(big_bar)))
        print("Самый маленький бар \"{}\"".format(get_name(small_bar)))
        print("Самый близкий бар \"{}\"".format(get_name(closest_bar)))
    except OSError as err:
        print("1{}".format(err))
    except ValueError as err:
        print("{}".format(err))


if __name__ == "__main__":
    main()
