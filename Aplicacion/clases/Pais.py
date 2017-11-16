from .Zonas import Zonas
from .ProvinciaEstado import ProvinciaEstado

class Pais(Zonas):
    ProvinciaEstados = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.ProvinciaEstados:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion

    def eliminar(self,codigo):
        i = 1
        for item in self.ProvinciaEstados:
            if item.Codigo == codigo:
                del self.ProvinciaEstados[i]
            i = i + 1