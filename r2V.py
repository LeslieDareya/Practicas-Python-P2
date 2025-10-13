class Validar():
    def __init__(self):
        pass

    def ValidarNumero(self, valor):
        try:
            num = int(valor)
            if num % 2 == 0:
                return "Par"
            else:
                return "Impar"
        except ValueError:
            return "No es un número válido"
