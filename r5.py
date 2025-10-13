from tkinter import *
from tkinter import messagebox
from r5V import Validar  # Este será para múltiplos de 2

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Múltiplos de 2")
        self.ventana.geometry("450x300")

        self.listaMult2 = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Detección de Múltiplos de 2", font=("Arial", 12)).place(x=50, y=10)

        Label(self.ventana, text="Escribe un número:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=170, y=60, width=200)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=90, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=250, y=110, width=80)

        Label(self.ventana, text="Múltiplos de 2:").place(x=40, y=170)
        self.mostrarMult2 = Label(self.ventana, text="[]")
        self.mostrarMult2.place(x=160, y=170)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        resultado = self.valid.ValidarNumero(val)
        if isinstance(resultado, str):
            messagebox.showerror("Error", resultado)
        else:
            if resultado:  # Si es múltiplo de 2
                self.listaMult2.append(int(val))
                self.mostrarMult2.config(text=f"{self.listaMult2}")
                messagebox.showinfo("Resultado", f"{val} es múltiplo de 2")
            else:
                messagebox.showinfo("Resultado", f"{val} no es múltiplo de 2")
            self.dato.delete(0, END)

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    app = Principal()
    app.inicio()
