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


# Configuració principal
window = tkinter.Tk()
window.geometry("800x500")
window.resizable(False, False)
window.title("Títul TR - Víctor Lacruz")
window.config(bg="#1f2327")
icon = tkinter.PhotoImage(file="icon.png")
window.iconphoto(True, icon)

# Entrada principal
entrada = tkinter.Entry(
    window, 
    font=("Arial", 20),
    width=40, 
    bg="#181c20", 
    fg="#b6b6b7", 
    relief="flat", 
    insertbackground="white"
)
title = tkinter.Label(
    text="Encriptador RSA",
    font=("Arial", 20),
    width=40,
    bg="#1f2327",
    fg="#b6b6b7",
    relief="flat"
)
title.grid(row=0, column=0, padx=10, pady=15, columnspan=3, sticky="nsew")

entrada.insert(0, "Introdueix el text: ")
entrada.grid(row=1, column=0, padx=10, pady=15, columnspan=3, sticky="nsew")

# Títuls columnes
lbl0 = tkinter.Label(text="Opcions per Xifrar", font=("Arial", 15, "bold"), bg="#1f2327", fg="#b6b6b7", pady=10)
lbl0.grid(row=2, column=0, padx=20, pady=10)
lbl1 = tkinter.Label(text="Opcions per Desxifrar", font=("Arial", 15, "bold"), bg="#1f2327", fg="#b6b6b7", pady=10)
lbl1.grid(row=2, column=1, padx=20, pady=10)
lbl2 = tkinter.Label(text="Recursos", font=("Arial", 15, "bold"), bg="#1f2327", fg="#b6b6b7", pady=10)
lbl2.grid(row=2, column=2, padx=20, pady=10)

# Estil dels botons
btn_style = {"bg": "#24282c", "fg": "#e0e0e0", "activebackground": "#3a3f44", "activeforeground": "white",
             "relief": "flat", "font": ("Arial", 11), "width": 22, "height": 2}

# Columna 0 - Xifrar
b0_0 = tkinter.Button(window, text="Generar p i q", **btn_style)
b0_0.grid(row=3, column=0, pady=5, padx=15)
b0_1 = tkinter.Button(window, text="Generar nombre n", **btn_style)
b0_1.grid(row=4, column=0, pady=5, padx=15)
b0_2 = tkinter.Button(window, text="Generar nombre funció Phi", **btn_style)
b0_2.grid(row=5, column=0, pady=5, padx=15)
b0_3 = tkinter.Button(window, text="Xifrar", **btn_style)
b0_3.grid(row=6, column=0, pady=5, padx=15)
b0_4 = tkinter.Button(window, text="Mostrar xifrat", **btn_style)
b0_4.grid(row=7, column=0, pady=5, padx=15)

# Columna 1 - Desxifrar
b1_0 = tkinter.Button(window, text="Trobar d", **btn_style)
b1_0.grid(row=3, column=1, pady=5, padx=15)
b1_1 = tkinter.Button(window, text="Desxifrar", **btn_style)
b1_1.grid(row=4, column=1, pady=5, padx=15)
b1_2 = tkinter.Button(window, text="Mostrar text desxifrat", **btn_style)
b1_2.grid(row=5, column=1, pady=5, padx=15)

# Columna 2 - Recursos
b2_0 = tkinter.Button(window, text="Taula de conversió ASCII", **btn_style)
b2_0.grid(row=3, column=2, pady=5, padx=15)
b2_1 = tkinter.Button(window, text="Manual de teoria RSA", **btn_style)
b2_1.grid(row=4, column=2, pady=5, padx=15)

# Expandir columnes
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()