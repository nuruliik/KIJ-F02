import socket
import json
from rsa_encryption import *
from enkripsi_des import process_oop as des


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("",8888))

des = des.process_oop()

print "Menunggu user lain terhubung ...."
server.listen(5)

client,addr = server.accept()
print addr,"Terhubung!!!!!"

p = generatePAndQ()
q = generatePAndQ()
n = getN(p, q)
m = getM(p, q)
e = getRelativePrime(m)
d = modinv(e, m)
public_key = [e,n]
private_key = [d,n]

print "Public Key Anda : ",public_key
print "Private Key Anda : ",private_key

print "Mengirim Public Key",public_key
client.send(json.dumps(public_key))

print "Menunggu enkripsi DES Key user lain ......"
des_key = json.loads(client.recv(1024))
print "****", des_key

print "Mendecrypt key . . ."
true_des_key = rsaDecrypt(des_key,d,n)
print "Des Key setelah di decrypt ", true_des_key

print "\n Silakan Berkirim Pesan\n"
while True:
    while True:
        msg = raw_input(">>> ")
        chipermsg = des.ofb_enkripsi(msg, true_des_key)
        client.send(chipermsg)
        message_get = client.recv(1024)
        print addr, " :(raw)" + des.bin_to_hex(message_get) +"(decrypt)"+des.ofb_dekripsi(message_get, true_des_key)