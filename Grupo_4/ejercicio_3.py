"""
Realizar el siguiente ejercicio con la instrucción if..elif..else
El equipo de futbol “los invencibles” está convocando ajóvenes
de su ciudad que quieran ser porteros. Para esto quiere saber
cuántos goles en contra ha tenido el aspirante en los últimos 5
partidos. Acorde a la siguiente tabla, mostrar el nivel en el cual
queda clasificado el aspirante:

| **Cantidad de goles** | **Nivel**  |
|------------------------|------------|
| Más de 12 goles        | Bajo       |
| Entre 5 y 12 goles     | Medio      |
| Entre 0 y 4 goles      | Alto       |


"""

# Solicitar al usuario la cantidad de goles recibidos
# Convertimos el valor ingresado a un número entero, ya que los goles son cantidades exactas
goles = int(input("Ingrese la cantidad de goles recibidos en los últimos 5 partidos: "))

# Comenzamos a evaluar los niveles con condicionales
if goles > 12:  # Si los goles son mayores a 12
    print("El nivel del aspirante es: Bajo")
elif 5 <= goles <= 12:  # Si los goles están entre 5 y 12 (inclusive)
    print("El nivel del aspirante es: Medio")
elif 0 <= goles <= 4:  # Si los goles están entre 0 y 4 (inclusive)
    print("El nivel del aspirante es: Alto")
else:  # Si el usuario ingresa un valor inválido (por ejemplo, goles negativos)
    print("Cantidad de goles no válida. Por favor ingrese un número mayor o igual a 0.")
