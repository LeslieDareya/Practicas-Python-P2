class Validar():
    def __init__(self):
        pass

    def ValidarNumero(self, valor):
        if not valor.isdigit():
            return "No es un número válido"
        numero = int(valor)
        return {
            'mult2': numero % 2 == 0,
            'mult5': numero % 5 == 0
        }