import socket
import enkripsi.process_oop as enkrip

enkripsi = enkrip.process_oop()
key = "kij12345"
server  = socket.socket()
server.connect(("localhost",8888))

while True:
    print "(localhost,8888) :", enkripsi.ofb_dekripsi(server.recv(1024),key)
    msg = raw_input(">>> ")
    server.send(enkripsi.ofb_enkripsi(msg,key))