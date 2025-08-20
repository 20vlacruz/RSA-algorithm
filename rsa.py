import random
import math
import tkinter

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


window = tkinter.Tk()
window.title("Generador de xifrats RSA")


entrada = tkinter.Entry(window, font=("Arial", 40), width=25)
entrada.insert(0, "Introdueix el text a encritar: ")
entrada.grid(row = 0, column=0,padx=5, pady=5, columnspan=4)



Column0 = tkinter.Label(text="Opcions per Xifrar")
Column0.grid(row=1, column=0)

Column0 = tkinter.Label(text="Opcions per desxifrar")
Column0.grid(row=1, column=1)

Column0 = tkinter.Label(text="Recursos")
Column0.grid(row=1, column=2)


#Columna 0
genprim = tkinter.Button(text="Generar p i q")
genprim.grid(row=2, column=0)

genn = tkinter.Button(text="Generar nombre n")
genn.grid(row=3, column=0)

genEuler = tkinter.Button(text="Generar nombre funció Phi")
genEuler.grid(row=4, column=0)

startconv = tkinter.Button(text="Xifrar")
startconv.grid(row=5, column=0)

#Columna 1
findd = tkinter.Button(text="Trobar d")
findd.grid(row=2, column=1)

startdesconv = tkinter.Button(text="Desxifrar")
startdesconv.grid(row=3, column=1)

#Columna 2
astable = tkinter.Button(text="Taula de conversió ASCII")
astable.grid(row=2, column=2)

theory = tkinter.Button(text="Manual de teoria RSA")
theory.grid(row=3, column=2)

window.mainloop()