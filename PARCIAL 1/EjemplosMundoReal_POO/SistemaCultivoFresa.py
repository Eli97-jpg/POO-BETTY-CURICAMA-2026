# Sistema de cultivo de fresas
# cultivo de fresa

class Fresa:
    def __init__(self, edad_dias):
        self.edad_dias = edad_dias
        self.altura_cm = 8
        self.frutos = 0

    def desarrollo(self):
        self.edad_dias += 1
        self.altura_cm += 0.6

    def producir_frutos(self):
        if self.edad_dias >= 20:
            self.frutos += 3
            print("La planta de fresa produjo frutos.")
        else:
            print("La planta aún es joven para producir frutos.")

    def mostrar_estado(self):
        print(
            f"Edad: {self.edad_dias} días | "
            f"Altura: {self.altura_cm} cm | "
            f"Frutos: {self.frutos}"
        )


# Objeto planta
planta = Fresa(25)
planta.mostrar_estado()
planta.desarrollo()
planta.desarrollo()
planta.producir_frutos()
planta.mostrar_estado()