"""
Realizar el siguiente ejercicio con la instrucción if..elif..else
En el Black Friday una tienda de tecnología va a realizar un
descuento del 15% en portátiles, del 12% en cámaras y del
6% en el resto de artículos. Usted debe construir un
programa que solicite al usuario el tipo de artículo a
comprar: portátil, cámara,otros, solicite el valor del artículo y
muestre el descuento y valorfinal a pagar.
"""
# Solicitar al usuario el tipo de artículo
articulo = input("Ingrese el tipo de artículo (portátil, cámara, otros): ").lower()

# Solicitar al usuario el valor del artículo
valor = float(input("Ingrese el valor del artículo: "))

# Aplicar el descuento según el tipo de artículo
if articulo == "portátil":
    descuento = valor * 0.15  # 15% de descuento para portátiles
    valor_final = valor - descuento  # Calcular el valor final a pagar
    print(f"Descuento aplicado: {descuento:.2f}")  # Mostrar el descuento con 2 decimales
    print(f"Valor final a pagar: {valor_final:.2f}")  # Mostrar el valor final a pagar con 2 decimales
elif articulo == "cámara":
    descuento = valor * 0.12  # 12% de descuento para cámaras
    valor_final = valor - descuento  # Calcular el valor final a pagar
    print(f"Descuento aplicado: {descuento:.2f}")  # Mostrar el descuento con 2 decimales
    print(f"Valor final a pagar: {valor_final:.2f}")  # Mostrar el valor final a pagar con 2 decimales
else:
    descuento = valor * 0.06  # 6% de descuento para otros artículos
    valor_final = valor - descuento  # Calcular el valor final a pagar
    print(f"Descuento aplicado: {descuento:.2f}")  # Mostrar el descuento con 2 decimales
    print(f"Valor final a pagar: {valor_final:.2f}")  # Mostrar el valor final a pagar con 2 decimales

