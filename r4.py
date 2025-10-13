from tkinter import *
from tkinter import messagebox
from r4V import Validar

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Extracción de Vocales")
        self.ventana.geometry("450x300")

        self.listaVocales = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Extracción de Vocales de una Cadena", font=("Arial", 12)).place(x=50, y=10)

        Label(self.ventana, text="Escribe una cadena:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=170, y=60, width=200)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=90, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=250, y=110, width=80)

        Label(self.ventana, text="Vocales Extraídas:").place(x=40, y=170)
        self.mostrarVocales = Label(self.ventana, text="[]")
        self.mostrarVocales.place(x=160, y=170)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        if val != "":
            resultado = self.valid.ValidarCadena(val)
            if isinstance(resultado, list):
                self.listaVocales.extend(resultado)
                self.mostrarVocales.config(text=f"{self.listaVocales}")
                messagebox.showinfo("Resultado", f"Vocales extraídas: {resultado}")
            else:
                messagebox.showerror("Error", resultado)
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()