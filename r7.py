from tkinter import *
from tkinter import messagebox
from r7V import GenerarCURP  # Archivo con la lógica de CURP

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Generador de CURP")
        self.ventana.geometry("550x400")

        self.curp_gen = GenerarCURP()

    def inicio(self):
        Label(self.ventana, text="Generador de CURP", font=("Arial", 14)).place(x=180, y=10)

        Label(self.ventana, text="Nombre:").place(x=40, y=50)
        self.nombre = Entry(self.ventana)
        self.nombre.place(x=200, y=50, width=250)

        Label(self.ventana, text="Apellido Paterno:").place(x=40, y=90)
        self.ap_paterno = Entry(self.ventana)
        self.ap_paterno.place(x=200, y=90, width=250)

        Label(self.ventana, text="Apellido Materno:").place(x=40, y=130)
        self.ap_materno = Entry(self.ventana)
        self.ap_materno.place(x=200, y=130, width=250)

        Label(self.ventana, text="Año de Nacimiento (YYYY):").place(x=40, y=170)
        self.anio = Entry(self.ventana)
        self.anio.place(x=250, y=170, width=200)

        Label(self.ventana, text="Mes (MM):").place(x=40, y=210)
        self.mes = Entry(self.ventana)
        self.mes.place(x=200, y=210, width=80)

        Label(self.ventana, text="Día (DD):").place(x=300, y=210)
        self.dia = Entry(self.ventana)
        self.dia.place(x=360, y=210, width=80)

        Label(self.ventana, text="Sexo (H/M):").place(x=40, y=250)
        self.sexo = Entry(self.ventana)
        self.sexo.place(x=200, y=250, width=50)

        Label(self.ventana, text="Estado:").place(x=300, y=250)
        self.estado = Entry(self.ventana)
        self.estado.place(x=360, y=250, width=80)

        Button(self.ventana, text="Generar CURP", command=self.generar).place(x=100, y=300, width=120)
        Button(self.ventana, text="Salir", command=self.salir).place(x=300, y=300, width=120)

        Label(self.ventana, text="CURP Generada:").place(x=40, y=350)
        self.mostrarCurp = Label(self.ventana, text="")
        self.mostrarCurp.place(x=160, y=350)

        self.ventana.mainloop()

    def generar(self):
        nom = self.nombre.get()
        ap1 = self.ap_paterno.get()
        ap2 = self.ap_materno.get()
        anio = self.anio.get()
        mes = self.mes.get()
        dia = self.dia.get()
        sexo = self.sexo.get()
        estado = self.estado.get()

        curp = self.curp_gen.generar_curp(nom, ap1, ap2, anio, mes, dia, sexo, estado)
        if isinstance(curp, str) and len(curp) > 0:
            self.mostrarCurp.config(text=curp)
            messagebox.showinfo("CURP", f"CURP generada: {curp}")
        else:
            messagebox.showerror("Error", curp)

    def salir(self):
        self.ventana.destroy()


if __name__ == "__main__":
    app = Principal()
    app.inicio()