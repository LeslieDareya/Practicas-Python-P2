
def inicio():
    #Define la función 'inicio' que procesa una persona y sus 3 calificaciones
    #Defines the 'inicio' function that processes one person and their 3 grades.
    
    global lista2
    # Declaramos lista2 como global para poder modificarla dentro de la función
    # Declare lista2 as global so it can be modified inside the function
    
    lista1 = []
    #Lista temporal para guardar nombre y calificaciones ordenadas.
    #Temporary list to store name and ordered grades.
    
    nom = input('Escribe tu nombre: ')
    #Pide el nombre de la persona.
    #Asks for the person's name.
    
    cal1 = int(input('Agrega tu primera Calificacion: '))
    #Pide la primera calificación y la convierte a entero.
    #Asks for the first grade and converts it to int.
    
    cal2 = int(input('Agrega tu segunda Calificacion: '))
    #Pide la segunda calificación y la convierte a entero.
    #Asks for the second grade and converts it to int.
    
    cal3 = int(input('Agrega tu tercera Calificacion: '))
    #Pide la tercera calificación y la convierte a entero.
    #Asks for the third grade and converts it to int.
    
    #Comparamos las calificaciones para determinar mayor, medio y menor.
    #Compares the grades to determine largest, middle and smallest.
    
    if (cal1 > cal2):
        #Si cal1 es mayor que cal2,
        #If cal1 is greater than cal2,
        if (cal1 > cal3):
            #Si cal1 es mayor que cal3, entonces cal1 es la mayor.
            #If cal1 is greater than cal3, then cal1 is the largest.
            #cal3 también es mayor que cal2 (cal1 es la mayor).
            #And cal3 is also greater than cal2 (cal1 is the largest).
            #And cal1 is also greater than cal3 (cal1 is the largest). (CORRECTION: This comment seems incorrect, it should compare cal2 and cal3 next)
            print(f'Es el mayor ({cal1})')
            #Imprime la mayor.
            #Prints the largest.
            
            lista1.append(nom)
            #Añade el nombre a la lista temporal.
            #Adds the name to the temporary list.
            
            lista1.append(cal1)
            #Añade la mayor (cal1).
            #Adds the largest (cal1).
            
            if (cal2 > cal3):
                #cal2 seria el medio y cal3 la menor.
                #cal2 would be the middle and cal3 the smallest.
                print(f'Es el de en medio ({cal2})')
                #Aqui cal2 seria la del medio.
                #Here cal2 would be the middle grade.
                print(f'Es el menor ({cal3})')
                #Imprime la menor (cal3).
                #Prints the smallest (cal3).
                
                lista1.append(cal2)
                #Añade la del medio (cal2).
                #Adds the middle (cal2).
                
                lista1.append(cal3)
                #Añade la menor (cal3).
                #Adds the smallest (cal3).
            else:
                #cal3 seria el medio y cal2 la menor.
                #cal3 would be the middle and cal2 the smallest.
                print(f'Es el de en medio ({cal3})')
                #Aquí cal3 seria la del medio.
                #Here cal3 would be the middle grade.
                print(f'Es el menor ({cal2})')
                #Imprime la menor (cal2).
                #Prints the smallest (cal2).
                
                lista1.append(cal3)
                #Añade la del medio (cal3).
                #Adds the middle (cal3).
                
                lista1.append(cal2)
                #Añade la menor (cal2).
                #Adds the smallest (cal2).
        else:
            #Si cal3 > cal1, entonces cal3 es la mayor.
            #If cal3 > cal1, then cal3 is the largest.
            #cal1 sería la del medio.
            #cal1 would be the middle.
            #cal2 sería la menor (porque cal1 > cal2).
            #cal2 would be the smallest (because cal1 > cal2).
            print(f'Es el de en medio ({cal1})')
            #Aquí cal1 seria la del medio.
            #Here cal1 would be the middle grade.
            print(f'Es mayor ({cal3})')
            #Imprime la mayor (cal3).
            #Prints the largest (cal3).
            print(f'Es el menor ({cal2})')
            #Imprime la menor (cal2).
            #Prints the smallest (cal2).
            
            lista1.append(nom)
            #Añade el nombre a la lista temporal.
            #Adds the name to the temporary list.
            
            lista1.append(cal3)
            #Añade la mayor (cal3) primero.
            #Adds the largest (cal3) first.
            
            lista1.append(cal1)
            #Añade la del medio (cal1).
            #Adds the middle grade (cal1).
            
            lista1.append(cal2)
            #Añade la menor (cal2).
            #Adds the smallest (cal2).
    else:
        #Case en que cal1 <= cal2 (cal2 podría ser mayor que cal1).
        #Case where cal1 <= cal2 (cal2 might be greater than cal1).
        if (cal2 > cal3):
            #Si cal2 es mayor que cal3, entonces cal2 es la mayor.
            #If cal2 is greater than cal3, then cal2 is the largest.
            print(f'Es mayor ({cal2})')
            #Imprime la mayor.
            #Prints the largest.
            
            lista1.append(nom)
            #Añade el nombre a la lista temporal.
            #Adds the name to the temporary list.
            
            lista1.append(cal2)
            #Añade la mayor (cal2).
            #Adds the largest (cal2).
            
            if (cal1 > cal3):
                #Si cal1 > cal3, entonces cal1 es la del medio y cal3 la menor.
                #If cal1 > cal3, then cal1 is middle and cal3 is smallest.
                print(f'Es el de en medio ({cal1})')
                #Imprime la del medio.
                #Prints the middle grade.
                print(f'Es el menor ({cal3})')
                #Imprime la menor.
                #Prints the smallest.
                
                lista1.append(cal1)
                #Añade cal1 (medio) a la lista temporal.
                #Adds cal1 (middle) to the temporary list.
                
                lista1.append(cal3)
                #Añade cal3 (menor) a la lista temporal.
                #Adds cal3 (smallest) to the temporary list.
            else:
                #Si cal3 >= cal1, entonces cal3 es la del medio y cal1 la menor.
                #If cal3 >= cal1, then cal3 is middle and cal1 is smallest.
                print(f'Es el de en medio ({cal3})')
                #Imprime la calificación del medio.
                #Prints the middle grade.
                print(f'Es el menor ({cal1})')
                #Imprime la calificación menor.
                #Prints the smallest grade.
                
                lista1.append(cal3)
                #Añade cal3 (medio) a la lista temporal.
                #Adds cal3 (middle) to the temporary list.
                
                lista1.append(cal1)
                #Añade cal1 (menor) a la lista temporal.
                #Adds cal1 (smallest) to the temporary list.
        else:
            #Si cal3 >= cal2, entonces cal3 es la mayor.
            #If cal3 >= cal2, then cal3 is the largest.
            print(f'Es el mayor ({cal3})')
            #Imprime la mayor.
            #Prints the largest.
            
            lista1.append(nom)
            #Añade el nombre.
            #Adds the name.
            
            lista1.append(cal3)
            #Añade la mayor primero.
            #Adds the largest first.
            
            if (cal1 > cal2):
                #Si cal1 > cal2, entonces cal1 es la del medio y cal2 la menor.
                #If cal1 > cal2, then cal1 is middle and cal2 is smallest.
                print(f'Es el de en medio ({cal1})')
                #Imprime la calificación del medio.
                #Prints the middle grade.
                print(f'Es el menor ({cal2})')
                #Imprime la calificación menor.
                #Prints the smallest grade.
                
                lista1.append(cal1)
                #Añade cal1 (medio) a la lista temporal.
                #Adds cal1 (middle) to the temporary list.
                
                lista1.append(cal2)
                #Añade cal2 (menor) a la lista temporal.
                #Adds cal2 (smallest) to the temporary list.
            else:
                #Si cal2 >= cal1, entonces cal2 es la del medio y cal1 la menor.
                #If cal2 >= cal1, then cal2 is middle and cal1 is smallest.
                print(f'Es el de en medio ({cal2})')
                #Imprime la del medio (cal2).
                #Prints the middle grade (cal2).
                print(f'Es el menor ({cal1})')
                #Imprime la menor (cal1).
                #Prints the smallest (cal1).
                
                lista1.append(cal2)
                #Añade cal2 (medio) a la lista temporal.
                #Adds cal2 (middle) to the temporary list.
                
                lista1.append(cal1)
                #Añade cal1 (menor) a la lista temporal.
                #Adds cal1 (smallest) to the temporary list.
    
    lista2.append(lista1)
    #Añade la lista temporal completa a lista2 global lista2.
    #Appends the full temporary list to the global lista2.
    
    #lista2.append(lista1) # Redundante, ya fue añadida.
    #Appends the ordered temporary list to lista2. (Inconsistent with other branches)
    
    #Guarda la lista ordenada en lista2.
    #Stores the ordered list in lista2.

lista2 = []

if __name__ == '__main__':
    while(True):
        inicio()
        a = input('Deseas otra persona s/n: ')
        if a == 'n' or a == 'N':
            print(lista2)
            break
