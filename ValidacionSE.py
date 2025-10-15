# validarRepaso.py
# Este archivo contiene todas las funciones de validación
# This file contains all the validation functions

class Validar():
    def __init__(self):
        # Índice usado para recorrer strings si es necesario
        # Index used to traverse strings if needed
        self.index = 0

    def ValidarAscii(self, valor):
        """
        Determina si el valor es solo números o una combinación de letras y números
        Determines if the value is only numbers or a combination of letters and numbers
        """
        con = 0  # Contador de números / Counter for numbers
        con2 = 0 # Contador de letras / Counter for letters

        for i in valor:
            # Revisar si es número
            # Check if it is a number
            if 48 <= ord(i) <= 57:
                con += 1
            # Revisar si es letra mayúscula o minúscula
            # Check if it is uppercase or lowercase letter
            elif (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
                con2 += 1

        # Si todos los caracteres son números
        # If all characters are numbers
        if con == len(valor):
            return "Numeros"
        else:
            return "Letras y numeros"

    def ValidarConError(self, valor):
        """
        Valida si el valor es un número entero, real o texto
        Validates if the value is an integer, float, or text
        """
        try:
            int(valor)
            return "Es un numero entero"
        except ValueError:
            try:
                float(valor)
                return "Es un numero real o decimal"
            except ValueError:
                return "Letras o caracteres"

    def ValidarConString(self, valor):
        """
        Revisa si el string contiene el caracter '@' para determinar si es un correo
        Checks if the string contains '@' to determine if it is an email
        """
        for i in valor:
            if i == "@":
                return "Es un correo"
        return "No es un correo"

