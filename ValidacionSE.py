# validarRepaso.py
# Aquí van todas las validaciones

class Validar():
    def __init__(self):
        self.index = 0

    def ValidarAscii(self, valor):
        """Determina si el valor es solo numeros o letras y numeros"""
        con = 0  # contador de números
        con2 = 0 # contador de letras
        for i in valor:
            if 48 <= ord(i) <= 57:
                con += 1
            elif (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
                con2 += 1

        if con == len(valor):
            return "Numeros"
        else:
            return "Letras y numeros"

    def ValidarConError(self, valor):
        """Valida si el valor es entero, real o texto"""
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
        """Verifica si el string contiene @ (correo)"""
        for i in valor:
            if i == "@":
                return "Es un correo"
        return "No es un correo"
