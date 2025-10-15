from tkinter import *           
# Importa todas las funciones de tkinter
# Imports all tkinter functions

from tkinter import messagebox  
# Importa el módulo para mostrar mensajes emergentes
# Imports messagebox for pop-up dialogs


def Ventana():  
    # Define la función principal
    # Defines the main function

    def revisar():  
        # Función interna para validar usuario y contraseña
        # Inner function to validate username and password
        try:  
            u = str(us.get())  
            # Obtiene el texto del campo de usuario
            # Gets text from the username entry

            p = str(pas.get())  
            # Obtiene el texto del campo de contraseña
            # Gets text from the password entry

            if u == 'admin' and p == '12345':
                # Verifica si usuario y contraseña son correctos
                # Checks if username and password are correct
                messagebox.showinfo('Validación', 'Usuario y contraseña correctos')  
                # Muestra mensaje de éxito
                # Shows success message
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrecta')   
                # Muestra mensaje de error
                # Shows error message
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos')  
            # Muestra error si ocurre un problema
            # Shows error if something goes wrong

    ven = Tk()  
    # Crea la ventana principal
    # Creates the main window

    ven.title('Programa 1 con Ventanas')  
    # Establece el título de la ventana
    # Sets window title

    ven.geometry('400x400')  
    # Define el tamaño de la ventana
    # Sets window size

    Label(ven, text='Usuario').pack(pady=10)  
    # Etiqueta "Usuario"
    # Label for "Username"

    us = Entry(ven)  
    # Campo de texto para escribir el usuario
    # Entry box for username input

    us.pack(pady=3)  
    # Empaqueta el campo en la ventana
    # Packs the entry in the window

    Label(ven, text='Contraseña').pack(pady=10)  
    # Etiqueta "Contraseña"
    # Label for "Password"

    pas = Entry(ven)  
    # Campo de texto para escribir la contraseña
    # Entry box for password input

    pas.pack(pady=3)  
    # Empaqueta el campo en la ventana
    # Packs the entry in the window

    boton = Button(ven, text='Aceptar', command=revisar)  
    # Crea un botón que ejecuta la función revisar
    # Creates a button to run revisar

    boton.pack(pady=3)  
    # Empaqueta el botón en la ventana
    # Packs the button in the window

    ven.mainloop()  
    # Inicia el bucle principal de la ventana
    # Starts the main event loop for the window


if __name__ == "__main__":  
    # Punto de entrada del programa
    # Program entry point

    Ventana()  
    # Llama a la función para ejecutar la ventana
    # Calls the function to run the window
