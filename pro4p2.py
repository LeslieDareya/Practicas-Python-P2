from tkinter import * 
from tkinter import messagebox


def Ventana():
    def revisar():
        try:
            u = str(us.get())
            p = str(pas.get())

            if u == 'admin' and p == '12345':
                messagebox.showinfo('Validacion', 'Usuario', 'Contraseña correcta')
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrecta')
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos')

    ven = Tk()  # Libreria
    ven.title('Programa 1 con Ventanas')  # Titulo de la ventana
    ven.geometry('400x400')  # Tamaño de la ventana

    Label(ven, text='Usuario').pack(pady=10)  # Texto

    us = Entry(ven)
    us.pack(pady=3)  # Caja de texto

    Label(ven, text='Contraseña').pack(pady=10)  # Texto

    pas = Entry(ven)
    pas.pack(pady=3)  # Caja de Texto

    boton = Button(ven, text='Aceptar', command=revisar).pack(pady=3)  # Boton 

    ven.mainloop()


if __name__ == "__main__":
    Ventana()