class Validar():
    def __init__(self):
        pass

    def ValidarNumero(self, valor):
        """
        Recibe un string 'valor'. Intenta convertirlo a int.
        Devuelve:
         - "Primo" si es primo
         - "No Primo" si no lo es (incluye 0, 1, negativos, compuestos)
         - "No es un número válido" si no se puede convertir a entero
        """
        try:
            n = int(valor)
        except ValueError:
            return "No es un número válido"

        if n < 2:
            return "No Primo"
        # Verificar divisores desde 2 hasta n-1
        for i in range(2, n):
            if n % i == 0:
                return "No Primo"
        return "Primo"