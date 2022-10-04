class Vehiculo:
        color = ""
        ruedas = ""
        puertas = ""

class Coche(Vehiculo):
        velocidad = ""
        cilindrada = ""

suzuki = Coche()
suzuki.color = "Rojo"
suzuki.ruedas = 4
suzuki.puertas = 4
suzuki.velocidad = "180 km/h"
suzuki.cilindrada = "No se que es eso"

print(suzuki.color)
print(suzuki.ruedas)
print(suzuki.puertas)
print(suzuki.velocidad)
print(suzuki.cilindrada)



