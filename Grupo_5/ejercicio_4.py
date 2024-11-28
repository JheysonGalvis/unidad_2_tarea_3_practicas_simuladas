"""
Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
La agencia de caminantes “el sendero” está otorgando
descuentos en sus caminatas, acorde a la cantidad de
participantes del grupo. Para esto, dependiendo de la
cantidad de personas que deseen tomar la caminata se
otorgará un descuento así:

| **Cantidad de personas**                     |         **Descuento**       |
|----------------------------------------------|-----------------------------|
| De dos a 4 personas                          |            12%              |
| De 5 a 10 personas                           |            17%              |
| Más de 10 personas                           |            22%              |

"""

# Paso 1: Solicitamos al usuario la cantidad de personas que participarán en la caminata
print("Bienvenido a la agencia de caminatas 'El Sendero'.")
personas = int(input("¿Cuántas personas desean tomar la caminata? Ingresa el número de personas: "))  # Capturamos la cantidad de personas

# Paso 2: Verificamos el descuento usando condicionales anidados
if personas >= 2 and personas <= 4:  # Si la cantidad de personas está entre 2 y 4 (inclusive)
    descuento = 12  # El descuento es del 12%
    print(f"El descuento aplicado es del {descuento}%")  # Mostramos el descuento
else:  # Si la cantidad de personas no está entre 2 y 4, entramos aquí
    if personas >= 5 and personas <= 10:  # Si la cantidad de personas está entre 5 y 10 (inclusive)
        descuento = 17  # El descuento es del 17%
        print(f"El descuento aplicado es del {descuento}%")  # Mostramos el descuento
    else:  # Si la cantidad de personas no está entre 5 y 10, entramos aquí
        if personas > 10:  # Si la cantidad de personas es mayor que 10
            descuento = 22  # El descuento es del 22%
            print(f"El descuento aplicado es del {descuento}%")  # Mostramos el descuento
        else:  # Si la cantidad de personas es menor a 2
            print("No se aplica descuento. La cantidad de personas es insuficiente.")  # Mensaje para menos de 2 personas
