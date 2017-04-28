import socket
import json
from key_exhange import *
from enkripsi import process_oop as enkrip

enkripsi = enkrip.process_oop()
server  = socket.socket()
server.connect(("127.0.0.1",8888))

print "Menerima q dan a . . ."
jsonMessage = json.loads(server.recv(1024))
q = jsonMessage['q']
a = jsonMessage['a']

print "Menerima public key user lain ...."
public_key_other = int(server.recv(2048))
print "****", public_key_other
xb = secretKey()
public_key = publicKey(xb,q,a)
print "Mengirim public key", public_key
server.send(str(public_key))

private_key = privateKey(public_key_other,xb,a)
print "Private Key = ", private_key
key = set_key(str(private_key))

print "\n Silakan Berkirim Pesan\n"
while True:
    print "(192.168.0.127,8888) :", enkripsi.ofb_dekripsi(server.recv(1024),key)
    msg = raw_input(">>> ")
    server.send(enkripsi.ofb_enkripsi(msg,key))