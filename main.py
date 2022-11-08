from tkinter import Tk, Button, Entry
import tkinter as tk

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x260")

# Configuración pantalla de salida 
salida = ""
eq = tk.StringVar()
pantalla = Entry(root, width=22, bg="black", fg="white", textvariable = eq, borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=2)

def presionar(num):
    global salida
    salida = salida + str(num)
    eq.set(salida)
    

def igual():
    try:
        global salida
        total = str(eval(salida))
        eq.set(total)
        salida = ""
    except:
        eq.set(" Error ")
        salida = "" 



# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(1))
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(2))
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(3))
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(4))
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(5))
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(6))
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(7))
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(8))
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: presionar(9))
boton_9.grid(row=3, column=2, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: igual())
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: presionar("."))
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: presionar("+"))
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: presionar("-"))
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: presionar("*"))
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: presionar("/"))
boton_division.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()