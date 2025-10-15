from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Contar letras (recursivo)")
        self.ventana.geometry("450x300")

        self.lista_palabras = []   # Lista para guardar las palabras

    def inicio(self):
        # Etiqueta y cuadro de texto
        l1 = Label(self.ventana, text="Escribe una palabra o frase:")
        l1.grid(row=1, column=2, pady=10)

        self.txt = Entry(self.ventana, width=40)
        self.txt.grid(row=2, column=2, pady=5)

        # Botones
        b1 = Button(self.ventana, text="Contar", command=self.contar)
        b1.grid(row=3, column=1, padx=10, pady=10)

        b2 = Button(self.ventana, text="Agregar", command=self.agregar)
        b2.grid(row=3, column=2, padx=10, pady=10)

        b3 = Button(self.ventana, text="Salir", command=self.salir)
        b3.grid(row=3, column=3, padx=10, pady=10)

        # Label donde se mostrará la lista completa
        self.lista_label = Label(self.ventana, text="")
        self.lista_label.grid(row=5, column=2, pady=10)

        self.ventana.mainloop()

    def contar_letras(self, cadena):
        # Función recursiva
        if cadena == "":
            return 0
        else:
            return 1 + self.contar_letras(cadena[1:])

    def contar(self):
        texto = self.txt.get()
        if texto == "":
            messagebox.showerror("Error", "Escribe algo primero.")
            return
        cantidad = self.contar_letras(texto)
        messagebox.showinfo("Resultado", f"La cadena tiene {cantidad} caracteres.")

    def agregar(self):
        palabra = self.txt.get()
        if palabra == "":
            messagebox.showerror("Error", "No se puede agregar texto vacío.")
            return
        
        # Agrega palabra a la lista
        self.lista_palabras.append(palabra)
        self.txt.delete(0, END)

        # Muestra toda la lista en el label
        self.lista_label.config(text=str(self.lista_palabras))

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()

