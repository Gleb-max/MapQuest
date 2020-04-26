import requests


def make_get_request(url, params):
    response = requests.get(url, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None
    return response


def tokenize_word(word):
    return word
