class Validar():
    def __init__(self):
        pass

    def ValidarCadena(self, valor):
        """
        Recibe un string 'valor'.
        Devuelve:
         - Lista con todas las vocales encontradas (mayúsculas y minúsculas)
         - "No es una cadena válida" si está vacío
        """
        if not valor:
            return "No es una cadena válida"
        
        vocales = 'aeiouAEIOU'
        resultado = []

        for letra in valor:
            if letra in vocales:
                resultado.append(letra)
        
        return resultado