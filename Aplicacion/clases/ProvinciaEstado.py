from .Zonas import Zonas
from .Ciudad import Ciudad

class ProvinciaEstado(Zonas):
    Ciudades = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.Ciudades:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion