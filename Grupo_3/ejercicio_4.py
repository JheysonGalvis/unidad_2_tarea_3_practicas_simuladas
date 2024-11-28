"""
Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)
Los investigadores de la escuela ECAPMA de la UNAD están
desarrollando un estudio para verificar si existe temporada de
heladas en sabana de Bogotá y le han solicitado su ayuda para
la construcción de un programa que valide la temporada acorde
a la temperatura así:
Tabla 5
Rango de temperaturas para las diferentes temporadas de
heladas en la sabana de Bogotá


| Rango de temperatura      | Temporada                        |
|---------------------------|-----------------------------------|
| Menor o igual a 6 grados  | Temporada de Heladas             |
| Mayor a 6 y menor a 12    | Temporada próxima a heladas      |
| Mayor de 12               | No hay temporada de heladas      |

"""

# Solicitar la temperatura al usuario
# La función input se utiliza para capturar datos desde el teclado.
# Convertimos la entrada a un número flotante (float) porque la temperatura puede incluir decimales.
temperatura = float(input("Ingresa la temperatura en grados: "))

# Comenzamos con las condiciones anidadas (if..else dentro de otro else)
if temperatura <= 6:  # Primera condición: si la temperatura es menor o igual a 6 grados.
    # Si esta condición es verdadera, estamos en "Temporada de Heladas".
    print("Temporada de Heladas")
else:  # Si no es menor o igual a 6 grados, evaluamos el siguiente rango.
    if temperatura < 12:  # Segunda condición: si la temperatura está entre 6 y menos de 12 grados.
        # Si esta condición es verdadera, estamos en "Temporada próxima a heladas".
        print("Temporada próxima a heladas")
    else:  # Si no es menor a 12 grados, entonces es mayor o igual a 12 grados.
        # En este caso, no hay temporada de heladas.
        print("No hay temporada de heladas")
