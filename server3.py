import socket
import threading


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    response = data
                    if data == 'close':
                        raise client.close()
                    client.send(response)
                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":

    host = '0.0.0.0'
    port = 2222

    ThreadedServer(host, port).listen()
