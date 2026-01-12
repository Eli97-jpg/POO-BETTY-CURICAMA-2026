"""
Conversión de temperatura de Celsius a Fahrenheit
Este programa permite ingresar datos básicos de un usuario y una temperatura en grados Celsius, convertirla a Fahrenheit y evaluar
si la temperatura es alta.

INDICADORES APLICADOS:
- Funcionalidad correcta
- Uso de tipos de datos
- Identificadores con snake_case
"""

# INDICADOR: Uso de Programación Orientada a Objetos
class Usuario:
    """
    Clase que representa al usuario del sistema.
    """

    def __init__(self, nombre: str, codigo: int):
        # INDICADOR: Uso de tipos de datos (string, int)
        self.nombre = nombre
        self.codigo = codigo


class ConvertidorTemperatura:
    """
    Clase encargada de realizar la conversión de temperatura.
    """

    def __init__(self, celsius: float):
        # INDICADOR: Uso del tipo de dato float
        self.celsius = celsius

    def convertir_a_fahrenheit(self) -> float:
        """
        Convierte grados Celsius a Fahrenheit.
        """
        # INDICADOR: Funcionalidad del programa
        return (self.celsius * 9 / 5) + 32

    def es_temperatura_alta(self) -> bool:
        """
        Verifica si la temperatura es mayor a 30 grados Celsius.
        """
        # INDICADOR: Uso del tipo de dato boolean
        return self.celsius > 30


def main():
    """
    Función principal del programa.
    """

    # INDICADOR: Identificadores descriptivos en snake_case
    nombre_usuario = input("Ingrese su nombre: ")  # string
    codigo_usuario = int(input("Ingrese su código de estudiante: "))  # int

    temperatura_celsius = float(
        input("Ingrese la temperatura en grados Celsius: ")
    )  # float

    # INDICADOR: Creación de objetos (POO)
    usuario = Usuario(nombre_usuario, codigo_usuario)
    convertidor = ConvertidorTemperatura(temperatura_celsius)

    # INDICADOR: Procesamiento de datos
    temperatura_fahrenheit = convertidor.convertir_a_fahrenheit()
    temperatura_alta = convertidor.es_temperatura_alta()

    # INDICADOR: Salida de información
    print("\n--- RESULTADOS ---")
    print(f"Usuario: {usuario.nombre}")
    print(f"Código: {usuario.codigo}")
    print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit:.2f}")
    print(f"¿La temperatura es alta?: {temperatura_alta}")


# INDICADOR: Estructura correcta del programa
if __name__ == "__main__":
    main()