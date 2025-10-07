
from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ven = Tk()  # Libreria
        self.ven.title('Programa 5 con Ventanas')  # Titulo de la ventana
        self.ven.geometry('600x250')  # Tamaño de la ventana
        self.lista = []
        self.inicio()
    def sumar(self):
        s = 0
        for i in self.lista:
            s += i #suma de cada elemento de la lista
        return s
    def promediar(self):
        try:
            a = float(self.n1.get())
            b = float(self.n2.get())
            c = float(self.n3.get())
            d = float(self.n4.get())
            pro =(a+b+c+d)/4
            self.l6.config(text=str(pro))
            self.lista.append(pro)
            self.l7.config(text=str(self.lista))
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.n3.delete(0,END)
            self.n4.delete(0,END)
            suma = self.sumar()
            p = suma / len(self.lista)#len, longitud de la lista
            self.l8.config(text=f' Promedio general: {str(p)}')

        except ValueError:
            messagebox.showerror("Error","Algun dato no es un numero")
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            self.n3.delete(0,END)
            self.n4.delete(0,END)
    def salir(self):
         self.ven.destroy()

        
    def inicio(self):
        l1 = Label(self.ven, text="Escribe un numero").place(y=10,x=20)#Y son filas y X columnas por el plano cartesiano ingles
        l2 = Label(self.ven, text="Escribe un numero").place(y=50,x=20)
        self.n1 = Entry(self.ven)
        self.n1.place(y=10, x=130)
        self.n2 = Entry(self.ven)
        self.n2.place(y=50, x=130)#cajas de texto
        l3 = Label(self.ven, text="Escribe un numero").place(y=90,x=20)#etiquetas label
        l4 = Label(self.ven, text="Escribe un numero").place(y=130,x=20)
        self.n3 = Entry(self.ven)
        self.n3.place(y=90, x=130)
        self.n4 = Entry(self.ven)
        self.n4.place(y=130, x=130)
        l5 = Label(self.ven, text="Promedio: ").place(y=150,x=130)
        self.l6 = Label(self.ven, text="0.0")
        self.l6.place(y=150,x=200)
        b1 = Button(self.ven, text="promedio", command=self.promediar).place(y=50,x=300)
        b2 = Button(self.ven, text="salir", command=self.salir).place(y=90,x=300)
        self.l7 = Label(self.ven, text="[]")
        self.l7.place(y=170,x=200)
        self.l8 = Label(self.ven, text="Promedio general: 0.0")
        self.l8.place(y=190,x=150)





        self.ven.mainloop()#para mostrar visualmente la ventana




if __name__ == "__main__":
    app = Principal()