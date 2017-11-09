from .Zonas import Zonas
from .Barrio import Barrio

class Ciudad(Zonas):
    Barrios = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.Barrios:
            poblacion = poblacion + item.Poblacion
        return poblacion