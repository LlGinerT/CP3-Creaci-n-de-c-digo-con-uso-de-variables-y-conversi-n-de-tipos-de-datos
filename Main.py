import datetime


def main():
    # Obtenemos la fecha actual con la clase date que nos facilitara operar con las fechas.
    fecha_actual = datetime.date.today()

    # Le pedimos al usuario que introduzca su fecha nacimiento (string)
    # y la transformamos en un objeto datetime, lo que nos permitirá operar con la fecha
    # y devolver un error si no se introduce en el formato que pedimos.
    while True:
        try:
            fecha_nacimiento = datetime.datetime.strptime(
                input("Ingrese su fecha de nacimiento (dd/mm/yyyy) "), "%d/%m/%Y"
            )
            break
        except ValueError:
            print("Por favor, introduzca una fecha válida en el formato dd/mm/yyyy.")

    # Comparamos el mes y dia actual, con el de nacimiento
    # a la vez que lo transformamos en un numero entero(int) lo que nos devuelve
    # 1(True) si no se han cumplido años este año o 0(false) si se han cumplido
    # asi podemos usarlo para el calculo de la edad exacta.
    ha_cumplido_anios = int(
        (fecha_actual.month, fecha_actual.day)
        < (
            fecha_nacimiento.month,
            fecha_nacimiento.day,
        )
    )
    # Calculamos la edad restando el año de nacimiento al año actual, y 1 año si aun no se han cumplido años.
    edad = fecha_actual.year - fecha_nacimiento.year - ha_cumplido_anios

    # Transformamos la edad a String para imprimirla.
    print("Su edad es de: " + str(edad) + " años")


if __name__ == "__main__":
    main()
