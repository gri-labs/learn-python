import requests

url = 'http://localhost:8080/estudiante/post'
data = {
    'id': 3,
    'nombre': 'Pepino',
    'carrera': 'pepote'
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Estudiante insertado correctamente')
else:
    print('Error al insertar estudiante')