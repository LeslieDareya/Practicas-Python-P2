from tkinter import *  
# Importa todas las funciones del módulo tkinter  
# Imports all functions from the tkinter module  

from tkinter import messagebox  
# Importa el módulo messagebox para mostrar mensajes emergentes  
# Imports messagebox to display pop-up messages  


class Principal():  
    # Define la clase principal que contiene toda la aplicación  
    # Defines the main class containing the whole application  

    def __init__(self):  
        # Constructor de la clase, inicializa los atributos y la ventana  
        # Class constructor, initializes attributes and window  

        self.ven = Tk()  
        # Crea la ventana principal  
        # Creates the main window  

        self.ven.title('Programa 6 con Ventanas')  
        # Asigna un título a la ventana  
        # Sets a title for the window  

        self.ven.geometry('650x350')  
        # Define el tamaño de la ventana  
        # Sets the window size  

        self.a = 0  
        # Variable para guardar el primer número  
        # Variable to store the first number  

        self.b = 0  
        # Variable para guardar el segundo número  
        # Variable to store the second number  

        self.lista = []  
        # Lista para guardar los números agregados  
        # List to store added numbers  

        self.aux1 = 0  
        # Variable auxiliar para encontrar el número mayor  
        # Auxiliary variable to find the largest number  

        self.aux2 = 0  
        # Variable auxiliar para encontrar el número menor  
        # Auxiliary variable to find the smallest number  

        self.cont = 0  
        # Contador usado en la función recursiva "mayor"  
        # Counter used in the recursive "mayor" function  


    def inicio(self):  
        # Función que crea los elementos visuales de la ventana  
        # Function that creates the visual elements of the window  

        l1 = Label(self.ven, text="Programa 9")  
        # Etiqueta con el título del programa  
        # Label showing the program title  
        l1.grid(row=1,column=2)  
        # Posiciona la etiqueta en la ventana  
        # Positions the label in the window  

        l2= Label(self.ven, text="Escribe un numero")  
        # Etiqueta para el primer número  
        # Label for the first number  
        l2.grid(row=3, column=1, padx=15 , pady=10)  
        # Coloca la etiqueta con separación  
        # Places the label with spacing  

        Label(self.ven, text="").grid(row=2,column=2)  
        # Etiqueta vacía usada para espacio  
        # Empty label used as spacer  

        self.n1 = Entry(self.ven)  
        # Caja de texto para el primer número  
        # Entry box for the first number  
        self.n1.grid(row=3, column=2)  
        # Posiciona la caja de texto  
        # Positions the entry box  

        l3 = Label(self.ven, text="Escribe otro numero")  
        # Etiqueta para el segundo número  
        # Label for the second number  
        l3.grid(row=1, column=2, padx=5 , pady=5)  
        # Coloca la etiqueta  
        # Places the label  

        Label(self.ven, text="").grid(row=4,column=2)  
        # Etiqueta vacía usada como separación  
        # Empty label used as spacing  

        self.n2 = Entry(self.ven)  
        # Caja de texto para el segundo número  
        # Entry box for the second number  
        self.n2.grid(row=5, column=2)  
        # Posiciona la caja de texto  
        # Positions the entry box  

        b1 = Button(self.ven,text="Agregar", command=self.agregar)  
        # Botón que llama a la función agregar  
        # Button that calls the add function  
        b1.grid(row=6, column=1, pady=10)  
        # Posiciona el botón en la ventana  
        # Positions the button in the window  

        b2 = Button(self.ven,text="Mayor", command=self.mayor)  
        # Botón que llama a la función para encontrar el mayor número  
        # Button that calls the function to find the largest number  
        b2.grid(row=6, column=2)  
        # Posiciona el botón en la ventana  
        # Positions the button in the window  

        b3 = Button(self.ven,text="Menor")  
        # Botón para encontrar el número menor (sin comando asignado aún)  
        # Button to find the smallest number (no command assigned yet)  
        b3.grid(row=6, column=3, padx=10)  
        # Posiciona el botón  
        # Positions the button  

        b4 = Button(self.ven,text="Salir", command=self.salir)  
        # Botón para cerrar la ventana  
        # Button to close the window  
        b4.grid(row=6, column=4, padx=25)  
        # Posiciona el botón en la ventana  
        # Positions the button in the window  

        self.listaElementos = Label(self.ven, text="")  
        # Etiqueta donde se mostrará la lista de números  
        # Label to display the list of numbers  
        self.listaElementos.grid(row=8,column=2, pady=15)  
        # Posiciona la etiqueta  
        # Positions the label  

        self.listview = Listbox(self.ven, height=10, width=15, bg='black', activestyle="dotbox", fg="red")  
        # Crea una lista visual donde se mostrarán los números agregados  
        # Creates a visual list to show added numbers  
        self.listview.grid(row=2,column=4)  
        # Posiciona la lista en la ventana  
        # Positions the listbox in the window  

        self.ven.mainloop()  
        # Mantiene la ventana abierta hasta que el usuario la cierre  
        # Keeps the window open until the user closes it  


    def mayor(self):  
        # Función recursiva para encontrar el número mayor  
        # Recursive function to find the largest number  

        if len(self.lista) > 0:  
            # Verifica si hay elementos en la lista  
            # Checks if the list has elements  

            if self.aux1 < self.lista[self.cont]:  
                # Si el elemento actual es mayor, lo guarda en aux1  
                # If current element is greater, store it in aux1  
                self.aux1 = self.lista[self.cont]  

            self.cont += 1  
            # Aumenta el contador  
            # Increments the counter  

            if len(self.lista)-1 <= self.cont:  
                # Si ya se recorrió la lista completa  
                # If the whole list has been checked  
                print(f'el mayor es {self.aux1}')  
                # Imprime el número mayor  
                # Prints the largest number  
                messagebox.showinfo('El mayor es', self.aux1)  
                # Muestra el número mayor en una ventana  
                # Displays the largest number in a messagebox  
                self.cont = 0  
                # Reinicia el contador  
                # Resets the counter  
            else:  
                return self.mayor()  
                # Llama de nuevo a la función (recursión)  
                # Calls the function again (recursion)  
        else:  
            print("Lista vacía")  
            # Muestra mensaje si no hay datos  
            # Displays message if list is empty  
            messagebox.showerror("Error","La lista está vacía")  
            # Ventana de error si la lista está vacía  
            # Error pop-up if list is empty  


    def menor(self):  
        # Función para encontrar el número menor  
        # Function to find the smallest number  

        if len(self.lista) > 0:  
            # Si la lista no está vacía  
            # If the list is not empty  
            for i in self.lista:  
                # Recorre todos los elementos  
                # Goes through all elements  
                if self.aux2 > i:  
                    # Si encuentra un número menor, lo guarda  
                    # If finds a smaller number, stores it  
                    self.aux2 = i  
            print(f'el menor es {self.aux2}')  
            # Imprime el menor  
            # Prints the smallest  
            messagebox.showinfo('El menor es', self.aux2)  
            # Muestra el menor en una ventana  
            # Shows the smallest in a messagebox  
        else:  
            messagebox.showerror("Error","La lista está vacía")  
            # Error si la lista no tiene elementos  
            # Error if the list has no elements  


    def agregar(self):  
        # Función para agregar los números a la lista  
        # Function to add numbers to the list  

        try:  
            self.a = int(self.n1.get())  
            # Convierte el primer número a entero  
            # Converts first input to integer  

            self.lista.append(self.a)  
            # Agrega el primer número a la lista  
            # Adds the first number to the list  

            self.listview.insert(self.listview.size()+1,self.a)  
            # Muestra el número en la lista visual  
            # Shows the number in the visual list  

            self.n1.delete(0,END)  
            # Limpia la caja de texto del primer número  
            # Clears the first entry box  

            self.b = int(self.n2.get())  
            # Convierte el segundo número a entero  
            # Converts second input to integer  

            self.listview.insert(self.listview.size()+1,self.b)  
            # Muestra el segundo número en la lista visual  
            # Shows the second number in the visual list  

            self.lista.append(self.b)  
            # Agrega el segundo número a la lista  
            # Adds the second number to the list  

            self.n2.delete(0,END)  
            # Limpia la caja de texto del segundo número  
            # Clears the second entry box  

            print(self.lista)  
            # Imprime la lista en consola  
            # Prints the list in console  

            self.aux2 = self.lista[0]  
            # Inicializa el valor del menor  
            # Initializes the smallest value  

            self.listaElementos.config(text=f'{self.lista}')  
            # Muestra la lista actual en pantalla  
            # Displays the current list on screen  

        except ValueError:  
            messagebox.showerror("Error", "Algún dato no es un número")  
            # Error si se ingresó algo que no es número  
            # Error if input is not a number  
            return self.agregar  
            # Regresa a la función agregar  
            # Returns to add function  


    def salir(self):  
        # Cierra la ventana principal  
        # Closes the main window  
        self.ven.destroy()  


if __name__ == "__main__":  
    # Punto de inicio del programa  
    # Program entry point  

    app = Principal()  
    # Crea una instancia de la clase Principal  
    # Creates an instance of the Principal class  

    app.inicio()  
    # Llama al método para iniciar la ventana  
    # Calls the method to start the window  

