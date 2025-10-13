from tkinter import *
from tkinter import messagebox
from r8V import Tienda  # Archivo con la lógica de la tienda

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Tienda de Abarrotes")
        self.ventana.geometry("600x400")

        self.tienda = Tienda()

    def inicio(self):
        Label(self.ventana, text="Tienda de Abarrotes", font=("Arial", 14)).place(x=200, y=10)

        # Productos
        Label(self.ventana, text="Producto 1:").place(x=40, y=50)
        self.prod1 = Entry(self.ventana)
        self.prod1.place(x=150, y=50, width=200)
        Label(self.ventana, text="Precio:").place(x=370, y=50)
        self.precio1 = Entry(self.ventana)
        self.precio1.place(x=430, y=50, width=100)

        Label(self.ventana, text="Producto 2:").place(x=40, y=90)
        self.prod2 = Entry(self.ventana)
        self.prod2.place(x=150, y=90, width=200)
        Label(self.ventana, text="Precio:").place(x=370, y=90)
        self.precio2 = Entry(self.ventana)
        self.precio2.place(x=430, y=90, width=100)

        Label(self.ventana, text="Producto 3:").place(x=40, y=130)
        self.prod3 = Entry(self.ventana)
        self.prod3.place(x=150, y=130, width=200)
        Label(self.ventana, text="Precio:").place(x=370, y=130)
        self.precio3 = Entry(self.ventana)
        self.precio3.place(x=430, y=130, width=100)

        # Botones
        Button(self.ventana, text="Agregar Productos", command=self.agregar).place(x=50, y=180, width=140)
        Button(self.ventana, text="Total Normal", command=self.total_normal).place(x=210, y=180, width=120)
        Button(self.ventana, text="Total + IVA", command=self.total_iva).place(x=350, y=180, width=120)
        Button(self.ventana, text="Total - 20% Descuento", command=self.total_descuento).place(x=50, y=220, width=200)
        Button(self.ventana, text="Salir", command=self.salir).place(x=350, y=220, width=120)

        # Mostrar totales
        Label(self.ventana, text="Total:").place(x=50, y=270)
        self.mostrarTotal = Label(self.ventana, text="")
        self.mostrarTotal.place(x=150, y=270)

        self.ventana.mainloop()

    def agregar(self):
        p1, p2, p3 = self.prod1.get(), self.prod2.get(), self.prod3.get()
        pr1, pr2, pr3 = self.precio1.get(), self.precio2.get(), self.precio3.get()
        resultado = self.tienda.agregar_productos(
            (p1, pr1), (p2, pr2), (p3, pr3)
        )
        if resultado == True:
            messagebox.showinfo("Éxito", "Productos agregados correctamente")
        else:
            messagebox.showerror("Error", resultado)

    def total_normal(self):
        total = self.tienda.total_normal()
        self.mostrarTotal.config(text=f"${total:.2f}")
        messagebox.showinfo("Total Normal", f"El total normal es: ${total:.2f}")

    def total_iva(self):
        total = self.tienda.total_iva()
        self.mostrarTotal.config(text=f"${total:.2f}")
        messagebox.showinfo("Total + IVA", f"El total con IVA es: ${total:.2f}")

    def total_descuento(self):
        total = self.tienda.total_descuento()
        self.mostrarTotal.config(text=f"${total:.2f}")
        messagebox.showinfo("Total - 20% Descuento", f"El total con descuento es: ${total:.2f}")

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()