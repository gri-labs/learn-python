# client to connect to the server:

import socket
import time


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.host, self.port))

    def send(self, msg):
        self.sock.send(msg.encode())

    def receive(self):
        return self.sock.recv(1024).decode()

    def close(self):
        self.sock.close()


if __name__ == "__main__":
    client = Client('localhost', 6001)
    client.connect()
    client.send("Good work e!")
    while True:
        print("Received: {}".format(client.receive()))
        time.sleep(2)