"""Realizar el siguiente ejercicio con la instrucción if..elif..else
Construir un programa que permita calcular el grupo
generacional al cual pertenece una persona, para esto debe
solicitar la edad y dependiendo del rango de edades mostrar a
que grupo pertenece así:"""

"""
**Tabla 1**  
*Rango de edades que muestra el grupo Generacional.*

| Edades               | Grupo Generacional |
|----------------------|--------------------|
| Menor o igual a 12 años | Niño             |
| De 13 a 17            | Adolescente       |
| De 18 a 34            | Joven            |
| De 35 a 63            | Adulto           |
| Más de 63             | Adulto mayor     |

**Nota:** Esta tabla muestra el rango de edades de acuerdo con su Grupo Generacional.
"""

# Paso 1: Mostrar un mensaje de introducción al usuario
print("Bienvenido al programa de clasificación generacional.")
print("Este programa determinará a qué grupo generacional perteneces según tu edad.")

# Paso 2: Solicitar la edad de la persona
# Usamos int() porque la edad siempre será un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Paso 3: Clasificar a la persona según su grupo generacional usando if..elif..else
if edad <= 12:
    # Si la edad es menor o igual a 12, pertenece al grupo 'Niño'
    print("Perteneces al grupo generacional: Niño.")
elif 13 <= edad <= 17:
    # Si la edad está entre 13 y 17, pertenece al grupo 'Adolescente'
    print("Perteneces al grupo generacional: Adolescente.")
elif 18 <= edad <= 34:
    # Si la edad está entre 18 y 34, pertenece al grupo 'Joven'
    print("Perteneces al grupo generacional: Joven.")
elif 35 <= edad <= 63:
    # Si la edad está entre 35 y 63, pertenece al grupo 'Adulto'
    print("Perteneces al grupo generacional: Adulto.")
else:
    # Si la edad es mayor a 63, pertenece al grupo 'Adulto mayor'
    print("Perteneces al grupo generacional: Adulto mayor.")

# Paso 4: Mensaje final
print("¡Gracias por usar este programa! 😊")
