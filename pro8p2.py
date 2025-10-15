from tkinter import *
from tkinter import messagebox

class Principal():
    # Clase principal de la aplicación
    # Main class of the application
    def __init__(self):
        # Constructor: crea la ventana y variables iniciales
        # Constructor: creates the window and initial variables
        self.ven = Tk()  # Libreria / Main window object
        self.ven.title('Programa 6 con Ventanas')  # Titulo de la ventana / Window title
        self.ven.geometry('650x350')  # Tamaño de la ventana / Window size
        self.a = 0
        self.b = 0
        self.lista = []          # Lista para guardar los números ingresados / List to store entered numbers
        self.aux1 = 0            # Auxiliar para mayor / Helper for max value
        self.aux2 = 0            # Auxiliar para menor / Helper for min value
        self.cont = 0            # (no usado en versión iterativa actual) / (not used in current iterative version)

    def inicio(self):
        # Crea y posiciona widgets en la ventana usando grid
        # Create and place widgets in the window using grid
        l1 = Label(self.ven, text="Programa 9")
        l1.grid(row=1,column=2)

        l2= Label(self.ven, text="Escribe un numero")
        l2.grid(row=3, column=1, padx=15 , pady=10)
        Label(self.ven, text="").grid(row=2,column=2)  # Espaciador / Spacer

        self.n1 = Entry(self.ven)  # Entrada para primer número / Entry for first number
        self.n1.grid(row=3, column=2)
        
        l3 = Label(self.ven, text="Escribe otro numero")
        l3.grid(row=1, column=2, padx=5 , pady=5)
        Label(self.ven, text="").grid(row=4,column=2)  # Espaciador / Spacer

        self.n2 = Entry(self.ven)  # Entrada para segundo número / Entry for second number
        self.n2.grid(row=5, column=2)

        # Botones: Agregar, Mayor, Menor, Salir
        # Buttons: Add, Max, Min, Exit
        b1 = Button(self.ven,text="Agregar", command=self.agregar)
        b1.grid(row=6, column=1, pady=10)
        b2 = Button(self.ven,text="Mayor", command=self.mayor)
        b2.grid(row=6, column=2)
        b3 = Button(self.ven,text="Menor", command=self.menor)
        b3.grid(row=6, column=3, padx=10)
        b4 = Button(self.ven,text="Salir", command=self.salir)
        b4.grid(row=6, column=4, padx=25)

        self.listaElementos = Label(self.ven, text="")  # Label para mostrar la lista completa
        self.listaElementos.grid(row=8,column=2, pady=15)

        # Listbox para mostrar cada elemento agregado visualmente
        # Listbox to visually display each added element
        self.listview = Listbox(self.ven, height=10,
                                width=15, bg='black',
                                activestyle= "dotbox", fg="red")
        self.listview.grid(row=2,column=4)

        self.ven.mainloop()  # Inicia el loop principal / Start the main loop

    def mayor(self):
        # Calcula el mayor valor dentro de self.lista (iterativo)
        # Compute the largest value in self.lista (iterative)
        if len(self.lista) > 0:
            self.aux1 = self.lista[0]  # Inicializa aux1 con el primer elemento / Init aux1 with first element
            for i in self.lista:
                if i > self.aux1:
                    self.aux1 = i
            print(f'el mayor es {self.aux1}')  # Salida por consola (debug)
            messagebox.showinfo('El mayor es', f'{self.aux1}')  # Muestra el mayor en un messagebox
        else:
            print("Lista vacia")
            messagebox.showerror("Error","La lista esta vacia")  # Error si la lista está vacía

    def menor(self):
        # Calcula el menor valor dentro de self.lista (iterativo)
        # Compute the smallest value in self.lista (iterative)
        if len(self.lista) > 0:
            self.aux2 = self.lista[0]  # Inicializa aux2 con el primer elemento / Init aux2 with first element
            for i in self.lista:
                if i < self.aux2:
                    self.aux2 = i
            print(f'el menor es {self.aux2}')  # Salida por consola (debug)
            messagebox.showinfo('El menor es', f'{self.aux2}')  # Muestra el menor en un messagebox
        else:
            messagebox.showerror("Error","La lista esta vacia")  # Error si la lista está vacía

    def agregar(self):
        # Agrega dos números (n1 y n2) a la lista y actualiza la vista
        # Adds two numbers (n1 and n2) to the list and updates the view
        try:
            self.a = int(self.n1.get())
            self.lista.append(self.a)  # Añade primer número a la lista / Append first number
            self.listview.insert(self.listview.size()+1,self.a)  # Inserta en Listbox
            self.n1.delete(0,END)

            self.b = int(self.n2.get())
            self.listview.insert(self.listview.size()+1,self.b)  # Inserta segundo número en Listbox
            self.lista.append(self.b)  # Añade segundo número a la lista
            self.n2.delete(0,END)

            print(self.lista)  # Debug: imprime lista completa / Debug: print full list
            self.aux2 = self.lista[0]  # Se puede usar como inicialización para menor / Can be used for min init
            self.listaElementos.config(text=f'{self.lista}')  # Muestra la lista en la etiqueta
        except ValueError:
            # Si alguna entrada no es un entero, muestra error
            # If any input is not an integer, show error
            messagebox.showerror("Error", "Algun dato no es un numero")
            return

    def salir(self):
        # Cierra la ventana principal / Close the main window
        self.ven.destroy()


if __name__ == "__main__":
    # Punto de entrada del programa / Program entry point
    app = Principal()
    app.inicio()  # Inicia la aplicación / Start the application
