from .Zonas import Zonas
from .Pais import Pais

class Continente(Zonas):
    Paises = []

    def calcularPoblacion(self):
        poblacion = 0
        for item in self.Paises:
            poblacion = poblacion + item.calcularPoblacion()
        return poblacion

    def eliminar(self,codigo):
        i = 1
        for item in self.Paises:
            if item.Codigo == codigo:
                del self.Paises[i]
            i = i + 1