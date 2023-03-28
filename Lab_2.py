def modificador_datos(nombre_archivo):
    separador = ","
    with open(nombre_archivo, encoding="utf-8") as archivo:
        next(archivo)  # Omitir encabezado del archivo
        datos = []
        for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)
            nro_region = int(columnas[0])
            region = columnas[1]
            provincia = columnas[2]
            circ_senatorial = int(columnas[3])
            distrito = int(columnas[4])
            comuna = columnas[5]
            circ_electoral = columnas[6]
            local = columnas[7]
            nro_mesa = int(columnas[8])
            tipo_mesa = columnas[9]
            mesas_fusionadas = columnas[10]
            electores = int(columnas[11])
            nro_en_voto = int(columnas[12])

            datos.append({
                "nro_region": nro_region,
                "region": region,
                "provincia": provincia,
                "circ_senatorial": circ_senatorial,
                "distrito": distrito,
                "comuna" : comuna,
                "circ_electoral" : circ_electoral,
                "local" : local,
                "nro_mesa" : nro_mesa,
                "tipo_mesa" : tipo_mesa,
                "mesas_fusionadas" : mesas_fusionadas,
                "electores" : electores,
                "nro_en_voto" : nro_en_voto,

            })
        return datos

print(modificador_datos("data.csv"))

