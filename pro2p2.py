
#Constructor: Metodo que se inicializa al momento de ejecutarse
from validaciones import validacion
val = validacion()

class Principal():
    def __init__(self):
        self.lista = []
        self.num = 0
        self.a = ""

    def inicio(self):
        self.a = input('Escribe una calificacion \n')
        if val.ValidarNumeros(self.a):
            self.num += 1
            self.lista.append(int(self.a))
            if self.num >= 5:
                print(self.lista)
                print(f'El promedio es: {val.Promedio(self.lista)}')
            else:
                self.inicio()
        else:
            print('No es un numero')
            self.inicio()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
