# Create script to request http
import requests

url_post = 'http://localhost:6000/student/1/Jesus'
url_get = 'http://localhost:6000/studiantes'
url_get_by_id = 'http://localhost:6000/studiantes/1'

type_request = input('Ingrese el tipo de request: ')

if type_request == 'GET':
    response = requests.get(url_get)
    print(response.json())
elif type_request == 'POST':
    response = requests.post(url_post)
    print(response.json())
elif type_request == 'GET_BY_ID':
    response = requests.get(url_get_by_id)
    print(response.json())
else:
    print('Tipo de request no soportado')