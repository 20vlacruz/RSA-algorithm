import random
import math
import tkinter
import webbrowser

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

def decipher(cyphertxt, n):
    elist = []
    for C in cyphertxt:
        M = pow(C, d, n)
        elist.append(chr(M))
    result = "".join(elist)
    return result

def opManual():
    url = "https://docs.google.com/document/d/1jfODmPfew1bb6YUtB_-nZCqmj27m_gtPon8m0G22sNg/edit?pli=1&tab=t.0#heading=h.3mnsjxsuq5xf"
    webbrowser.open(url)

def opRSA():
    url = "https://docs.google.com/document/d/1jfODmPfew1bb6YUtB_-nZCqmj27m_gtPon8m0G22sNg/edit?pli=1&tab=t.0#heading=h.dhw8vuos626h"
    webbrowser.open(url)

def opASCII():
    url = "https://elcodigoascii.com.ar/"
    webbrowser.open(url)


p = prime_generator()
q = prime_generator()
Euler = Euler_function(p, q)
e = find_e(Euler)
n = n(p,q)
d = pow(e, -1, Euler)

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
entrada.insert(0, "Introdueix el text a xifrar")
title = tkinter.Label(
    text="Encriptador RSA",
    font=("Arial", 20),
    width=40,
    bg="#1f2327",
    fg="#b6b6b7",
    relief="flat"
)
title.grid(row=0, column=0, padx=10, pady=15, columnspan=3, sticky="nsew")

entrada.grid(row=1, column=0, padx=10, pady=15, columnspan=2, sticky="nsew")

def delete():
    entrada.delete(0, "end")
    entrada.insert(0, "Introdueix el text a xifrar")

btn_delete = tkinter.Button(
    window,
    text="Esborrar",
    font=("Arial", 12),
    bg="#24282c",
    fg="#e0e0e0",
    relief="flat",
    activebackground="#3a3f44",
    activeforeground="white",
    width=15,
    height=2,
    command=delete
)
btn_delete.grid(row=1, column=2, padx=10, pady=15, sticky="nsew")


def on_entry_click(event):
    if entrada.get() != "":
        entrada.delete(0, "end")
    entrada.config(fg="#e0e0e0")

def on_focusout(event):
    if entrada.get() == "":
        entrada.insert(0, "Introdueix el text a xifrar")
        entrada.config(fg="#808285") 

def focusout(event):
    widget = event.widget
    if not isinstance(widget, tkinter.Entry):
        window.focus()

window.bind_all("<Button-1>", focusout)
entrada.bind("<FocusIn>", on_entry_click)
entrada.bind("<FocusOut>", on_focusout)

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
b0_3 = tkinter.Button(window, text="Guardar text", **btn_style, command= lambda: savetxt())
b0_3.grid(row=3, column=0, pady=5, padx=15)
b0_0 = tkinter.Button(window, text="Generar p i q", **btn_style, command=lambda:showprimes(p, q))
b0_0.grid(row=4, column=0, pady=5, padx=15)
b0_1 = tkinter.Button(window, text="Generar nombre n", **btn_style, command=lambda:shown(n))
b0_1.grid(row=5, column=0, pady=5, padx=15)
b0_2 = tkinter.Button(window, text="Generar nombre funció Phi", **btn_style, command=lambda:showphi(Euler))
b0_2.grid(row=6, column=0, pady=5, padx=15)
b0_4 = tkinter.Button(window, text="Xifrar", **btn_style, command=lambda: savecypher(text, e, n))
b0_4.grid(row=7, column=0, pady=5, padx=15)

# Columna 1 - Desxifrar
b1_3 = tkinter.Button(window, text="Mostrar text xifrat", **btn_style, command=lambda: showcypher(C))
b1_3.grid(row=3, column=1, pady=5, padx=15)
b1_0 = tkinter.Button(window, text="Trobar d", **btn_style, command= lambda: showd())
b1_0.grid(row=4, column=1, pady=5, padx=15)
b1_1 = tkinter.Button(window, text="Desxifrar", **btn_style, command= lambda: savedecipher())
b1_1.grid(row=5, column=1, pady=5, padx=15)
b1_2 = tkinter.Button(window, text="Mostrar text desxifrat", **btn_style, command=lambda: showdecipher(deciphertxt))
b1_2.grid(row=6, column=1, pady=5, padx=15)

# Columna 2 - Recursos
b2_0 = tkinter.Button(window, text="Instruccions Aplicació", **btn_style, command=opManual)
b2_0.grid(row=3, column=2, pady=5, padx=15)
b2_1 = tkinter.Button(window, text="Manual de teoria RSA", **btn_style)
b2_1.grid(row=4, column=2, pady=5, padx=15)
b2_2 = tkinter.Button(window, text="Taula de conversió ASCII", **btn_style, command=opASCII)
b2_2.grid(row=5, column=2, pady=5, padx=15)

# Expandir columnes
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

#Funcions UI
def showprimes(p, q):
    entrada.delete(0, "end")
    entrada.insert(0, f"p = {p} i q = {q}")

def shown(n):
    entrada.delete(0, "end")
    entrada.insert(0, f"n = {n}")

def showphi(phi):
    entrada.delete(0, "end")
    entrada.insert(0, f"φ = {phi}")

text = ""
def savetxt():
    global text
    text = entrada.get()
    entrada.delete(0, "end")
    entrada.insert(0, "El text s'ha guardat correctament.")
    return text

C=""
def savecypher(ptext, e, n):
    global C
    C = cypher(ptext, e, n)
    entrada.delete(0, "end")
    entrada.insert(0, f"El text s'ha xifrat correctament.")

def showcypher(C):
    entrada.delete(0, "end")
    entrada.insert(0, C)

def showd():
    entrada.delete(0, "end")
    entrada.insert(0, f"d = {d}")

deciphertxt =""
def savedecipher():
    global C
    global n
    global deciphertxt
    deciphertxt = decipher(C, n)
    entrada.delete(0, "end")
    entrada.insert(0, "El text s'ha desxifrat correctament.")

def showdecipher(D):
    entrada.delete(0, "end")
    entrada.insert(0, D)

window.mainloop()