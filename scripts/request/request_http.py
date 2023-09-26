# Create script to request http
import requests

port = '81'
base_url = 'http://localhost:'+port

url_post = base_url+'/login'
url_get = base_url+'/info'
url_get_by_id = base_url+'/student/1'
url_delete = base_url+'/employ/1'
url_put = base_url+'/employ/2'

type_request = input('Ingrese el tipo de request: ')

if type_request == 'GET':
    response = requests.get(url_get)
    print(response)
elif type_request == 'POST':
    response = requests.post(url_post, json={'username': 'admin', 'password': 'admin'})
    print(response)
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
