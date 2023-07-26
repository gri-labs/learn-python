import requests

url = url = 'http://localhost:8080/create/user/5/papi/90'


response = requests.post(url)
if response.status_code == 201:
    print('User inserted successfully')
else:
    print('Error while inserting user')