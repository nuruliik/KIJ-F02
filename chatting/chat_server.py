import socket
import enkripsi.process_oop as enkrip

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("localhost",8888))
server.listen(5)

enkripsi = enkrip.process_oop()
key = "kij12345"
client, addr = server.accept()
print addr, " Telah memasuki room"

while True:
    msg = raw_input(">>> ")
    chipermsg = enkripsi.ofb_enkripsi(msg,key)
    client.send(chipermsg)
    print addr ," :", enkripsi.ofb_dekripsi(client.recv(1024),key)