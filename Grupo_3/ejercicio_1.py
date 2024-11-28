"""Realizar el siguiente ejercicio con la instrucción if..else
El restaurante “doña Pancha” desea construir un programa para
calcular el valor de la propina sugerida. Para esto, usted debe
solicitar el valor de la cuenta, si el valor es menor o igual a
50000 la propina a calcular es el 10% de ese valor, si es mayor
la propina sugerida es del 5%, por ultimo debe mostrar así el
valor de la propina sugerida."""

# Paso 1: Capturar el valor de la cuenta
print("Bienvenido al restaurante Doña Pancha")
valor_cuenta = float(input("Por favor ingresa el valor de tu cuenta: "))  # Capturamos el valor de la cuenta, lo convertimos a float porque puede tener decimales

# Paso 2: Evaluar si el valor de la cuenta es menor o igual a 50,000 o mayor
if valor_cuenta <= 50000:  # Si el valor de la cuenta es menor o igual a 50,000
    propina = valor_cuenta * 0.10  # La propina es el 10% del valor de la cuenta
else:  # Si el valor de la cuenta es mayor a 50,000
    propina = valor_cuenta * 0.05  # La propina es el 5% del valor de la cuenta

# Paso 3: Mostrar el valor de la propina sugerida
print(f"La propina sugerida es: {propina:.2f}")  # Mostramos el valor de la propina con dos decimales

