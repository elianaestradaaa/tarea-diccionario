# Tarea: Trabajando con diccionarios en Python
# Comentarios en español para que entiendas cada paso

# 1) Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "María Pérez",    # nombre ficticio
    "edad": 30,                # edad (se eliminará luego según la tarea)
    "ciudad": "Quito",         # ciudad inicial
    "profesion": "Estudiante"  # profesión inicial
}

# Mostrar el diccionario inicial (opcional, para ver cómo comienza)
print("Diccionario inicial:")
print(informacion_personal)

# 2) Acceder y modificar el valor de la clave "ciudad"
# Accedemos imprimiendo antes y luego cambiamos a otra ciudad
print("\nCiudad antes:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"  # cambiamos la ciudad
print("Ciudad después:", informacion_personal["ciudad"])

# 2b) Agregar o actualizar la clave "profesion"
# (si ya existe, aquí la actualizamos; si no existe, la agregaríamos)
informacion_personal["profesion"] = "Técnica en soporte"  # nueva profesión

# 3) Verificar existencia de la clave "telefono" y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"  # número ficticio

# 4) Eliminar la clave "edad" porque la tarea lo pide
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 5) Imprimir el diccionario final tras las operaciones
print("\nDiccionario final:")
print(informacion_personal)
