from tkinter import *
from tkinter import messagebox
from r1V import Validar

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Conversor de Cadenas")
        self.ventana.geometry("400x300")
        self.listaMayus = []
        self.listaMinus = []
        self.valid = Validar()

    def inicio(self):
        Label(self.ventana, text="Conversor de texto a MAY/MIN", font=("Arial", 12)).place(x=80, y=10)
        
        Label(self.ventana, text="Escribe una palabra:").place(x=40, y=60)
        self.dato = Entry(self.ventana)
        self.dato.place(x=180, y=60, width=150)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=40, y=110, width=80)
        Button(self.ventana, text="Mayúsculas", command=self.convertirMayus).place(x=130, y=110, width=100)
        Button(self.ventana, text="Minúsculas", command=self.convertirMinus).place(x=240, y=110, width=100)
        Button(self.ventana, text="Salir", command=self.salir).place(x=160, y=160, width=80)

        Label(self.ventana, text="Lista Mayúsculas:").place(x=40, y=210)
        self.mostrarMayus = Label(self.ventana, text="[]")
        self.mostrarMayus.place(x=160, y=210)

        Label(self.ventana, text="Lista Minúsculas:").place(x=40, y=240)
        self.mostrarMinus = Label(self.ventana, text="[]")
        self.mostrarMinus.place(x=160, y=240)

        self.ventana.mainloop()

    def agregar(self):
        val = self.dato.get()
        if val != "":
            tipo = self.valid.ValidarAscii(val)
            messagebox.showinfo("Tipo de dato", f"El valor contiene: {tipo}")
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def convertirMayus(self):
        val = self.dato.get()
        if val != "":
            valMayus = val.upper()
            self.listaMayus.append(valMayus)
            self.mostrarMayus.config(text=f"{self.listaMayus}")
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def convertirMinus(self):
        val = self.dato.get()
        if val != "":
            valMinus = val.lower()
            self.listaMinus.append(valMinus)
            self.mostrarMinus.config(text=f"{self.listaMinus}")
            self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "Caja de texto vacía")

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()