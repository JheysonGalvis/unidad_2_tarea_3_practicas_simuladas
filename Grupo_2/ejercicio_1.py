"""
Realizar el siguiente ejercicio con la instrucción if..else
La escuela ECAPMA de la UNAD está desarrollando un estudio
para verificar el cambio climático en su ciudad. Para esto, le ha
pedido su ayuda en la construcción de un programa que solicite
las temperaturas de los últimos 5 días y muestre el promedio de
temperaturas si el promedio es mayor o igual a 22 grados,
debe informar que el clima es cálido si es menor que es frio.
"""

# Paso 1: Mensaje introductorio
# Explicamos al usuario lo que hace el programa.
print("Bienvenido al programa de análisis climático de la escuela ECAPMA.")
print("Este programa calcula el promedio de las temperaturas de los últimos 5 días.")
print("Dependiendo del promedio, indicará si el clima es cálido o frío.\n")

# Paso 2: Inicializar una lista para almacenar las temperaturas
# Usaremos una lista vacía para guardar las temperaturas ingresadas por el usuario.
temperaturas = []

# Paso 3: Solicitar las temperaturas al usuario
# Usamos un bucle para pedir 5 temperaturas y las guardamos en la lista.
for i in range(5):
    # Solicitamos la temperatura para el día i+1 (los días se numeran desde 1 hasta 5).
    temperatura = float(input(f"Por favor, ingresa la temperatura del día {i+1}: "))
    # Añadimos la temperatura ingresada a la lista.
    temperaturas.append(temperatura)

# Paso 4: Calcular el promedio de las temperaturas
# La función sum() suma todos los elementos de la lista, y len() obtiene la cantidad de elementos.
promedio = sum(temperaturas) / len(temperaturas)

# Paso 5: Mostrar el promedio al usuario
# Informamos el valor del promedio antes de analizar si el clima es cálido o frío.
print(f"\nEl promedio de las temperaturas es: {promedio:.2f} grados.")

# Paso 6: Usar una estructura if..else para determinar el clima
if promedio >= 22:
    # Si el promedio es mayor o igual a 22 grados
    print("El clima es cálido.")
else:
    # Si el promedio es menor a 22 grados
    print("El clima es frío.")

# Paso 7: Mensaje final
print("\nGracias por usar este programa. 🌞❄️")
