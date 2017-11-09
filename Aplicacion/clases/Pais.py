from .Zonas import Zonas
from .ProvinciaEstado import ProvinciaEstado

class Pais(Zonas):
    ProvinciaEstados = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.ProvinciaEstados:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion