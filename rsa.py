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


p = prime_generator()
q = prime_generator()
print(cypher("Hola", find_e(Euler_function(p, q)), n(p,q)))

