#Hacer un programa que mediante una ventana tkn}inter realice lo siguiente
#1. La ventana debe contener 3 cajas de texto y 2 botones
#2. El programa validara que la primer caja de texto solo permita letras minusculas, en la segunda caja solo 
#letras mayusculas y en la tercera solo numeros, dicha validacion la realizara el primer boton,
#si algun dato es incorrecto mostrara un mensaje de error y se borrara la caja de texto.
#3. Unicamente cuando las 3 cajas de texto tengan informacion y esten validadas se concatenaran y se agregaran a una lista visual
#tres cajas de texto arriba, un label en medio y dos botones abajo validar y agregar y una list box a un lado 
# si algun lado no es correcto borra solo esa casilla y la vuelve a pedir y si esta correcto al presionar el boton agregar se agrega a la list box 
#con los 3 datos concatenados y el label muestra 1. al terminar este proceso se borran los datos de las cajas de texto para
#ingresar un nuevo registro y repite el proceso, valida, pide corregir si esta mal y si es correcto lo agrega al list box
# con los datos concatenados y el label muestra 2. asi sicesivamente con todos los registros deseados

from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Simulacro examen")
        self.ventana.geometry("600x250")
        self.lista = []
        self.counter = 0
        self.validado = False

    def inicio(self):
        # --- Título arriba ---
        l1 = Label(self.ventana, text="Simulacro Examen", font=("Arial", 14, "bold"))
        l1.grid(row=0, column=0, columnspan=5, pady=10)

        # --- Cajas de texto en horizontal ---
        self.n1 = Entry(self.ventana, width=15)
        self.n1.grid(row=1, column=0, padx=5)
        self.n2 = Entry(self.ventana, width=15)
        self.n2.grid(row=1, column=1, padx=5)
        self.n3 = Entry(self.ventana, width=15)
        self.n3.grid(row=1, column=2, padx=5)

        # --- Label debajo de las cajas ---
        Label(self.ventana, text="Elemento:").grid(row=2, column=0, pady=10, sticky=W)
        self.elemento = Label(self.ventana, text="0.")
        self.elemento.grid(row=2, column=1, pady=10, sticky=W)

        # --- Botones debajo del label ---
        b1 = Button(self.ventana, text="Validar", width=12, command=self.agregar)
        b1.grid(row=3, column=0, pady=10)
        b2 = Button(self.ventana, text="Agregar", width=12, command=self.mayor)
        b2.grid(row=3, column=1, pady=10)

        # --- Listbox a la derecha ---
        self.listview = Listbox(self.ventana, height=10, width=25)
        self.listview.grid(row=1, column=4, rowspan=3, padx=10, pady=5)

        self.ventana.mainloop()

    def agregar(self):
        campos = [self.n1, self.n2, self.n3]

        def validar_campo(idx):
            texto = campos[idx].get()
            if idx == 0 and (texto == "" or not texto.isalpha() or not texto.islower()):
                campos[idx].delete(0, END)
                messagebox.showerror("Error", "Algún campo no es correcto.")
                return False
            elif idx == 1 and (texto == "" or not texto.isalpha() or not texto.isupper()):
                campos[idx].delete(0, END)
                messagebox.showerror("Error", "Algún campo no es correcto.")
                return False
            elif idx == 2 and (texto == "" or not texto.isdigit()):
                campos[idx].delete(0, END)
                messagebox.showerror("Error", "Algún campo no es correcto.")
                return False

            if idx + 1 < len(campos):
                return validar_campo(idx + 1)
            else:
                return True

        if validar_campo(0):
            self.validado = True
            messagebox.showinfo("Validación", "Los 3 campos están validados correctamente.")
        else:
            self.validado = False

    def mayor(self):
        if not self.validado:
            self.agregar()

        if self.validado:
            v1 = self.n1.get()
            v2 = self.n2.get()
            v3 = self.n3.get()
            conjunto = f"{v1} {v2} {v3}"
            self.listview.insert(END, conjunto)
            self.lista.append(conjunto)
            self.counter += 1
            self.elemento.config(text=f"{self.counter}.")
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.validado = False
        else:
            messagebox.showerror("No agregado", "No se pudo agregar: corrige los campos.")

if __name__ == "__main__":
    app = Principal()
    app.inicio()


