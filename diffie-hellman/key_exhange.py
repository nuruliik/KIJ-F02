import random

def bigPrime():
    while True:
        p = random.randrange(1000, 9999, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def secretKey():
    q = bigPrime()
    while True:
        p = random.randrange(1000,q,2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def smallPrime():
    while True:
        p = random.randrange(2, 999, 1)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def publicKey(prime_number, g, n):
    return pow(g, prime_number) % n

def privateKey(public_key, prime_number, n):
    return pow(public_key, prime_number) % n

def set_key(private_key):
    key = "kij12345"
    for i in range(0, 8-len(private_key)):
        private_key = private_key+'0'
    return key

def primitiveRoot():
    q = bigPrime()
    for i in range(2,q):
        x = []
        for j in range(1,q-1):
            print j
            x.append(pow(j,i)%q)
        if len(x)==len(set(x)):
           return i

