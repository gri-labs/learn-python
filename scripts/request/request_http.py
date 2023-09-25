# Create script to request http
import requests

url_post = 'http://localhost:6000/employ'
url_get = 'http://localhost:6000/employ/3'
url_get_by_id = 'http://localhost:6000/student/1'
url_delete = 'http://localhost:6000/employ/1'
url_put = 'http://localhost:6000/employ/2'

type_request = input('Ingrese el tipo de request: ')

if type_request == 'GET':
    response = requests.get(url_get)
    print(response.json())
elif type_request == 'POST':
    response = requests.post(url_post, json={'name': 'Ricardo', 'department': 'IT', 'salary': 2500.00})
    print(response.json())
elif type_request == 'GET_BY_ID':
    response = requests.get(url_get_by_id)
    print(response.json())
elif type_request == 'DELETE':
    response = requests.delete(url_delete)
    print(response.json())
elif type_request == 'PUT':
    response = requests.put(url_put, json={'name': 'Ricardo', 'department': 'IT', 'salary': 3500.00})
    print(response.json())
else:
    print('Tipo de request no soportado')
