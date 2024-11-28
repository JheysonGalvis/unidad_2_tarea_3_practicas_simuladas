"""Realizar el siguiente ejercicio con la instrucción if..else
Para el ingreso a la montaña rusa, el parque mundo locura valida
que la persona tenga una altura igual o superior a 1.20, para
ayudar a esta validación usted debe construir un programa que
solicite la altura y muestre un mensaje indicando si la persona
puede ingresar o no a la atracción"""

# Paso 1: Mostrar un mensaje inicial
print("¡Bienvenido al parque Mundo Locura!")
print("Vamos a validar si puedes ingresar a la montaña rusa.")

# Paso 2: Solicitar la altura de la persona
# Usamos float porque la altura puede incluir decimales (ejemplo: 1.25)
altura = float(input("Por favor, ingresa tu altura en metros: "))

# Paso 3: Validar si la altura es igual o mayor a 1.20
if altura >= 1.20:
    # Mensaje para el caso en que la persona puede ingresar
    print("¡Genial! Cumples con la altura requerida. Puedes ingresar a la montaña rusa.")
else:
    # Mensaje para el caso en que la persona no cumple con la altura
    print("Lo siento, no cumples con la altura mínima de 1.20 metros. No puedes ingresar.")

# Fin del programa
print("Gracias por visitar el parque Mundo Locura.")
