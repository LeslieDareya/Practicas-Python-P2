from tkinter import *
#Importamos las librerías necesarias de tkinter
#Import the necessary libraries from tkinter
from tkinter import messagebox
#Para mostrar mensajes emergentes
#To show pop-up messages

class Principal():
#Definimos la clase principal de la aplicación
#Define the main application class
    def __init__(self):
        #Creamos la ventana principal
        #Create the main window
        self.ven = Tk()
        self.ven.title('Programa 6 con Ventanas GRID')
        #Título de la ventana / Window title
        self.ven.geometry('450x250')
        #Tamaño de la ventana / Window size

        #Inicializamos variables
        #Initialize variables
        self.a = 0
        self.b = 0
        self.lista = []
        #Lista donde se guardarán los números
        #List to store numbers
        # self.aux1 = 0  <-- Se inicializará dentro de mayor()
        # self.aux2 = 0  <-- Se inicializará dentro de menor()
        # self.cont = 0  <-- Ya no es necesario para la búsqueda iterativa simple.

    def inicio(self):
        #Función que inicia y construye la interfaz gráfica
        #Function that builds the GUI
        #Etiqueta del título del programa / Program title label
        l = Label(self.ven, text="Programa 9")
        l.grid(row=1, column=2)
        #Colocamos con grid / Place using grid layout

        l2 = Label(self.ven, text="Escribe un numero")
        l2.grid(row=3, column=1, padx=15, pady=10)
        #Etiqueta pidiendo el primer número / Label asking for first number

        Label(self.ven, text=" ").grid(row=2, column=2)
        #Etiqueta vacía para crear espacio / Empty label for spacing

        self.n1 = Entry(self.ven)
        self.n1.grid(row=3, column=2)
        #Campo de entrada del primer número / Entry field for first number

        l3 = Label(self.ven, text="Escribe otro numero")
        l3.grid(row=5, column=1, pady=5)
        #Etiqueta para el segundo número / Label for second number

        Label(self.ven, text=" ").grid(row=4, column=2)
        #Otra etiqueta vacía para espacio / Another empty label for spacing

        self.n2 = Entry(self.ven)
        self.n2.grid(row=5, column=2)
        #Campo de entrada del segundo número / Entry field for second number

        b1 = Button(self.ven, text="Agregar", command=self.agregar)
        b1.grid(row=6, column=1, pady=10)
        #Botón para agregar los números a la lista / Button to add numbers to the list

        b2 = Button(self.ven, text="Mayor", command=self.mayor)
        b2.grid(row=6, column=2)
        #Botón para encontrar el mayor / Button to find the largest number

        b3 = Button(self.ven, text="Menor", command=self.menor)
        b3.grid(row=6, column=3, padx=10)
        #Botón para encontrar el menor / Button to find the smallest number

        b4 = Button(self.ven, text="Salir", command=self.salir)
        b4.grid(row=6, column=4, padx=25)
        #Botón para salir del programa / Button to exit the program

        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.grid(row=3, column=3, pady=15)
        #Etiqueta donde se mostrará la lista / Label to display the list

        self.listview = Listbox(self.ven, height=10,
                               width=15, bg='black',
                               activestyle='dotbox', fg='white')
        self.listview.grid(row=2, column=4)
        #Listbox para mostrar los elementos de la lista visualmente
        #Listbox to show the numbers visually

        self.ven.mainloop()
        #Ejecuta el bucle principal de la ventana / Run the main window loop

    def agregar(self):
        #Función para agregar números a la lista
        #Function to add numbers to the list
        try:
            self.a = int(self.n1.get())
            #Lee el texto de n1, lo convierte a int y lo guarda en self.a.
            #Reads text from n1, converts to int and stores in self.a.
            self.lista.append(self.a)
            #Añade el número a la lista. / Appends the number to the list.
            self.listview.insert(self.listview.size(), self.a)
            #Inserta visualmente el número en el Listbox.
            #Inserts the number into the Listbox for display.
            self.n1.delete(0, END)
            #Borra el contenido del campo n1.
            #Clears the n1 entry field.

            self.b = int(self.n2.get())
            #Lee y convierte el valor de n2 a entero.
            #Reads and converts the value of n2 to int.
            self.listview.insert(self.listview.size()+1, self.b)
            #Inserta el segundo número en el Listbox.
            #Inserts the second number into the Listbox.
            self.lista.append(self.b)
            #Añade el segundo número a la lista.

            self.n2.delete(0, END)
            #Borra el campo n2.
            #Clears the n2 entry.

            print(self.lista)
            #Imprime la lista completa en la consola (debug).
            #Prints the full list to console (debug).

            self.listaElementos.config(text=f'{self.lista}')
            #Actualiza la etiqueta que muestra la lista.
            #Updates the label that displays the list.

        except ValueError:
            messagebox.showerror("Error","Algun dato no es numero")
            # return self.agregar # <-- Se eliminó el 'return' inusual
            return # <-- Solo sale de la función

    def mayor(self):
        #Función para obtener el número mayor
        #Function to find the largest number
        if len(self.lista) > 0:
            #Verifica que la lista no esté vacía / Checks that the list is not empty.
            self.aux1 = self.lista[0] # <-- Inicializa aux1 con el primer elemento.
            for i in self.lista: # <-- Itera sobre la lista.
                if self.aux1 < i:
                    #Compara el auxiliar aux1 con el elemento.
                    #Compares aux1 with the element.
                    self.aux1 = i
                    #Si el elemento actual es mayor, actualiza aux1.
                    #If current element is larger, update aux1.

            print(f'El mayor es {self.aux1}')
            #Imprime en consola el mayor encontrado.
            #Prints the found maximum to console.
            messagebox.showinfo('El mayor', self.aux1)
            #Muestra el mayor en un messagebox.
            #Shows the maximum in a messagebox.
        else:
            messagebox.showerror("Error", "La lista esta vacia")
            #Si la lista está vacía / If the list is empty

    def menor(self):
        #Función para obtener el número menor
        #Function to find the smallest number
        if len(self.lista) > 0:
            #Comprueba que la lista no esté vacía.
            #Checks that the list is not empty.
            self.aux2 = self.lista[0] # <-- Inicializa aux2 con el primer elemento.
            for i in self.lista:
                #Recorre cada elemento i dentro de la lista.
                #Iterates through each element i in the list.
                if self.aux2 > i:
                    self.aux2 = i
                    #Si aux2 es mayor que el elemento actual, actualiza aux2 al valor más pequeño encontrado.
                    #Update aux2 to the smaller value found.
            print(f'El menor es {self.aux2}')
            #Imprime el menor en consola.
            #Prints the smallest to console.
            messagebox.showinfo('El menor', self.aux2)
            #Muestra un messagebox con el menor
            #Shows a messagebox with the smallest
        else:
            messagebox.showerror("Error", "La lista esta vacia")
            #Si vacía, muestra error / If empty, show error.

    def salir(self):
        #Método para cerrar la ventana / Method to close the window.
        self.ven.destroy()
        #Destruye la ventana y termina la aplicación.
        #Destroys the window and ends the application.

if __name__ == '__main__':
    app = Principal()
    #Crea la instancia de la clase Principal.
    #Creates an instance of the Principal class.
    app.inicio()
    #Llama a inicio() para construir la interfaz y arrancar la app.
    #Calls inicio() to build the GUI and start the app.
