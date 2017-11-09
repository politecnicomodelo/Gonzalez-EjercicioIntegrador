from .Zonas import Zonas
from .Pais import Pais

class Continente(Zonas):
    Paises = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.Paises:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion