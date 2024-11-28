"""Realizar el siguiente ejercicio con la instrucción if..else
El profesor Juan ha solicitado su ayuda para calcular el
promedio de 5 notas del curso de 1 estudiante. Usted debe
construir un programa que solicite las 5 notas, las sume y
muestre el promedio, además si el promedio es mayor o
igual a 3 debe decir curso aprobado, sino entonces curso no
aprobado"""

# Paso 1: Mostrar un mensaje inicial
print("¡Bienvenido! Vamos a calcular el promedio de 5 notas.")

# Paso 2: Solicitar las notas al usuario
# Aquí usamos float para permitir números con decimales (ejemplo: 3.5, 4.2)
nota1 = float(input("Por favor, ingresa la primera nota: "))
nota2 = float(input("Por favor, ingresa la segunda nota: "))
nota3 = float(input("Por favor, ingresa la tercera nota: "))
nota4 = float(input("Por favor, ingresa la cuarta nota: "))
nota5 = float(input("Por favor, ingresa la quinta nota: "))

# Paso 3: Calcular la suma de las notas
suma_notas = nota1 + nota2 + nota3 + nota4 + nota5

# Paso 4: Calcular el promedio
promedio = suma_notas / 5

# Paso 5: Usar una estructura if..else para evaluar el promedio
# Si el promedio es mayor o igual a 3, el curso está aprobado
if promedio >= 3:
    # Mensaje para el caso aprobado
    print(f"El promedio es {promedio:.2f}. ¡Curso aprobado!")
else:
    # Mensaje para el caso no aprobado
    print(f"El promedio es {promedio:.2f}. Curso no aprobado.")

# Fin del programa
print("Gracias por usar este programa.")
