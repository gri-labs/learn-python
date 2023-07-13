import requests

url = 'http://localhost:8080/estudiante/delete/3'

response = requests.delete(url)
if response.status_code == 200:
    print('Estudiante eliminado correctamente')
else:
    print('Error al eliminar estudiante')