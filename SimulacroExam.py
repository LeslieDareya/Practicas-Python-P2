#Hacer un programa que mediante una ventana tkn}inter realice lo siguiente
#1. La ventana debe contener 3 cajas de texto y 2 botones
#2. El programa validara que la primer caja de texto solo permita letras minusculas, en la segunda caja solo 
#letras mayusculas y en la tercera solo numeros, dicha validacion la realizara el primer boton,
#si algun dato es incorrecto mostrara un mensaje de error y se borrara la caja de texto.
#3. Unicamente cuando las 3 cajas de texto tengan informacion y esten validadas se concatenaran y se agregaran a una lista visual
#tres cajas de texto arriba, un label en medio y dos botones abajo validar y agregar y una list box a un lado 
# si algun lado no es correcto borra solo esa casilla y la vuelve a pedir y si esta correcto al presionar el boton agregar se agrega a la list box 
#con los 3 datos concatenados y el label muestra 1. al terminar este proceso se borran los datos de las cajas de texto para
#ingresar un nuevo registro y repite el proceso, valida, pide corregir si esta mal y si es correcto lo agrega al list box
# con los datos concatenados y el label muestra 2. asi sicesivamente con todos los registros deseados

# validarRepaso.py
# Este archivo contiene todas las funciones de validación
# This file contains all the validation functions

# principal.py
# Este archivo contiene la interfaz gráfica y usa las validaciones del otro archivo
# This file contains the GUI and uses the validations from the other file

from tkinter import *
from tkinter import messagebox
from validarRepaso import Validar  # Importamos la clase de validaciones / Import validation class

class Principal():
    def __init__(self):
        # Crear la ventana principal / Create the main window
        self.ventana = Tk()
        self.ventana.geometry("400x200")

        # Lista para almacenar todos los datos ingresados / List to store all input data
        self.lista = []

        # Instancia de la clase Validar / Instance of the Validar class
        self.valid = Validar()

    def inicio(self):
        # Etiqueta principal de la ventana / Main label of the window
        Label(self.ventana, text="Programa de Python con TKInter").place(x=50, y=20)

        # Caja de texto para ingresar datos / Entry box to input data
        self.dato = Entry(self.ventana)
        self.dato.place(x=150, y=50, width=150)

        # Botón que llama a la función ValidarDatos / Button that calls the ValidarDatos function
        Button(self.ventana, text="Validar", command=self.ValidarDatos).place(x=150, y=90, width=150)

        # Label que mostrará los datos ingresados / Label to display the entered data
        self.mostrar = Label(self.ventana, text="Ejemplo")
        self.mostrar.place(x=20, y=150)

        # Ciclo principal de la ventana / Main loop of the window
        self.ventana.mainloop()

    def ValidarDatos(self):
        # Obtener el valor de la caja de texto / Get the value from the entry box
        val = self.dato.get()

        if val != "":
            # Agregar a la lista y limpiar la caja de texto / Add to the list and clear the entry
            self.lista.append(val)
            self.dato.delete(0, END)

            # Mostrar la lista en el label / Show the list in the label
            self.mostrar.config(text=f'{self.lista}')

            # Llamar a la función de validación ASCII / Call the ASCII validation function
            respuesta = self.valid.ValidarAscii(val)
            messagebox.showinfo("Validar datos", f'El dato es: {respuesta}')

        else:
            # Mensaje de error si la caja está vacía / Error message if entry is empty
            messagebox.showerror("Error", "Caja de texto vacía")

# Punto de entrada principal / Main entry point
if __name__ == "__main__":
    app = Principal()
    app.inicio()

