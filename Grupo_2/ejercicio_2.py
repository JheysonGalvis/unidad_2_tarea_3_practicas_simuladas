"""
Realizar el siguiente ejercicio con la instrucción if..else
Construir un programa que permita verificar si una persona es
mayor de edad. Para esto debe solicitar el año de nacimiento,
calcular la edad y si la edad es mayor o igual a 18 mostrar un
mensaje por consola que indique que la persona es mayor de
edad, de lo contrario que muestre un mensaje indicando que es
menor de edad
"""

# Paso 1: Mensaje introductorio
# Informamos al usuario lo que hace el programa.
print("Bienvenido al programa de verificación de mayoría de edad.")
print("Este programa te dirá si eres mayor o menor de edad basándose en tu año de nacimiento.\n")

# Paso 2: Solicitar el año de nacimiento
# Usamos la función input() para pedir al usuario que ingrese su año de nacimiento.
# Convertimos la entrada en un número entero con int(), ya que los cálculos requieren números.
anio_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))

# Paso 3: Calcular la edad
# Para calcular la edad, restamos el año de nacimiento del año actual.
# Aquí usamos la función date del módulo datetime para obtener el año actual.
from datetime import date
anio_actual = date.today().year  # Obtenemos el año actual.
edad = anio_actual - anio_nacimiento  # Calculamos la edad.

# Paso 4: Mostrar la edad calculada
# Esto es opcional, pero podemos mostrarle la edad calculada al usuario.
print(f"\nTu edad actual es: {edad} años.")

# Paso 5: Usar una estructura if..else para determinar si es mayor o menor de edad
if edad >= 18:
    # Si la edad es mayor o igual a 18, mostramos que la persona es mayor de edad.
    print("Eres mayor de edad. 🎉")
else:
    # Si la edad es menor a 18, mostramos que la persona es menor de edad.
    print("Eres menor de edad. 👶")

# Paso 6: Mensaje final
# Agregamos un mensaje de despedida para que el programa sea más interactivo.
print("\nGracias por usar este programa. ¡Hasta luego!")
