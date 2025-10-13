from tkinter import *
from tkinter import messagebox

# Clase de validación para palabras
class Validar():
    def __init__(self):
        pass

    def EsPalindromo(self, valor):
        if not valor.isalpha():
            return "La palabra debe contener solo letras"
        valor = valor.lower()  # Ignorar mayúsculas/minúsculas
        return valor == valor[::-1]  # Retorna True si es palíndromo

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Verificador de Palíndromos")
        self.ventana.geometry("450x300")

        self.listaPalindromos = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Verificador de Palíndromos", font=("Arial", 12)).place(x=50, y=10)

        Label(self.ventana, text="Escribe una palabra:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=170, y=60, width=200)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=90, y=110, width=80)
        Button(self.ventana, text="Salir", command=self.salir).place(x=250, y=110, width=80)

        Label(self.ventana, text="Palíndromos encontrados:").place(x=40, y=170)
        self.mostrarPalindromos = Label(self.ventana, text="[]")
        self.mostrarPalindromos.place(x=180, y=170)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        resultado = self.valid.EsPalindromo(val)
        if isinstance(resultado, str):  # Error de validación
            messagebox.showerror("Error", resultado)
        else:
            if resultado:  # Es palíndromo
                self.listaPalindromos.append(val)
                self.mostrarPalindromos.config(text=f"{self.listaPalindromos}")
                messagebox.showinfo("Resultado", f"{val} es un palíndromo")
            else:
                messagebox.showinfo("Resultado", f"{val} no es un palíndromo")
            self.dato.delete(0, END)

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    app = Principal()
    app.inicio()

