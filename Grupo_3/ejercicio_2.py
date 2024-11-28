"""Realizar el siguiente ejercicio con la instrucción if..else
Construir una calculadora básica con las operaciones: suma,
resta, multiplicación y división. Para esto, debe solicitar al
usuario ingresar dos números y seleccionar qué operación desea
realizar y mostrar por consola el resultado."""

# Paso 1: Capturamos los dos números del usuario
print("¡Bienvenido a la calculadora básica!")
num1 = float(input("Ingresa el primer número: "))  # Capturamos el primer número, lo convertimos a float para permitir decimales
num2 = float(input("Ingresa el segundo número: "))  # Capturamos el segundo número

# Paso 2: Mostramos las opciones de operaciones al usuario
print("\nSelecciona la operación que deseas realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Paso 3: Capturamos la opción seleccionada por el usuario
operacion = input("\nIngresa el número de la operación (1/2/3/4): ")

# Paso 4: Realizamos la operación seleccionada utilizando condicionales if..else
if operacion == "1":  # Si el usuario seleccionó la opción 1 (Suma)
    resultado = num1 + num2  # Realizamos la suma
    print(f"El resultado de la suma es: {resultado}")  # Mostramos el resultado
elif operacion == "2":  # Si el usuario seleccionó la opción 2 (Resta)
    resultado = num1 - num2  # Realizamos la resta
    print(f"El resultado de la resta es: {resultado}")  # Mostramos el resultado
elif operacion == "3":  # Si el usuario seleccionó la opción 3 (Multiplicación)
    resultado = num1 * num2  # Realizamos la multiplicación
    print(f"El resultado de la multiplicación es: {resultado}")  # Mostramos el resultado
elif operacion == "4":  # Si el usuario seleccionó la opción 4 (División)
    if num2 != 0:  # Verificamos que el segundo número no sea 0 para evitar la división por 0
        resultado = num1 / num2  # Realizamos la división
        print(f"El resultado de la división es: {resultado}")  # Mostramos el resultado
    else:
        print("Error: No se puede dividir por cero.")  # Mensaje de error si el divisor es 0
else:
    print("Opción no válida. Por favor, selecciona una operación entre 1 y 4.")  # Mensaje si el usuario ingresa una opción inválida
