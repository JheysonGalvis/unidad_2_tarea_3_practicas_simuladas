"""Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
La EPS “Mi Salud” ha solicitado su ayuda para la creación de un
programa que permita calcular el valor de la cuota moderadora
de un afiliado acorde a sus ingresos. Para esto, usted debe
solicitar que digiten el ingreso del afiliado y mostrar la cuota
moderadora acorde a esta tabla:"""

"""
**Tabla 2**  
*Rango de ingresos y su cuota moderadora.*

| Rango de ingresos              | Valor de la cuota moderadora |
|--------------------------------|------------------------------|
| Menor a 2 salarios mínimos     | 4000                         |
| Entre 2 y 5 salarios mínimos   | 15000                        |
| Mayor a 5 salarios mínimos     | 40000                        |

**Nota:** Esta tabla muestra el rango de edades para la aplicación de la cuota moderadora.

"""

# Paso 1: Mensaje introductorio
# Explicamos al usuario lo que hace el programa
print("Bienvenido al sistema de cálculo de cuota moderadora de la EPS 'Mi Salud'.")
print("Este programa calcula el valor de la cuota moderadora según el ingreso del afiliado.")

# Paso 2: Solicitar el ingreso mensual del usuario
# Usamos float() para permitir decimales, ya que el ingreso puede no ser un número entero.
ingreso = float(input("Por favor, ingresa tu salario mensual en términos de salarios mínimos: "))

# Paso 3: Condicionales anidados para determinar la cuota moderadora
if ingreso <= 2:
    # Si el ingreso es menor o igual a 2 salarios mínimos
    print("Tu cuota moderadora es de $4000.")
else:
    # Si el ingreso es mayor a 2, evaluamos otra condición
    if ingreso <= 5:
        # Si el ingreso está entre 2 y 5 salarios mínimos
        print("Tu cuota moderadora es de $15000.")
    else:
        # Si el ingreso es mayor a 5 salarios mínimos
        print("Tu cuota moderadora es de $40000.")

# Paso 4: Mensaje final
print("Gracias por usar este programa. 😊")

