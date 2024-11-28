"""
Realizar el siguiente ejercicio con la instrucción if..else
Para incentivar las compras, la cadena de almacenes “el
triunfo” está otorgando un 15% de descuento en todos sus
productos que se aplica si el valor de la compra es mayor de
300000. Usted debe construir un programa que permita
calcular este descuento, solicitando al usuario el valor del
artículo, calculando el descuento y mostrando el valor a
pagar.
"""

# Solicitar al usuario el valor del artículo
# Utilizamos float() para permitir decimales en el valor del artículo
valor_articulo = float(input("Ingrese el valor del artículo: "))

# Verificar si el valor es mayor a 300000 para aplicar descuento
if valor_articulo > 300000:
    # Calculamos el descuento (15%)
    descuento = valor_articulo * 0.15
    # Calculamos el valor final a pagar, restando el descuento
    valor_a_pagar = valor_articulo - descuento
    # Mostrar el valor del descuento y el valor final a pagar
    print(f"Se aplica un descuento de: {descuento:.2f}")
    print(f"El valor a pagar con descuento es: {valor_a_pagar:.2f}")
else:
    # Si el valor no es mayor a 300000, no hay descuento
    print(f"No se aplica descuento. El valor a pagar es: {valor_articulo:.2f}")
