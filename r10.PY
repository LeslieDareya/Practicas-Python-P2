from tkinter import *
from tkinter import messagebox

# Clase de validación de números
class Validar():
    def __init__(self):
        pass

    def ValidarNumero(self, valor):
        if not valor.isdigit():
            return "No es un número válido"
        return int(valor)

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Ordenar Números Descendente")
        self.ventana.geometry("500x350")

        self.listaNumeros = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Ordenar Números Descendente", font=("Arial", 12)).place(x=50, y=10)

        Label(self.ventana, text="Escribe un número:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=180, y=60, width=200)

        Button(self.ventana, text="Agregar a lista", command=self.agregar).place(x=50, y=110, width=120)
        Button(self.ventana, text="Ordenar", command=self.ordenar).place(x=200, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=320, y=110, width=80)

        Label(self.ventana, text="Lista de números:").place(x=40, y=170)
        self.mostrarLista = Label(self.ventana, text="[]")
        self.mostrarLista.place(x=160, y=170)

        Label(self.ventana, text="Suma total:").place(x=40, y=220)
        self.mostrarSuma = Label(self.ventana, text="0")
        self.mostrarSuma.place(x=140, y=220)

        self.ventana.mainloop()

    def agregar(self):
        if len(self.listaNumeros) >= 5:
            messagebox.showwarning("Aviso", "Ya ingresaste 5 números")
            return
        val = self.dato.get()
        resultado = self.valid.ValidarNumero(val)
        if isinstance(resultado, str):  # Error
            messagebox.showerror("Error", resultado)
        else:
            self.listaNumeros.append(resultado)
            self.mostrarLista.config(text=f"{self.listaNumeros}")
            self.dato.delete(0, END)

    def ordenar(self):
        if not self.listaNumeros:
            messagebox.showwarning("Aviso", "La lista está vacía")
            return
        self.listaNumeros.sort(reverse=True)
        self.mostrarLista.config(text=f"{self.listaNumeros}")
        total = sum(self.listaNumeros)
        self.mostrarSuma.config(text=f"{total}")
        messagebox.showinfo("Resultado", f"Lista ordenada descendente.\nSuma total: {total}")

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    app = Principal()
    app.inicio()
