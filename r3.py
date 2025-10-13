from tkinter import *
from tkinter import messagebox
from r3V import Validar

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Clasificador de Primos")
        self.ventana.geometry("420x320")

        self.listaPrimo = []
        self.listaNoPrimo = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Clasificador de Números Primos", font=("Arial", 12)).place(x=80, y=10)

        Label(self.ventana, text="Escribe un número:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=170, y=60, width=150)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=90, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=250, y=110, width=80)

        Label(self.ventana, text="Lista Primos:").place(x=40, y=170)
        self.mostrarPrimos = Label(self.ventana, text="[]", anchor="w", justify=LEFT)
        self.mostrarPrimos.place(x=140, y=170)

        Label(self.ventana, text="Lista No Primos:").place(x=40, y=210)
        self.mostrarNoPrimos = Label(self.ventana, text="[]", anchor="w", justify=LEFT)
        self.mostrarNoPrimos.place(x=140, y=210)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        if val != "":
            tipo = self.valid.ValidarNumero(val)
            if tipo == "Primo":
                self.listaPrimo.append(int(val))
                self.mostrarPrimos.config(text=f"{self.listaPrimo}")
                messagebox.showinfo("Resultado", f"El número {val} es PRIMO")
            elif tipo == "No Primo":
                self.listaNoPrimo.append(int(val))
                self.mostrarNoPrimos.config(text=f"{self.listaNoPrimo}")
                messagebox.showinfo("Resultado", f"El número {val} NO es primo")
            else:
                # mensaje de error retornado por ValidarNumero (ej. no es entero)
                messagebox.showerror("Error", tipo)
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()