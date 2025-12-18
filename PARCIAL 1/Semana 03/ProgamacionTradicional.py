def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias
    de una semana (7 días).
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("=== PROMEDIO SEMANAL DEL CLIMA (TRADICIONAL) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal del clima es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()