# Create script to request http
import requests

port = '6000'
base_url = 'http://localhost:'+port

url_post = base_url+'/employ'
url_get = base_url+'/employ/4'
url_get_by_id = base_url+'/student/1'
url_delete = base_url+'/employ/4'
url_put = base_url+'/employ/2'

type_request = input('Ingrese el tipo de request: ')

if type_request == 'GET':
    response = requests.get(url_get)
    print(response.content.decode('utf-8'))
elif type_request == 'POST':
    data = {'name': 'admin', 'department': 'admin'}

    response = requests.post(url_post, params=data)
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
