import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 2222

s.bind((host, port))

while True:
    s.listen(10)

    conn, addr = s.accept()
    # conn.setblocking(0)

    while True:

        data = conn.recv(1024)

        if data == 'close':
            break
        print("+ " + data)

        if not data:
            break
        conn.send(data)

    conn.close()
