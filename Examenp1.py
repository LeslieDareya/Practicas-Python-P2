#Hacer un programa que lea nombre y 3 calificaciones que se agregaran con las siguientes restricciones:
#Las calificaciones se agregan en orden decendente, una vez realizado esto, mostrara una pregunta si deseas otra 
#persona. Si la respuesta es si, la primer lista se agregara a otra lista que contenga los 4 datos, para agregar
#a otra persona.
def inicio():
    lista1 = []
    nom = input('Escribe un nombre\n')
    c1 = int(input('Escribe una calificacion\n'))
    c2 = int(input('Escribe una calificacion\n'))
    c3 = int(input('Escribe una calificacion\n'))
    if (c1 > c2):
         if (c1 > c3):
              print('f es mayor {c1}')
              lista1.append(nom)
              lista1.append(c1)
              if (c2 > c3):
                   print('f es el de en medio {c2}')
                   print('f es el menor {c3}')
                   lista1.append(c2)
                   lista1.append(c3)
                   lista2.append(lista1)
              else:
                   print('f es el de en medio {c3}')
                   print('f es el menor {c2}')
                   lista1.append(c3)
                   lista1.append(c2)
                   lista2.append(lista1)
         else:
               print('f es el de en medio {c1}')
               print('f es el mayor {c3}')
               print('f es el menor {c2}')
               lista1.append(c3)
               lista1.append(c1)
               lista1.append(c2)
               lista2.append(lista1)
    else:
          if (c2 > c3):
              print('f es mayor {c2}')
              lista1.append(nom)
              lista1.append(c2)
              if (c1 > c3):
                    print('f es el de en medio {c1}')
                    print('f es el menor {c3}')
                    lista1.append(c1)
                    lista1.append(c3)
                    lista2.append(lista1)
              else:
                    print('f es el de en medio {c3}')
                    print('f es el menor {c1}')
                    lista1.append(c3)
                    lista1.append(c1)
                    lista2.append(lista1)
          else:
                print('f es el de en medio {c2}')
                print('f es el mayor {c3}')
                print('f es el menor {c1}')
                lista1.append(nom)
                lista1.append(c3)
                lista1.append(c2)
                lista1.append(c1)
                lista2.append(lista1)
lista2 = []

if __name__ == "__main__":
     while(True):
          inicio()
          a = input('Deseas agregar otro registro s\n')
          if a=='n' or a=='N':
               print(lista2)
               break
    

         
             
              
