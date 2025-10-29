import datetime
import json
import os #importamos 'os' para comprobar si el atchivo existe
# El nombre de nuestro archivo de guardado
constructor_silvermind_tracker = "datos.json"
# 1.Obtener la fecha de hoy (como texto, para que sea facil de guardar)
fecha_de_hoy = datetime.date.today().isoformat()# . isoformat() la convierte a "YYYY-MM-DD"
print(f"Iniciando Constructor Silvermind... Fecha de hoy: {fecha_de_hoy}")
# 2. Cargar los datos existentes (si los hay)
datos = {} # Creamos un diccionario vacio para empezar
if os.path.exists(constructor_silvermind_tracker):
    print("Cargando archivo de leyenda existente...")
    with open(constructor_silvermind_tracker, "r") as archivo:
        datos = json.load(archivo)
else:
    print("Creando nuevo archivo de leyenda...")
# 3. Anadir la marca de hoy
if fecha_de_hoy not in datos:
    print(f"Gig completado! Marcado el dia {fecha_de_hoy}...")
    datos[fecha_de_hoy] ="X" # Anadimos nuestra X para hoy
else:
    print(f"El dia {fecha_de_hoy} ya estaba marcado. Bien hecho!!!")
# 4. Guardar los datos actualizados de vuelta en el archivo
print("guardando progreso...")
with open(constructor_silvermind_tracker, "w") as archivo:
    json.dump(datos, archivo, indent=4)
    print("Leyenda actualizada! Nos vemos en el proximo gig.")    

