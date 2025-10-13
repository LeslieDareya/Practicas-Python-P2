class GenerarCURP():
    def __init__(self):
        pass

    def generar_curp(self, nombre, ap_paterno, ap_materno, anio, mes, dia, sexo, estado):
        # Validar que no falten datos
        if nombre == "" or ap_paterno == "" or ap_materno == "" or anio == "" or mes == "" or dia == "" or sexo == "" or estado == "":
            return "Faltan datos, todos los campos son obligatorios"

        # Primer letra y primera vocal interna del apellido paterno
        primera_letra = ap_paterno[0].upper()
        primera_vocal = ""
        for letra in ap_paterno[1:]:
            if letra.upper() in "AEIOU":
                primera_vocal = letra.upper()
                break
        if primera_vocal == "":
            primera_vocal = "X"

        # Primera letra del apellido materno y del nombre
        letra_materno = ap_materno[0].upper() if len(ap_materno) > 0 else "X"
        letra_nombre = nombre[0].upper()

        # Fecha de nacimiento en formato YYMMDD
        if len(anio) != 4 or not anio.isdigit() or not mes.isdigit() or not dia.isdigit():
            return "Fecha de nacimiento inválida"
        fecha = anio[2:] + mes.zfill(2) + dia.zfill(2)

        # Sexo
        sexo = sexo.upper()
        if sexo != "H" and sexo != "M":
            return "Sexo inválido"

        # Estado: solo las primeras 3 letras
        estado = estado.upper()[:3]

        # Homoclave simplificada
        homoclave = "XX"

        curp = primera_letra + primera_vocal + letra_materno + letra_nombre + fecha + sexo + estado + homoclave
        return curp