class Validar():
    def __init__(self):
        self.index
    def ValidarAscii(self, valor):
        con = 0
        con2 = 0
        for i in valor:
            if ord(i) >=48 and ord(i)<= 57:
                con += 1
            if (ord(i)>= 65 and ord()<=90) or (ord(i)>= 97 and ord()<=122):
                con2 += 1
                
            if con == len(valor):
                return "Numeros"
            else:
                return "Letras y numeros"

       
    def ValidarConError(self, valor):
        a = 0
        b = 0.0
        try:
            a = int(valor)
            return "numeros"
        except ValueError:
        try:
            b = float(valor)
            return "Es un numero real o con decimales"
            return "letras o numeros"
        
       
    def ValidarConString(self, valor):
       if valor[self.index] == "@":
           return "si es un correo"
       else:
           if self.index < len(valor):
           self.index += 1
           self.ValidarConString
           