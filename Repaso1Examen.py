# principal.py
from tkinter import *
from tkinter import messagebox
from validarRepaso import Validar  # Importamos la clase de validaciones

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.lista = []
        self.valid = Validar()  # Instancia de la clase Validar

    def inicio(self):
        Label(self.ventana, text="Programa de Python con TKInter").place(x=50, y=20)

        # Caja de texto para ingresar datos
        self.dato = Entry(self.ventana)
        self.dato.place(x=150, y=50, width=150)

        # Botón para validar datos
        Button(self.ventana, text="Validar", command=self.ValidarDatos).place(x=150, y=90, width=150)

        # Label para mostrar la lista de datos ingresados
        self.mostrar = Label(self.ventana, text="Ejemplo")
        self.mostrar.place(x=20, y=150)

        self.ventana.mainloop()

    def ValidarDatos(self):
        val = self.dato.get()
        if val != "":
            self.lista.append(val)
            self.dato.delete(0, END)
            self.mostrar.config(text=f'{self.lista}')

            # Llamamos a la validación ASCII de la clase Validar
            respuesta = self.valid.ValidarAscii(val)
            messagebox.showinfo("Validar datos", f'El dato es: {respuesta}')
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

# Punto de entrada del programa
if __name__ == "__main__":
    app = Principal()
    app.inicio()
