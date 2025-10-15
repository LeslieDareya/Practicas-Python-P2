# Constructor: Metodo que se inicializa al momento de ejecutarse
# Constructor: Method that is initialized when executed
from validaciones import validacion
val = validacion()  # Crear una instancia de la clase de validaciones
                     # Create an instance of the validation class

class Principal():
    def __init__(self):
        # Lista que almacenará las calificaciones ingresadas
        # List that will store the entered grades
        self.lista = []

        # Contador de cuántas calificaciones se han ingresado
        # Counter for how many grades have been entered
        self.num = 0

        # Variable temporal para guardar la entrada del usuario (string)
        # Temporary variable to store the user's input (string)
        self.a = ""

    def inicio(self):
        # Pedir al usuario que escriba una calificación (se recibe como texto)
        # Ask the user to write a grade (received as text)
        self.a = input('Escribe una calificacion \n')

        # Validar que la entrada sea numérica usando la instancia val
        # Validate that the input is numeric using the val instance
        if val.ValidarNumeros(self.a):
            # Si es número, incrementar el contador
            # If it's a number, increment the counter
            self.num += 1

            # Convertir la entrada a entero y agregar a la lista de calificaciones
            # Convert the input to int and append to the grades list
            self.lista.append(int(self.a))

            # Si ya se han ingresado 5 o más calificaciones, mostrar la lista y el promedio
            # If 5 or more grades have been entered, show the list and the average
            if self.num >= 5:
                print(self.lista)
                # Usar el método Promedio de la clase de validaciones para calcular el promedio
                # Use the Promedio method from the validation class to compute the average
                print(f'El promedio es: {val.Promedio(self.lista)}')
            else:
                # Si faltan más entradas, llamar de nuevo a inicio() para pedir otra calificación
                # If more entries are needed, call inicio() again to request another grade
                self.inicio()
        else:
            # Si la entrada no es un número, avisar y volver a pedir una calificación
            # If the input is not a number, notify and ask for a grade again
            print('No es un numero')
            self.inicio()

if __name__ == '__main__':
    # Crear la aplicación y comenzar el proceso de entrada de calificaciones
    # Create the application and start the grade input process
    app = Principal()
    app.inicio()
