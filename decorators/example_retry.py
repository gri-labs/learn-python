import requests


def retry_decorator(func):
    def wrapper():
        for i in range(3):
            try:
                func()
            except Exception as e:
                print(f"Error: {e}")
            else:
                break

    return wrapper


@retry_decorator
def http_request():
    print("Requesting...")
    response = requests.get("http://localhost:6000/student/1")
    print(response.json())


http_request()
