"""
Realizar el siguiente ejercicio con la instrucción if..else
La tienda deportiva “Sports” desea realizar una campaña de
fidelización con sus clientes y dependiendo del día de la semana,
creará campañas para los fanáticos de un deporte; construir un
programa en el cual ingrese el día de la semana y muestre por
consola qué artículos del deporte asociado tendrán descuento:

| **Día**      | **Deporte**    |
|--------------|----------------|
| Lunes        | Fútbol         |
| Martes       | Tenis          |
| Miércoles    | Ciclismo       |
| Jueves       | Atletismo      |
| Viernes      | Natación       |
| Sábado       | Montañismo     |


"""

# Solicitar al usuario el día de la semana
# Usamos input para capturar el día y lo convertimos a minúsculas para evitar problemas con mayúsculas.
dia = input("Ingresa el día de la semana: ").strip().lower()

# Comenzamos con las condiciones if..else
if dia == "lunes":  # Si el día es lunes
    print("Los artículos de Fútbol tienen descuento.")
elif dia == "martes":  # Si el día es martes
    print("Los artículos de Tenis tienen descuento.")
elif dia == "miércoles":  # Si el día es miércoles
    print("Los artículos de Ciclismo tienen descuento.")
elif dia == "jueves":  # Si el día es jueves
    print("Los artículos de Atletismo tienen descuento.")
elif dia == "viernes":  # Si el día es viernes
    print("Los artículos de Natación tienen descuento.")
elif dia == "sábado":  # Si el día es sábado
    print("Los artículos de Montañismo tienen descuento.")
else:  # Si el día ingresado no es válido
    print("Día no válido. Por favor ingresa un día de lunes a sábado.")
