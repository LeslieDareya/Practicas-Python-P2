class Validar():
    def __init__(self):
        pass

    def ValidarAscii(self, valor):
        con_letras = 0
        con_numeros = 0
        for i in valor:
            if ord(i) >= 48 and ord(i) <= 57:  # Números del 0 al 9
                con_numeros += 1
            elif (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                con_letras += 1  # Letras mayúsculas o minúsculas

        if con_numeros == len(valor):
            return "Números"
        elif con_letras == len(valor):
            return "Letras"
        else:
            return "Letras y números"