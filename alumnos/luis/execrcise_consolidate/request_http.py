# Create script to request http
import requests

url_post = 'http://localhost:6000/student/1/Ricardo'
url_get = 'http://localhost:6000/students'
url_get_by_id = 'http://localhost:6000/student/1'

type_request = input('Ingrese el tipo de request: ')

try:
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

except Exception as e:
    print(e)
