"""
2. Realizar el siguiente ejercicio con la instrucción if..else
La tienda de tecnología “Byte” desea construir un programa
que permita calcular el porcentaje de comisión de ventas
diarias de un vendedor, acorde a los rangos de venta así:
Tabla 8
Rango de ventas y su porcentaje de comisión.

| **Rango**                                    | **Porcentaje de comisión**  |
|----------------------------------------------|-----------------------------|
| Hasta 1 millón de ventas                     |            7%               |
| Más de un millón y menos de dos millones     |            9%               |
| Más de dos millones                          |           11%               |

"""

# Solicitar al usuario el valor de las ventas diarias
ventas = float(input("Ingrese el valor de las ventas diarias: "))

# Verificar el rango de ventas y calcular la comisión correspondiente
if ventas <= 1000000:
    # Si las ventas son hasta un millón, la comisión es del 7%
    comision = ventas * 0.07
    print(f"Porcentaje de comisión: 7%")
    print(f"Comisión ganada: {comision:.2f}")
elif ventas > 1000000 and ventas < 2000000:
    # Si las ventas son mayores a un millón y menores a dos millones, la comisión es del 9%
    comision = ventas * 0.09
    print(f"Porcentaje de comisión: 9%")
    print(f"Comisión ganada: {comision:.2f}")
else:
    # Si las ventas son mayores a dos millones, la comisión es del 11%
    comision = ventas * 0.11
    print(f"Porcentaje de comisión: 11%")
    print(f"Comisión ganada: {comision:.2f}")
