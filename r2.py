from tkinter import *
from tkinter import messagebox
from r2V import Validar

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Clasificador de Números")
        self.ventana.geometry("400x300")

        self.listaPar = []
        self.listaImpar = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Clasificador de Números Pares e Impares", font=("Arial", 11)).place(x=40, y=10)
        
        Label(self.ventana, text="Escribe un número:").place(x=50, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=180, y=60, width=120)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=60, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=260, y=110, width=80)

        Label(self.ventana, text="Lista Pares:").place(x=50, y=170)
        self.mostrarPares = Label(self.ventana, text="[]")
        self.mostrarPares.place(x=150, y=170)

        Label(self.ventana, text="Lista Impares:").place(x=50, y=200)
        self.mostrarImpares = Label(self.ventana, text="[]")
        self.mostrarImpares.place(x=150, y=200)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        if val != "":
            tipo = self.valid.ValidarNumero(val)
            if tipo == "Par":
                self.listaPar.append(int(val))
                self.mostrarPares.config(text=f"{self.listaPar}")
                messagebox.showinfo("Resultado", f"El número {val} es PAR")
            elif tipo == "Impar":
                self.listaImpar.append(int(val))
                self.mostrarImpares.config(text=f"{self.listaImpar}")
                messagebox.showinfo("Resultado", f"El número {val} es IMPAR")
            else:
                messagebox.showerror("Error", tipo)
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()