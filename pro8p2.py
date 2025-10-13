from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ven = Tk()  # Libreria
        self.ven.title('Programa 6 con Ventanas')  # Titulo de la ventana
        self.ven.geometry('650x350')  # Tamaño de la ventana
        self.a = 0
        self.b = 0
        self.lista = []
        self.aux1 = 0
        self.aux2 = 0
        self.cont = 0

    def inicio(self):
        l1 = Label(self.ven, text="Programa 9")
        l1.grid(row=1,column=2)
        l2= Label(self.ven, text="Escribe un numero")
        l2.grid(row=3, column=1, padx=15 , pady=10)
        Label(self.ven, text="").grid(row=2,column=2)
        self.n1 = Entry(self.ven)
        self.n1.grid(row=3, column=2)
        
        l3 = Label(self.ven, text="Escribe otro numero")
        l3.grid(row=1, column=2, padx=5 , pady=5)
        Label(self.ven, text="").grid(row=4,column=2)
        self.n2 = Entry(self.ven)
        self.n2.grid(row=5, column=2)
        b1 = Button(self.ven,text="Agregar", command=self.agregar)
        b1.grid(row=6, column=1, pady=10)
        b2 = Button(self.ven,text="Mayor", command=self.mayor)
        b2.grid(row=6, column=2)
        b3 = Button(self.ven,text="Menor", command=self.menor)
        b3.grid(row=6, column=3, padx=10)
        b4 = Button(self.ven,text="Salir", command=self.salir)
        b4.grid(row=6, column=4, padx=25)
        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.grid(row=8,column=2, pady=15)
        self.listview = Listbox(self.ven, height=10,
                                width=15, bg='black',
                                activestyle= "dotbox", fg="red")
        self.listview.grid(row=2,column=4)

        self.ven.mainloop()

    def mayor(self):
        if len(self.lista) > 0:
            self.aux1 = self.lista[0]  # inicializa
            for i in self.lista:
                if i > self.aux1:
                    self.aux1 = i
            print(f'el mayor es {self.aux1}')
            messagebox.showinfo('El mayor es', f'{self.aux1}')
        else:
            print("Lista vacia")
            messagebox.showerror("Error","La lista esta vacia")

    def menor(self):
        if len(self.lista) > 0:
            self.aux2 = self.lista[0]  # inicializa
            for i in self.lista:
                if i < self.aux2:
                    self.aux2 = i
            print(f'el menor es {self.aux2}')
            messagebox.showinfo('El menor es', f'{self.aux2}')
        else:
            messagebox.showerror("Error","La lista esta vacia")

    def agregar(self):
        try:
            self.a = int(self.n1.get())
            self.lista.append(self.a)
            self.listview.insert(self.listview.size()+1,self.a)
            self.n1.delete(0,END)
            self.b = int(self.n2.get())
            self.listview.insert(self.listview.size()+1,self.b)
            self.lista.append(self.b)
            self.n2.delete(0,END)
            print(self.lista)
            self.aux2 = self.lista[0]
            self.listaElementos.config(text=f'{self.lista}')

        except ValueError:
            messagebox.showerror("Error", "Algun dato no es un numero")
            return

    def salir(self):
        self.ven.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio() #mandar llamar a la ventana