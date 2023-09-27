import requests

url = 'https://jsonplaceholder.typicode.com/users'

try:
    response = requests.get(url)

    if response.status_code == 200:
        list_data = response.json()
        for x in list_data:
            print(type(x))
except:
    print("Ha ocurrido un error")
