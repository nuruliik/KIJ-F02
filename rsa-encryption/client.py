import socket
import json
from rsa_encryption import *
from enkripsi_des import process_oop as des

des = des.process_oop()

server = socket.socket()
server.connect(("127.0.0.1",8888))

key = "kij12345"

print "Menerima public key . . ."
jsonMessage = json.loads(server.recv(1024))
e = jsonMessage[0]
n = jsonMessage[1]

encrypted_key = rsaEncrypt(key,e,n)

print "Mengirim key yang sudah di enkripsi",encrypted_key
server.send(json.dumps(encrypted_key))

print "\n Silakan Berkirim Pesan\n"
while True:
    message_get = server.recv(1024)
    print  "server :(raw)" + des.bin_to_hex(message_get) + " (decrypt) " + des.ofb_dekripsi(message_get, key)
    # print "(192.168.0.127,8888) :", enkripsi.ofb_dekripsi(server.recv(1024),key)
    msg = raw_input(">>> ")
    server.send(des.ofb_enkripsi(msg,key))