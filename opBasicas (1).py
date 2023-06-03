from tkinter import *

ventana = Tk()
ventana.title("Operaciones Básicas")
ventana.geometry('450x300')
ventana.configure(bg="royalblue")

presentacion = Label(ventana, text="Realiza Operaciones Básicas", font=("Arial Bold", 15), bg="royalblue").place(x=100, y=10)
lnum1 = Label(ventana, text="Ingresa el primer número: ", font=("Arial", 10), bg="royalblue").place(x=10, y=45)
lnum2 = Label(ventana, text="Ingresa el segundo número: ", font=("Arial", 10), bg="royalblue").place(x=10, y=70)
lab_resultado = Label(ventana, text="Resultado:", font=("Arial Bold", 10), bg="royalblue").place(x=10, y=240)

entradaNum1 = StringVar()
entradaNum2 = StringVar()
opcion = IntVar()

ingresoNum1 = Entry(ventana, textvariable=entradaNum1).place(x=165, y=45)
ingresoNum2 = Entry(ventana, textvariable=entradaNum2).place(x=180, y=70)

def suma():
    num1=float(entradaNum1.get()) 
    num2=float(entradaNum2.get())
    
    suma = num1 + num2
    
    resultado = Label(ventana, text=""+str(suma), font=("Arial", 10)).place(x=80, y=240)
    del(resultado)
    
def resta():
    num1=float(entradaNum1.get()) 
    num2=float(entradaNum2.get())
    
    resta = num1 - num2
    
    resultado = Label(ventana, text=""+str(resta), font=("Arial", 10)).place(x=80, y=240)
    del(resultado)
    
def multiplicacion():
    num1=float(entradaNum1.get()) 
    num2=float(entradaNum2.get())
    
    multiplicacion = num1 * num2
    
    resultado = Label(ventana, text=""+str(multiplicacion), font=("Arial", 10)).place(x=80, y=240)
    del(resultado)
    
def division():
    num1=float(entradaNum1.get()) 
    num2=float(entradaNum2.get())
    
    if num2==0:
        resultado = Label(ventana, text="No se puede hacer division entre 0", font=("Arial", 10)).place(x=80, y=240)

    elif num2!=0:
        division = num1 / num2
        resultado = Label(ventana, text=""+str(division), font=("Arial", 10)).place(x=80, y=240)

def borrar():
    resultado = Label(ventana, text="                                                   ", font=("Arial", 10), bg="royalblue").place(x=80, y=240)
    

lab_encabezado=Label(ventana, text="Operación a realizar:",font=("Arial Bold", 10), bg="royalblue").place(x=30, y=100)

btnS = Button(text="Suma", bg="orange", command=suma).place(x=70, y=120)
btnR = Button(text="Resta", bg="green", command=resta).place(x=70, y=150)
btnM = Button(text="Multiplicación", bg="red", command=multiplicacion).place(x=70, y=180)
btnD = Button(text="División", bg="yellow", command=division).place(x=70, y=210)
btnB = Button(text="Borrar Resultado", bg="aquamarine", command=borrar).place(x=200, y=160)

ventana.mainloop()