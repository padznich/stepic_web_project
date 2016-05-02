import socket
import time


req = "="
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 2222))
i = 1
while i < 2:
    s.send("client1" + req + ' ' + str(i))
    rsp = s.recv(1024)
    print("-", rsp)
    time.sleep(3)
    i += 1

s.send("after1")
time.sleep(1)
s.send("close")
time.sleep(1)
s.send("after2")
s.close()
