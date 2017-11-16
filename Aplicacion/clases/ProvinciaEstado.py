from .Zonas import Zonas
from .Ciudad import Ciudad

class ProvinciaEstado(Zonas):
    Ciudades = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.Ciudades:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion

    def eliminar(self,codigo):
        i = 1
        for item in self.Ciudades:
            if item.Codigo == codigo:
                del self.Ciudades[i]
            i = i + 1