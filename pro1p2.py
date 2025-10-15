def inicio(num):
    # Función que pide calificaciones y las guarda en una lista hasta tener 5

    a = int(input('Escribe una calificacion \n'))  # Pide una calificación al usuario
    num += 1  # Aumenta el contador de calificaciones
    lista.append(a)  # Agrega la calificación a la lista

    if num >= 5:  # Si ya se ingresaron 5 calificaciones
        print(lista)  # Muestra la lista completa
    else:
        inicio(num)  # Si no, vuelve a llamar la función para pedir otra calificación


lista = []  # Crea una lista vacía para guardar las calificaciones
global num  # Declara la variable num como global
num = 0  # Inicializa el contador en 0

if __name__=='__main__':  # Punto de inicio del programa
    inicio(num)  # Llama a la función inicio por primera vez
