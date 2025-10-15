#Hacer un programa que lea nombre y 3 calificaciones que se agregaran con las siguientes restricciones:
#Las calificaciones se agregan en orden decendente, una vez realizado esto, mostrara una pregunta si deseas otra 
#persona. Si la respuesta es si, la primer lista se agregara a otra lista que contenga los 4 datos, para agregar
#a otra persona.
def inicio():
    # Lista temporal para guardar los datos de un solo alumno
    # Temporary list to store data for a single student
    lista1 = []

    # Se pide el nombre del alumno
    # Ask for the student's name
    nom = input('Escribe un nombre\n')

    # Se piden tres calificaciones
    # Ask for three grades
    c1 = int(input('Escribe una calificación\n'))
    c2 = int(input('Escribe una calificación\n'))
    c3 = int(input('Escribe una calificación\n'))

    # Comienza la comparación para saber cuál calificación es mayor
    # Start comparing to determine which grade is highest
    if (c1 > c2):
         if (c1 > c3):
              # Si c1 es mayor que las otras dos
              # If c1 is greater than both others
              print(f'f es mayor {c1}')  # ← faltaba la f antes de la cadena
              lista1.append(nom)
              lista1.append(c1)
              if (c2 > c3):
                   # Si c2 es el de en medio y c3 el menor
                   # If c2 is middle and c3 is lowest
                   print(f'f es el de en medio {c2}')
                   print(f'f es el menor {c3}')
                   lista1.append(c2)
                   lista1.append(c3)
                   lista2.append(lista1)
              else:
                   # Si c3 es el de en medio y c2 el menor
                   # If c3 is middle and c2 is lowest
                   print(f'f es el de en medio {c3}')
                   print(f'f es el menor {c2}')
                   lista1.append(c3)
                   lista1.append(c2)
                   lista2.append(lista1)
         else:
               # Si c3 es mayor que c1 (aunque c1 > c2)
               # If c3 is greater than c1 (even though c1 > c2)
               print(f'f es el de en medio {c1}')
               print(f'f es el mayor {c3}')
               print(f'f es el menor {c2}')
               lista1.append(c3)
               lista1.append(c1)
               lista1.append(c2)
               lista2.append(lista1)
    else:
          # Si c2 es mayor o igual a c1
          # If c2 is greater than or equal to c1
          if (c2 > c3):
              # Si c2 es mayor que c3
              # If c2 is greater than c3
              print(f'f es mayor {c2}')
              lista1.append(nom)
              lista1.append(c2)
              if (c1 > c3):
                    # Si c1 es el de en medio y c3 el menor
                    # If c1 is middle and c3 is lowest
                    print(f'f es el de en medio {c1}')
                    print(f'f es el menor {c3}')
                    lista1.append(c1)
                    lista1.append(c3)
                    lista2.append(lista1)
              else:
                    # Si c3 es el de en medio y c1 el menor
                    # If c3 is middle and c1 is lowest
                    print(f'f es el de en medio {c3}')
                    print(f'f es el menor {c1}')
                    lista1.append(c3)
                    lista1.append(c1)
                    lista2.append(lista1)
          else:
                # Si c3 es mayor que todos
                # If c3 is the highest of all
                print(f'f es el de en medio {c2}')
                print(f'f es el mayor {c3}')
                print(f'f es el menor {c1}')
                lista1.append(nom)
                lista1.append(c3)
                lista1.append(c2)
                lista1.append(c1)
                lista2.append(lista1)


# Lista general para guardar los datos de todos los alumnos
# Global list to store data for all students
lista2 = []

# Punto de entrada principal del programa
# Main program entry point
if __name__ == "__main__":
     while(True):
          # Se llama a la función para capturar datos
          # Call the function to capture data
          inicio()

          # Se pregunta si se desea continuar
          # Ask if user wants to continue
          a = input('¿Deseas agregar otro registro? s/n\n')

          # Si la respuesta es 'n' o 'N', se termina el ciclo
          # If the answer is 'n' or 'N', end the loop
          if a == 'n' or a == 'N':
               # Se muestra la lista completa de registros
               # Show the full list of records
               print(lista2)
               break

    

         
             
              
