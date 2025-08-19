import random
import math

def prime_generator():
    while True:
        number = random.randint(100, 900)
        prime = True

        for i in range(2, number):
            if number % i == 0:
                prime = False
                break 

        if prime:
            return number



def Euler_function(p, q):
    result = (p-1) * (q - 1)
    return result


def find_e(Euler):
    while True:
        e = random.randint(2, Euler - 1)
        if math.gcd(e, Euler) == 1:
            return e

def n(p, q):
    n = p * q
    return n


def cypher(plaintext, e, n):
    plist = []
    cypher = ""
    for m in plaintext:
        m = ord(m)
        plist.append((m**e)%n)
    return(plist)

def decipher(cyphertxt, e, Euler, n):
    d = pow(e, -1, Euler)
    elist=[]
    for C in cyphertxt:
        D = pow(C, d, n)
        elist.append(chr(D))
    D = ""
    for i in elist:
        D += i
    return D

p = prime_generator()
q = prime_generator()
Euler = Euler_function(p, q)
e = find_e(Euler)
n = n(p,q)


tcypher=cypher("Hello World!",e, n)
print(tcypher)

tdecipher = decipher(tcypher, e, Euler, n)
print(tdecipher)

