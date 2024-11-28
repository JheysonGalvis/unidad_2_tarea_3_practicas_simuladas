"""
Realizar el siguiente ejercicio con la instrucción if..elif..else
El hospital la Misericordia le ha solicitado su ayuda para construir
un programa que permita verificar acorde a los resultados de
niveles de azúcar en ayunas si un paciente es diabético. Para
esto, usted debe solicitar el nivel de glucosa y dependiendo de
la siguiente tabla mostrar el resultado.

| Nivel de glucosa          | Criterio médico |
|---------------------------|-----------------|
| Menor o igual a 65 ml     | Hipoglucemia    |
| Mayor a 65 ml y menor a 100 ml | Normal     |
| Entre 100 y 110 ml        | Prediabetes     |
| Mayor a 110 ml            | Diabetes        |

"""

# Solicitar al usuario que ingrese el nivel de glucosa en ayunas
# Utilizamos input() para recibir la entrada del usuario y float() para convertirla a un número decimal
nivel_glucosa = float(input("Por favor, ingrese el nivel de glucosa en ayunas (en ml): "))

# Evaluar el nivel de glucosa y determinar el criterio médico correspondiente
# Usamos la estructura if..elif..else para realizar las comparaciones

if nivel_glucosa <= 65:
    # Si el nivel de glucosa es menor o igual a 65, se considera hipoglucemia
    print("Criterio médico: Hipoglucemia")
elif 65 < nivel_glucosa < 100:
    # Si el nivel de glucosa está entre 65 y 100 (sin incluir 100), se considera normal
    print("Criterio médico: Normal")
elif 100 <= nivel_glucosa <= 110:
    # Si el nivel de glucosa está entre 100 y 110 (incluyendo ambos), se considera prediabetes
    print("Criterio médico: Prediabetes")
else:
    # Si el nivel de glucosa es mayor a 110, se considera diabetes
    print("Criterio médico: Diabetes")
