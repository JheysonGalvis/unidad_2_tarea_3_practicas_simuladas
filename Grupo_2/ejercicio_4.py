"""
Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
La empresa Netflix desea saber cuál es el género favorito de
streaming entre 5 personas. Para esto, le ha solicitado su ayuda
para desarrollar un programa para saber cuál es el género con
más votos entre: acción y ciencia ficción. El programa debe
capturar la preferencia de las 5 personas y mostrar cuál de los
géneros es el favorito.
"""

# Paso 1: Inicializamos los contadores para los géneros
# Definimos dos variables para contar los votos de cada género.
accion = 0
ciencia_ficcion = 0

# Paso 2: Capturamos las preferencias de las 5 personas
# Usamos un ciclo para capturar la preferencia de las 5 personas.
for i in range(1, 6):  # Repetimos 5 veces (para las 5 personas)
    print(f"Persona {i}: ¿Cuál es tu género favorito? (acción/ciencia ficción)")  # Preguntamos por el género
    preferencia = input().lower()  # Leemos la respuesta, .lower() convierte todo a minúsculas para evitar errores
    
    # Paso 3: Condicionales anidados para contar los votos
    if preferencia == "acción":  # Si la preferencia es acción
        accion += 1  # Aumentamos el contador de acción
    else:  # Si no es acción (es ciencia ficción)
        if preferencia == "ciencia ficción":  # Comprobamos si es ciencia ficción
            ciencia_ficcion += 1  # Aumentamos el contador de ciencia ficción
        else:
            print("Opción no válida, ingresa 'acción' o 'ciencia ficción'.")  # Si la respuesta es incorrecta

# Paso 4: Determinamos el género con más votos
if accion > ciencia_ficcion:  # Si los votos de acción son mayores
    print("\nEl género favorito es: Acción.")  # Mostramos que acción es el favorito
else:  # Si no, el género favorito será ciencia ficción o empate
    if ciencia_ficcion > accion:  # Si los votos de ciencia ficción son mayores
        print("\nEl género favorito es: Ciencia ficción.")  # Mostramos que ciencia ficción es el favorito
    else:  # Si los votos son iguales (empate)
        print("\nHay empate entre acción y ciencia ficción.")  # Mostramos que hay empate
