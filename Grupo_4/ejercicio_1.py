"""
Realizar el siguiente ejercicio con la instrucción if..else
En el Black Friday, la tienda de artículos deportivos “Sports” va
a realizar un descuento del 25% en toda su línea de productos
si el valor es mayor a 200000, le han solicitado a usted que
construya un programa que solicite el valor del producto a
comprar, muestre el valor del descuento si aplica y el valor final
a pagar.
"""

# Solicitar el valor del producto al usuario
# Usamos input para pedir el valor y convertimos la entrada a un número flotante (puede incluir decimales)
valor_producto = float(input("Ingresa el valor del producto: "))

# Comenzamos con la condición para aplicar el descuento
if valor_producto > 200000:  # Si el valor del producto es mayor a 200000:
    # Calculamos el descuento como el 25% del valor del producto
    descuento = valor_producto * 0.25
    # Calculamos el valor final a pagar restando el descuento al valor inicial
    valor_final = valor_producto - descuento
    # Mostramos los resultados
    print(f"El descuento aplicado es de: ${descuento:.2f}")
    print(f"El valor final a pagar es de: ${valor_final:.2f}")
else:  # Si el valor del producto es menor o igual a 200000:
    # No se aplica ningún descuento, el valor final es igual al valor del producto
    print("No aplica descuento.")
    print(f"El valor final a pagar es de: ${valor_producto:.2f}")
