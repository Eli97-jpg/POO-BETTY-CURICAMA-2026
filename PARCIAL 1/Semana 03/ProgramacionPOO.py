class ClimaSemanal:
    """
    Clase que gestiona las temperaturas diarias
    y calcula el promedio semanal.
    """
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Solicita al usuario ingresar las temperaturas
        de una semana (7 días).
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de temperaturas.
        """
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resultado(self):
        """
        Muestra el promedio semanal del clima.
        """
        promedio = self.calcular_promedio()
        print(f"El promedio semanal del clima es: {promedio:.2f} °C")


def main():
    """
    Función principal del programa.
    """
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resultado()


if __name__ == "__main__":
    main()