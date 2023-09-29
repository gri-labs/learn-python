import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen()
        print("Listening on port {}...".format(self.port))
        while True:
            client, address = self.sock.accept()
            print("Connected to {}".format(address))
            print("Received: {}".format(client.recv(1024).decode()))
            client.send("Hello World!".encode())
            client.close()


if __name__ == "__main__":
    server = Server('localhost', 6000)
    server.listen()
