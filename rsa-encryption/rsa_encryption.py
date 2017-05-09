import random
from fractions import gcd


def generatePAndQ():
    while True:
        p = random.randrange(1, 1000, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p


def getN(p, q):
    return p * q


def getM(p, q):
    return (p - 1) * (q - 1)


def getRelativePrime(m):
    e = []
    for i in range(1, m):
        if m % i != 0:
            e.append(i)
    for i in e:
        if gcd(i, m) == 1:
            return i


def getD(e, m):
    return pow(e, -1) % m


def generatePublicKey(message, e, n):
    chiper_text = []
    for i in message:
        chiper_text.append(pow(ord(i), e) % n)
    return chiper_text


def generatePrivatekey(chipert_text, d, n):
    message = ""
    for i in (chipert_text):
        print i
        print chr(pow(i,d)%n)
        # message = message + chr(pow(i,d)%n)
    return message


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


p = generatePAndQ()
q = generatePAndQ()
n = getN(p, q)
m = getM(p, q)
e = getRelativePrime(m)
d = modinv(e, m)

print e, m, d
chiper_text = generatePublicKey("saya", e, n)
print chiper_text
message = generatePrivatekey(chiper_text, d, n)
print message
