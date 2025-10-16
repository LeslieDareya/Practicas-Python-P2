from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        # Crear la ventana principal
        # Create the main window
        self.ventana = Tk()
        self.ventana.title("Contar letras (recursivo)")  # Título de la ventana / Window title
        self.ventana.geometry("450x300")                 # Tamaño de la ventana / Window size

        self.lista_palabras = []   # Lista para guardar las palabras / List to store the entered words

    def inicio(self):
        # Etiqueta para indicar qué escribir
        # Label to instruct the user
        l1 = Label(self.ventana, text="Escribe una palabra o frase:")
        l1.grid(row=1, column=2, pady=10)

        # Cuadro de texto para ingresar la palabra o frase
        # Text entry box to input a word or phrase
        self.txt = Entry(self.ventana, width=40)
        self.txt.grid(row=2, column=2, pady=5)

        # Botón para contar letras
        # Button to count letters
        b1 = Button(self.ventana, text="Contar", command=self.contar)
        b1.grid(row=3, column=1, padx=10, pady=10)

        # Botón para agregar palabra a la lista
        # Button to add the entered word to the list
        b2 = Button(self.ventana, text="Agregar", command=self.agregar)
        b2.grid(row=3, column=2, padx=10, pady=10)

        # Botón para salir del programa
        # Button to close the application
        b3 = Button(self.ventana, text="Salir", command=self.salir)
        b3.grid(row=3, column=3, padx=10, pady=10)

        # Etiqueta para mostrar la lista completa de palabras
        # Label to display the list of entered words
        self.lista_label = Label(self.ventana, text="")
        self.lista_label.grid(row=5, column=2, pady=10)

        # Inicia el bucle principal de la interfaz gráfica
        # Starts the main GUI loop
        self.ventana.mainloop()

    def contar_letras(self, cadena):
        # Función recursiva para contar las letras de una cadena
        # Recursive function to count characters in a string
        if cadena == "":
            return 0
        else:
            return 1 + self.contar_letras(cadena[1:])

    def contar(self):
        # Obtiene el texto del cuadro de entrada
        # Get the text from the input box
        texto = self.txt.get()
        if texto == "":
            messagebox.showerror("Error", "Escribe algo primero.")  # Muestra error si está vacío / Show error if empty
            return
        # Llama a la función recursiva y muestra el resultado
        # Calls the recursive function and displays the result
        cantidad = self.contar_letras(texto)
        messagebox.showinfo("Resultado", f"La cadena tiene {cantidad} caracteres.")  # Display the result

    def agregar(self):
        # Obtiene la palabra escrita
        # Get the entered word
        palabra = self.txt.get()
        if palabra == "":
            messagebox.showerror("Error", "No se puede agregar texto vacío.")  # Error if empty / Show error if empty text
            return
        
        # Agrega la palabra a la lista
        # Add the word to the list
        self.lista_palabras.append(palabra)
        self.txt.delete(0, END)  # Limpia el cuadro de texto / Clear the input box

        # Muestra la lista completa en la etiqueta
        # Display the entire list in the label
        self.lista_label.config(text=str(self.lista_palabras))

    def salir(self):
        # Cierra la ventana principal
        # Close the main window
        self.ventana.destroy()


# Punto de entrada del programa
# Program entry point
if __name__ == "__main__":
    app = Principal()
    app.inicio()


