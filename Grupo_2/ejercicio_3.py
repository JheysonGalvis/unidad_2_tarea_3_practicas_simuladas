"""Realizar el siguiente ejercicio con la instrucción if..elif..else
El almacén “viste con estilo” requiere de su ayuda para construir
un programa que permita calcular la talla de ropa acorde a la
altura ingresada así (la altura debe capturarse en centímetros):"""

"""
**Tabla 3**  
*Rango de ingresos y su cuota moderadora.*

| Altura                           | Talla |
|----------------------------------|-------|
| Menor o igual a 150              | S     |
| Mayor a 150 y menor a 170        | M     |
| Mayor o igual a 170 y menor a 180| L     |
| Mayor o igual a 180              | XL    |

"""

# Paso 1: Mensaje introductorio
# Explicamos brevemente lo que hace el programa.
print("Bienvenido al programa de cálculo de talla de ropa.")
print("Por favor, ingresa tu altura en centímetros para determinar tu talla.\n")

# Paso 2: Solicitar la altura
# Usamos la función input() para que el usuario introduzca su altura.
# Convertimos el valor a número entero con int(), ya que trabajaremos con números.
altura = int(input("Ingresa tu altura en centímetros: "))

# Paso 3: Evaluar la altura con if..elif..else
# Comparamos la altura ingresada con los rangos definidos en la tabla.

if altura <= 150:
    # Si la altura es menor o igual a 150 cm, la talla es "S".
    talla = "S"
elif altura > 150 and altura < 170:
    # Si la altura está entre 151 y 169 cm (excluyendo 170), la talla es "M".
    talla = "M"
elif altura >= 170 and altura < 180:
    # Si la altura está entre 170 y 179 cm (excluyendo 180), la talla es "L".
    talla = "L"
else:
    # Si la altura es mayor o igual a 180 cm, la talla es "XL".
    talla = "XL"

# Paso 4: Mostrar la talla calculada
# Imprimimos el resultado al usuario.
print(f"\nCon una altura de {altura} cm, tu talla de ropa es: {talla}.\n")

# Paso 5: Mensaje final
# Agregamos un mensaje de despedida para mejorar la experiencia del usuario.
print("Gracias por usar el programa. ¡Que tengas un buen día!")
