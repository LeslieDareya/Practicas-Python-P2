

class validacion():
    def __init__(self):
        self.suma = 0
        self.promedio = 0.0



    def ValidarNumeros(self, valor):
        if valor.isdigit():
            return True 
        else:
            return False

    def Promedio(self, lista):
        for i in lista:
            self.suma += i
        self.promedio = self.suma / len(lista)
        return self.promedio

        
        
        
        