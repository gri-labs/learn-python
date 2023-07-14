# Create script to request http
import requests

url_post = 'http://localhost:6000/estudiantes/1/Jesus'
url_get = 'http://localhost:6000/estudiantes'
url_get_by_id = 'http://localhost:6000/estudiantes/1'
url_delete = 'http://localhost:6000/estudiantes/1'
url_put = 'http://localhost:6000/estudiantes/1/JesusRV'


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
elif type_request == 'DELETE':
    response = requests.delete(url_delete)
    print(response.json())
elif type_request == 'PUT':
    response = requests.put(url_put)
    print(response.json())
else:
    print('Tipo de request no soportado')
