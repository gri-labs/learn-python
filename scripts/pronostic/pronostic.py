import requests


def get_info(api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": "Barcelona",
        "APPID": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        # Que hace el raise?
        # Raise es una palabra reservada que se utiliza para lanzar una excepción.
        raise Exception("Error en la petición, status code: ", response.status_code)

    return response.json()


def get_temperature(data):
    return data['main']['temp']


if __name__ == '__main__':
    print("La temperatura es: ", get_temperature(get_info("44eef3e79ed268f2755fb75b53e34579")), "ºC")
