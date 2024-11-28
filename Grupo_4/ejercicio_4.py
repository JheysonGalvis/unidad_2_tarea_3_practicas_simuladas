"""
Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
Los alumnos del profesor Juan requieren un programa que les
indique si han aprobado el curso. Para esto, usted debe solicitar
la nota definitiva y si dicha nota es menor a 3, muestre un
mensaje indicando que no ha aprobado el curso. Si es igual 3 y
menor a 4.5 debe mostrar un mensaje que informe que el
alumno ha aprobado el curso, si la nota es mayor a 4.5 muestre
el mensaje que ha probado el curso con un desempeño superior.
"""

# Solicitar al usuario la nota definitiva
# Convertimos la entrada a un número flotante porque las notas pueden tener decimales
nota = float(input("Ingrese su nota definitiva: "))

# Primera condición: Si la nota es menor a 3
if nota < 3:
    print("No ha aprobado el curso.")
else:  # Caso contrario (nota >= 3), evaluamos más condiciones
    if nota < 4.5:  # Si la nota está entre 3 y 4.5
        print("Ha aprobado el curso.")
    else:  # Si la nota es mayor o igual a 4.5
        print("Ha aprobado el curso con un desempeño superior.")

