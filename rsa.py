import random
import math
import tkinter
import webbrowser
import pyperclip
import sys
import os


def resource_path(relative_path):
    """Devuelve la ruta absoluta del archivo para PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Funcions "internes"
def prime_generator():
    while True:
        number = random.randint(100, 999)
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

def cypher(plaintext, e, n):
    plist = []
    for m in plaintext:
        m = ord(m)
        plist.append((m ** e) % n)
    return plist

def decipher(cyphertxt, n, d):
    elist = []
    for C in cyphertxt:
        M = pow(C, d, n)
        elist.append(chr(M))
    return "".join(elist)


def opManual():
    webbrowser.open("https://docs.google.com/document/d/1jfODmPfew1bb6YUtB_-nZCqmj27m_gtPon8m0G22sNg/edit?pli=1&tab=t.0#heading=h.io896uf4pm76")

def opASCII():
    webbrowser.open("https://elcodigoascii.com.ar/")

def opTeoria():
    webbrowser.open("https://docs.google.com/document/d/1jfODmPfew1bb6YUtB_-nZCqmj27m_gtPon8m0G22sNg/edit?pli=1&tab=t.0#heading=h.dhw8vuos626h")

#Variables globals
p = q = n = e = d = Euler = None
text = ""
C = []
deciphertxt = ""

#Finestra
window = tkinter.Tk()
window.geometry("950x650")
window.resizable(False, False)
window.title("RSA - Víctor Lacruz")
window.config(bg="#1f2327")
icon_path = resource_path("icon.png")
icon = tkinter.PhotoImage(file=icon_path)
window.iconphoto(True, icon)

label_style = {"bg": "#1f2327", "fg": "#b6b6b7", "font": ("Arial", 12)}

entry_style = {"bg": "#181c20", "fg": "#b6b6b7", "relief": "flat", "insertbackground": "white", "font": ("Arial", 13), "justify": "center"}

btn_style = {"bg": "#24282c", "fg": "#e0e0e0", "activebackground": "#3a3f44",
             "activeforeground": "white", "relief": "flat",
             "font": ("Arial", 11, "bold"), "width": 18, "height": 2}


title = tkinter.Label(window, text="Xifrar amb RSA", font=("Arial", 22, "bold"), bg="#1f2327", fg="#e0e0e0")
title.pack(pady=20)


frame_keys = tkinter.Frame(window, bg="#1f2327")
frame_keys.pack(pady=10)

lbl_p = tkinter.Label(frame_keys, text="p", **label_style); lbl_p.grid(row=0, column=0, padx=10, pady=5)
ent_p = tkinter.Entry(frame_keys, width=15, **entry_style); ent_p.grid(row=1, column=0, padx=10, pady=5)

lbl_q = tkinter.Label(frame_keys, text="q", **label_style); lbl_q.grid(row=0, column=1, padx=10, pady=5)
ent_q = tkinter.Entry(frame_keys, width=15, **entry_style); ent_q.grid(row=1, column=1, padx=10, pady=5)

lbl_n = tkinter.Label(frame_keys, text="n = p·q", **label_style); lbl_n.grid(row=0, column=2, padx=10, pady=5)
ent_n = tkinter.Entry(frame_keys, width=15, **entry_style); ent_n.grid(row=1, column=2, padx=10, pady=5)

lbl_phi = tkinter.Label(frame_keys, text="φ(n)", **label_style); lbl_phi.grid(row=2, column=0, padx=10, pady=5)
ent_phi = tkinter.Entry(frame_keys, width=15, **entry_style); ent_phi.grid(row=3, column=0, padx=10, pady=5)

lbl_e = tkinter.Label(frame_keys, text="e", **label_style); lbl_e.grid(row=2, column=1, padx=10, pady=5)
ent_e = tkinter.Entry(frame_keys, width=15, **entry_style); ent_e.grid(row=3, column=1, padx=10, pady=5)

lbl_d = tkinter.Label(frame_keys, text="d", **label_style); lbl_d.grid(row=2, column=2, padx=10, pady=5)
ent_d = tkinter.Entry(frame_keys, width=15, **entry_style); ent_d.grid(row=3, column=2, padx=10, pady=5)

#Scroll
def make_scroll_entry(parent, width=30):
    frame = tkinter.Frame(parent, bg="#1f2327")
    entry = tkinter.Entry(frame, width=width, **entry_style)
    entry.pack(side="top", fill="x", padx=2)

    scrollbar = tkinter.Scrollbar(frame, orient="horizontal", command=entry.xview, bg="#24282c", troughcolor="#181c20")
    scrollbar.pack(side="bottom", fill="x")

    entry.config(xscrollcommand=scrollbar.set)
    return entry, frame

frame_msgs = tkinter.Frame(window, bg="#1f2327")
frame_msgs.pack(pady=20)

# Missatge original
lbl_msg = tkinter.Label(frame_msgs, text="Missatge original", **label_style)
lbl_msg.grid(row=0, column=0, padx=20, pady=5)
ent_msg, frame_msg = make_scroll_entry(frame_msgs, width=30)
frame_msg.grid(row=1, column=0, padx=20, pady=5)

# Missatge xifrat
lbl_cyph = tkinter.Label(frame_msgs, text="Missatge xifrat", **label_style)
lbl_cyph.grid(row=0, column=1, padx=20, pady=5)
ent_cyph, frame_cyph = make_scroll_entry(frame_msgs, width=30)
frame_cyph.grid(row=1, column=1, padx=20, pady=5)

# Missatge desxifrat
lbl_dec = tkinter.Label(frame_msgs, text="Missatge desxifrat", **label_style)
lbl_dec.grid(row=0, column=2, padx=20, pady=5)
ent_dec, frame_dec = make_scroll_entry(frame_msgs, width=30)
frame_dec.grid(row=1, column=2, padx=20, pady=5)

#Funcions dels Botons
def generar():
    global p, q, n, Euler, e, d
    p = prime_generator()
    q = prime_generator()
    Euler = Euler_function(p, q)
    e = find_e(Euler)
    n = p*q
    d = pow(e, -1, Euler)
    
    ent_p.delete(0, "end"); ent_p.insert(0, str(p))
    ent_q.delete(0, "end"); ent_q.insert(0, str(q))
    ent_n.delete(0, "end"); ent_n.insert(0, str(n))
    ent_phi.delete(0, "end"); ent_phi.insert(0, str(Euler))
    ent_e.delete(0, "end"); ent_e.insert(0, str(e))
    ent_d.delete(0, "end"); ent_d.insert(0, str(d))

def xifrar():
    global text, C
    text = ent_msg.get()
    C = cypher(text, e, n)
    ent_cyph.delete(0, "end")
    ent_cyph.insert(0, str(C))

def desxifrar():
    global deciphertxt
    deciphertxt = decipher(C, n, d)
    ent_dec.delete(0, "end")
    ent_dec.insert(0, deciphertxt)

def copy():
    text = ent_cyph.get()
    pyperclip.copy(text)

# Botons
frame_btns = tkinter.Frame(window, bg="#1f2327")
frame_btns.pack(pady=30)

btn_gen = tkinter.Button(frame_btns, text="Generar claus", **btn_style, command=generar)
btn_gen.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)

btn_xif = tkinter.Button(frame_btns, text="Xifrar missatge", **btn_style, command=xifrar)
btn_xif.grid(row=0, column=1, padx=20, pady=10, ipadx=5, ipady=5)

btn_desxif = tkinter.Button(frame_btns, text="Desxifrar missatge", **btn_style, command=desxifrar)
btn_desxif.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

btn_manual = tkinter.Button(frame_btns, text="Manual", **btn_style, command=opManual)
btn_manual.grid(row=1, column=0, padx=20, pady=10, ipadx=5, ipady=5)

btn_teoria = tkinter.Button(frame_btns, text="Teoria RSA", **btn_style, command=opTeoria)
btn_teoria.grid(row=1, column=1, padx=20, pady=10, ipadx=5, ipady=5)

btn_ascii = tkinter.Button(frame_btns, text="Taula ASCII", **btn_style, command=opASCII)
btn_ascii.grid(row=1, column=2, padx=20, pady=10, ipadx=5, ipady=5)

btn_copy = tkinter.Button(frame_btns, text="Copiar Xifrat", **btn_style, command=copy)
btn_copy.grid(row=2, column=1, padx=20, pady=10, ipadx=5, ipady=5)

window.mainloop()
