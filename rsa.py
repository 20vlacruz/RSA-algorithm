import random

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



def ASCII_conv(string):
    conversion = []
    for char in string:
        conversion.append(ord(char))
    return conversion


def Euler_function(p, q):
    result = (p-1) * (q - 1)
    return print(result)