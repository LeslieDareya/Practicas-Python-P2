class Validar():
    def __init__(self):
        pass
    def ValidarAscii(self, valor):
        con = 0
        for i in valor:
            if ord(i) >=48 and ord(i)<= 57:
                con += 1
            if con == len(valor):
                return "Numeros"
            else:
                return "Letras y numeros"

       
    def ValidarConError(self, valor):
        pass
    def ValidarConString(self, valor):
        pass