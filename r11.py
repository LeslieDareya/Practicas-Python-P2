from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("500x400")
        self.ventana.title("Registro de Personas")

        # Lista que almacena todos los registros como diccionarios
        # List that stores all records as dictionaries
        self.registros = []

        # Interfaz: etiquetas y cajas de texto
        Label(self.ventana, text="Nombre:").place(x=50, y=20)
        self.nombre_entry = Entry(self.ventana)
        self.nombre_entry.place(x=150, y=20, width=200)

        Label(self.ventana, text="Edad:").place(x=50, y=60)
        self.edad_entry = Entry(self.ventana)
        self.edad_entry.place(x=150, y=60, width=200)

        Label(self.ventana, text="Correo:").place(x=50, y=100)
        self.correo_entry = Entry(self.ventana)
        self.correo_entry.place(x=150, y=100, width=200)

        # Botón para agregar registro
        Button(self.ventana, text="Agregar", command=self.agregar_registro).place(x=150, y=140, width=200)

        # Botones para ordenar la lista
        Button(self.ventana, text="Ordenar por Nombre", command=lambda: self.ordenar("nombre")).place(x=50, y=180, width=140)
        Button(self.ventana, text="Ordenar por Edad", command=lambda: self.ordenar("edad")).place(x=200, y=180, width=140)
        Button(self.ventana, text="Ordenar por Correo", command=lambda: self.ordenar("correo")).place(x=350, y=180, width=140)

        # Label para mostrar los registros
        self.mostrar = Label(self.ventana, text="", justify=LEFT)
        self.mostrar.place(x=50, y=220)

        self.ventana.mainloop()

    def agregar_registro(self):
        # Leer datos de las cajas de texto
        nombre = self.nombre_entry.get().strip()
        edad = self.edad_entry.get().strip()
        correo = self.correo_entry.get().strip()

        # Validación básica: no dejar campos vacíos
        if nombre == "" or edad == "" or correo == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Validar que edad sea un número
        if not edad.isdigit():
            messagebox.showerror("Error", "Edad debe ser un número")
            return

        # Crear un diccionario con los datos
        registro = {"nombre": nombre, "edad": int(edad), "correo": correo}

        # Agregar a la lista
        self.registros.append(registro)

        # Limpiar las cajas de texto
        self.nombre_entry.delete(0, END)
        self.edad_entry.delete(0, END)
        self.correo_entry.delete(0, END)

        # Mostrar registros concatenados
        self.mostrar_registros()

    def mostrar_registros(self):
        # Concatenar los registros en un solo texto
        texto = ""
        for r in self.registros:
            texto += f"Nombre: {r['nombre']}, Edad: {r['edad']}, Correo: {r['correo']}\n"
        self.mostrar.config(text=texto)

    def ordenar(self, campo):
        # Ordena la lista por el campo indicado
        self.registros.sort(key=lambda x: x[campo])
        self.mostrar_registros()


# Punto de entrada
if __name__ == "__main__":
    app = Principal()
