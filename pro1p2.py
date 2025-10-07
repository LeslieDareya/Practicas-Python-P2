def inicio(num):
##  global num
    a = int(input('Escribe una calificacion \n'))
    num += 1
    lista.append(a)
    if num >= 5:
        print(lista)
    else:
        inicio(num)


lista = []
global num
num = 0
if __name__=='__main__':
    inicio(num)