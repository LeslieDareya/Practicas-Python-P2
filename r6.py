from tkinter import *
from tkinter import messagebox
from r6V import Validar  # Archivo con las validaciones

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Múltiplos de 2 y 5")
        self.ventana.geometry("500x350")

        self.listaMult2 = []
        self.listaMult5 = []

        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Detección de Múltiplos de 2 y 5", font=("Arial", 12)).place(x=50, y=10)

        Label(self.ventana, text="Escribe un número:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=180, y=60, width=200)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=100, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=300, y=110, width=80)

        Label(self.ventana, text="Múltiplos de 2:").place(x=40, y=170)
        self.mostrarMult2 = Label(self.ventana, text="[]")
        self.mostrarMult2.place(x=160, y=170)

        Label(self.ventana, text="Múltiplos de 5:").place(x=40, y=220)
        self.mostrarMult5 = Label(self.ventana, text="[]")
        self.mostrarMult5.place(x=160, y=220)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        if val != "":
            resultado = self.valid.ValidarNumero(val)
            if isinstance(resultado, dict):
                if resultado['mult2']:
                    self.listaMult2.append(int(val))
                    self.mostrarMult2.config(text=f"{self.listaMult2}")
                    messagebox.showinfo("Resultado", f"{val} es múltiplo de 2")
                else:
                    messagebox.showinfo("Resultado", f"{val} no es múltiplo de 2")

                if resultado['mult5']:
                    self.listaMult5.append(int(val))
                    self.mostrarMult5.config(text=f"{self.listaMult5}")
                    messagebox.showinfo("Resultado", f"{val} es múltiplo de 5")
                else:
                    messagebox.showinfo("Resultado", f"{val} no es múltiplo de 5")
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