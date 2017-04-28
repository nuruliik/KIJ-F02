import socket
import json
from key_exhange import *
from enkripsi import process_oop as enkrip

enkripsi = enkrip.process_oop()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("",8888))

print "Menunggu user lain terhubung ...."
server.listen(5)

client,addr = server.accept()
print addr, "Terhubung!!!!!!"
print "Mengirim q dan a....."
q = bigPrime()
a = smallPrime()
client.send(json.dumps({'q':q,'a':a}))

xa = secretKey()
public_key = publicKey(xa,q,a)

print "Mengirim Public Key "  ,public_key
client.send(str(public_key))
print "Menerima Public Key user lain ......"
public_key_other = int(client.recv(1024))
print "****", public_key_other

private_key = privateKey(public_key_other,xa,a)
print "Private Key = ", private_key
key = set_key(str(private_key))

print "\n Silakan Berkirim Pesan\n"
while True:
    while True:
        msg = raw_input(">>> ")
        chipermsg = enkripsi.ofb_enkripsi(msg, key)
        client.send(chipermsg)
        print addr, " :", enkripsi.ofb_dekripsi(client.recv(1024), key)