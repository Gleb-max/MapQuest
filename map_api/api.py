from utils.utils import make_get_request


def coordinates_by_address(place):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": place,
        "format": "json",
    }

    response = make_get_request(geocode_url, geocode_params)
    if response is None:
        return None
    json_response = response.json()

    toponyms = json_response["response"]["GeoObjectCollection"]["featureMember"]

    if not toponyms:
        print("Адрес не найден")
        return None

    toponym = toponyms[0]["GeoObject"]
    coordinates = toponym["Point"]["pos"]

    return tuple(map(float, coordinates.split(" ")))


def get_bytes_map(coordinates, map_type):
    map_url = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "l": map_type,
        "ll": ",".join(map(str, coordinates)),
        "z": 7,
    }

    response = make_get_request(map_url, map_params)
    if not response:
        print("Не удалось отобразить карту")
        return
    print(response.url)
    return response.content
