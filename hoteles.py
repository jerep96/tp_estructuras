# archivo: hoteles.py
# descripción: Programa que gestiona una cadena de 10 hoteles.
#              Calcula la capacidad total de la cadena, el porcentaje de
#              ocupación de cada filial y determina la ciudad con más habitaciones.
# autores: [BRIAN NICOLAS OCHNICKI HEFLIN - MATÍAS BASSO - MATIAS SANCHEZ - OMAR JEREMIAS PALACIOS TOCONAS]

# ---------------------------------------------------------------
# Variables de acumulación y control general
# ---------------------------------------------------------------
total_capacidad_cadena = 0   # Acumula la capacidad total de todas las filiales
ciudad_max_habitaciones = ""  # Ciudad con más habitaciones (resultado final)
max_habitaciones = 0         # Máximo de habitaciones encontrado hasta el momento
bandera = True               # Bandera para inicializar el máximo con el primer valor leído

print("=" * 50)
print("  SISTEMA DE GESTIÓN DE CADENA DE HOTELES")
print("=" * 50)

# ---------------------------------------------------------------
# Bucle principal: recorre las 10 filiales una por una
# ---------------------------------------------------------------
for numero_filial in range(1, 11):

    print(f"\n--- Filial {numero_filial} de 10 ---")

    # Ingreso del nombre de la ciudad (sin validación numérica)
    ciudad = input("Ingrese el nombre de la ciudad: ")

    # -----------------------------------------------------------
    # Validación: la capacidad total debe ser mayor a 0
    # -----------------------------------------------------------
    capacidad_valida = False
    while not capacidad_valida:
        capacidad = int(
            input("Ingrese la capacidad total del hotel (huéspedes): "))
        if capacidad > 0:
            capacidad_valida = True
        else:
            print("  ERROR: la capacidad debe ser mayor a 0. Intente de nuevo.")

    # -----------------------------------------------------------
    # Validación: la cantidad de habitaciones debe ser mayor a 0
    # -----------------------------------------------------------
    habitaciones_validas = False
    while not habitaciones_validas:
        habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
        if habitaciones > 0:
            habitaciones_validas = True
        else:
            print(
                "  ERROR: la cantidad de habitaciones debe ser mayor a 0. Intente de nuevo.")

    # -----------------------------------------------------------
    # Validación: los huéspedes del mes no pueden superar la capacidad
    # -----------------------------------------------------------
    huespedes_validos = False
    while not huespedes_validos:
        huespedes = int(input("Ingrese la cantidad de huéspedes en el mes: "))
        if huespedes >= 0 and huespedes <= capacidad:
            huespedes_validos = True
        else:
            print(
                f"  ERROR: los huéspedes deben estar entre 0 y {capacidad}. Intente de nuevo.")

    # -----------------------------------------------------------
    # Acumulación de la capacidad total de la cadena
    # -----------------------------------------------------------
    total_capacidad_cadena = total_capacidad_cadena + capacidad

    # -----------------------------------------------------------
    # Cálculo y muestra del porcentaje de ocupación de esta filial
    # -----------------------------------------------------------
    porcentaje_ocupacion = (huespedes / capacidad) * 100
    print(
        f"  >> Porcentaje de ocupación de {ciudad}: {porcentaje_ocupacion:.2f}%")

    # -----------------------------------------------------------
    # Determinación de la ciudad con mayor cantidad de habitaciones.
    # Se usa la bandera para inicializar el máximo con el primer
    # valor leído, evitando comparar contra un 0 arbitrario.
    # -----------------------------------------------------------
    if bandera:
        # Primer hotel: se toma como máximo inicial
        max_habitaciones = habitaciones
        ciudad_max_habitaciones = ciudad
        bandera = False          # Se desactiva la bandera; ya no se usará
    else:
        # Hoteles siguientes: se compara contra el máximo actual
        if habitaciones > max_habitaciones:
            max_habitaciones = habitaciones
            ciudad_max_habitaciones = ciudad

# ---------------------------------------------------------------
# Resultados finales de toda la cadena
# ---------------------------------------------------------------
print("\n" + "=" * 50)
print("         RESULTADOS FINALES DE LA CADENA")
print("=" * 50)
print(f"Capacidad total de la cadena: {total_capacidad_cadena} huéspedes")
print(
    f"Ciudad con más habitaciones : {ciudad_max_habitaciones} ({max_habitaciones} habitaciones)")
print("=" * 50)

"""
Reflexión grupal:
------------------
Con este ejercicio aprendimos a resolver un problema real usando únicamente
variables simples, bucles for/while y condicionales if/else, prescindiendo
de listas u otras estructuras avanzadas.

Uno de los puntos más importantes fue el uso de la variable bandera para
inicializar el máximo de habitaciones con el primer valor real ingresado
por el usuario, en lugar de asumir un valor arbitrario como 0. Esto hace
que el programa sea correcto incluso si todos los valores son muy pequeños
o muy grandes.

También practicamos la validación de datos de entrada con bucles while,
lo que nos enseñó a pensar en los posibles errores que puede cometer el
usuario y cómo proteger el programa ante ellos.

Finalmente, el trabajo grupal nos permitió dividir el análisis del problema
en partes más pequeñas —ingreso, validación, cálculo y resultados— y
resolverlas de manera ordenada antes de integrarlas en un solo programa.
"""
