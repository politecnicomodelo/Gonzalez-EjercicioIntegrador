from Aplicacion.clases.Barrio import Barrio
from Aplicacion.clases.Ciudad import Ciudad
from Aplicacion.clases.ProvinciaEstado import ProvinciaEstado
from Aplicacion.clases.Pais import Pais
from Aplicacion.clases.Continente import Continente

Continentes = []
eleccion = 0

while(eleccion != 6):
    print("selecciones un tipo de zona")
    print("1: Continente")
    print("2: Pais")
    print("3: Provincia o Estado")
    print("4: Ciudad")
    print("5: Barrio")
    print("6: Salir")

    eleccion = int(input())

    if eleccion == 1:
        print("elija una opcion")
        print("1: ver lista de continentes")
        print("2: ver datos completos de un continente")
        print("3: ingresar un continente")
        print("4: eliminar continente")
        eleccion = int(input())
        if eleccion == 1:
            for item in Continentes:
                print("Nombre: ", item.Nombre, " Codigo: ", item.Codigo, " Coordenadas W: ", item.Coordenada[0], " S: ", item.Coordenada[1])
            a = input("precione enter para continuar")
        if eleccion == 2:
            print("ingrese el codigo del continente")
            codigo = int(input())
            for item in Continentes:
                if codigo == item.Codigo:
                    print("Nombre: " + item.Nombre)
                    print("Coordenadas W: " + item.Coordenada[0] + " S: " + item.Coordenada[1])
                    print("Poblacion: ", item.calcularPoblacion())
                    print("Paises: ")
                    for newItem in item.Paises:
                        print("   " + newItem.Nombre, "   " , newItem.Codigo)
            a = input("precione enter para continuar")
        if eleccion == 3:
            print("ingrese los siguientes datos")
            nuevoContinente = Continente()
            nuevoContinente.Nombre = input("Nombre: ")
            nuevoContinente.Coordenada.append(input("Coordenada W: "))
            nuevoContinente.Coordenada.append(input("Coordenada S: "))
            if(len(Continentes) != 0):
                nuevoContinente.Codigo = Continentes[len(Continentes) - 1].Codigo + 1
            else:
                nuevoContinente.Codigo = 1
            Continentes.append(nuevoContinente)
        if eleccion == 4:
            print("ingrese el codigo del continente")
            codigo = int(input(codigo))
            i = 1
            for item in self.Continentes:
                if item.Codigo == codigo:
                    del self.Continentes[i]
                i = i + 1
    elif eleccion == 2:
        print("elija una opcion")
        print("1: ver lista de paises")
        print("2: ver datos completos de un pais")
        print("3: ingresar un pais")
        eleccion = int(input())
        if eleccion == 1:
            print("ingrese el codigo del continente")
            codigo = int(input())
            for item in Continentes:
                if item.Codigo == codigo:
                    for item2 in item.Paises:
                        print("Nombre: ", item2.Nombre, " Codigo: ", item2.Codigo, " Coordenadas W: ", item2.Coordenada[0], " S: ", item2.Coordenada[1])
            input("presione enter para continuar")
        if eleccion == 2:
            print("ingrese el codigo del pais")
            codigo = int(input())
            n1 = codigo/100
            n1 = int(n1)
            for item in Continentes:
                if item.Codigo == n1:
                    for item2 in item.Paises:
                        if item2.Codigo == codigo:
                            print("Nombre: ", item2.Nombre)
                            print("Codigo: ", item2.Codigo)
                            print("Coordenadas W: ", item2.Coordenada[0], " S: ", item2.Coordenada[1])
                            print("Poblacion: ", item2.calcularPoblacion())
                            print("Provincias/Estados: ")
                            for item3 in item2.ProvinciaEstados:
                                print("   ", item3.Nombre, "   ", item3.Codigo)
            a = input("presione enter para continuar")
        if eleccion == 3:
            print("ingrese el codigo del continente")
            codigo = int(input())
            for item in Continentes:
                if item.Codigo == codigo:
                    nuevoPais = Pais()
                    nuevoPais.Nombre = input("Nombre: ")
                    nuevoPais.Coordenada.append(input("Coordenada W: "))
                    nuevoPais.Coordenada.append(input("Coordenada S: "))
                    if len(item.Paises) != 0:
                        nuevoPais.Codigo = item.Paises[len(item.Paises) - 1].Codigo + 1
                    else:
                        nuevoPais.Codigo = (item.Codigo * 100) + 1
                    item.Paises.append(nuevoPais)
    elif eleccion == 3:
        print("elija una opcion")
        print("1: ver lista de provincias/estados")
        print("2: ver datos completos de un provincia/estado")
        print("3: ingresar una provincia/estado")
        eleccion = int(input())
        if eleccion == 1:
            print("ingrese el codigo del pais")
            codigo = int(input())
            n1 = codigo / 100
            n1 = int(n1)
            for item in Continentes:
                if item.Codigo == n1:
                    for item2 in item.Paises:
                        if item2.Codigo == codigo:
                            for item3 in item2.ProvinciaEstados:
                                print("Nombre: ", item3.Nombre, " Codigo: ", item3.Codigo, " Coordenadas W: ", item3.Coordenada[0], " S: ", item3.Coordenada[1])
        if eleccion == 2:
            print("ingrese el codigo de la provincia/estado")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1 / 100)
            for item in Continentes:
                if item.Codigo == n2:
                    for item2 in item.Paises:
                        if item2.Codigo == n1:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == codigo:
                                    print("Nombre: ", item3.Nombre)
                                    print("Codigo: ", item3.Codigo)
                                    print("Coordenadas W: ", item3.Coordenada[0], " S: ", item3.Coordenada[1])
                                    print("Poblacion: ", item3.calcularPoblacion())
                                    print("Provincias/Estados: ")
                                    for item4 in item3.Ciudades:
                                        print("   ", item4.Nombre, "   ", item4.Codigo)
            a = input("presione enter para continuar")
        if eleccion == 3:
            print("ingrese el codigo del pais")
            codigo = int(input())
            n1 = codigo / 100
            n1 = int(n1)
            for item in Continentes:
                if item.Codigo == n1:
                    for item2 in item.Paises:
                        if item2.Codigo == codigo:
                            nuevaProvincia = ProvinciaEstado()
                            nuevaProvincia.Nombre = input("Nombre: ")
                            nuevaProvincia.Coordenada.append(input("Coordenada W: "))
                            nuevaProvincia.Coordenada.append(input("Coordenada S: "))
                            if len(item2.ProvinciaEstados) != 0:
                                nuevaProvincia.Codigo = item2.ProvinciaEstados[len(item2.ProvinciaEstados) - 1] + 1
                            else:
                                nuevaProvincia.Codigo = (item2.Codigo * 100) + 1
                            item2.ProvinciaEstados.append(nuevaProvincia)
    elif eleccion == 4:
        print("elija una opcion")
        print("1: ver lista de ciudades")
        print("2: ver datos completos de un ciudades")
        print("3: ingresar una ciudades")
        eleccion = int(input())
        if eleccion == 1:
            print("ingrese el codigo de la provincia/estado")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1/100)
            for item in Continentes:
                if item.Codigo == n2:
                    for item2 in item.Paises:
                        if item2.Codigo == n1:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == codigo:
                                    for item4 in item3.Ciudades:
                                        print("Nombre: ", item4.Nombre, " Codigo: ", item4.Codigo, " Coordenadas W: ", item4.Coordenada[0], " S: ", item4.Coordenada[1])
        if eleccion == 2:
            print("ingrese el codigo de la ciudad")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1 / 100)
            n3 = int(n2/100)
            for item in Continentes:
                if item.Codigo == n3:
                    for item2 in item.Paises:
                        if item2.Codigo == n2:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == n1:
                                    for item4 in item3.Ciudades:
                                        if item4.Codigo == codigo:
                                            print("Nombre: ", item4.Nombre)
                                            print("Codigo: ", item4.Codigo)
                                            print("Coordenadas W: ", item4.Coordenada[0], " S: ", item4.Coordenada[1])
                                            print("Poblacion: ", item4.calcularPoblacion())
                                            print("Provincias/Estados: ")
                                            for item5 in item4.Barrios:
                                                print("   ", item5.Nombre, "   ", item5.Codigo)
        if eleccion == 3:
            print("ingrese el codigo de la provincia/estado")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1/100)
            for item in Continentes:
                if item.Codigo == n2:
                    for item2 in item.Paises:
                        if item2.Codigo == n1:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == codigo:
                                    nuevaCiudad = Ciudad()
                                    nuevaCiudad.Nombre = input("Nombre: ")
                                    nuevaCiudad.Coordenada.append(input("Coordenada W: "))
                                    nuevaCiudad.Coordenada.append(input("Coordenada S: "))
                                    if len(item3.Ciudades) != 0:
                                        nuevaCiudad.Codigo = item3.Ciudades[len(item3.Ciudades) - 1] + 1
                                    else:
                                        nuevaCiudad.Codigo = (item3.Codigo * 100) + 1
                                        item3.Ciudades.append(nuevaCiudad)
    elif eleccion == 5:
        print("elija una opcion")
        print("1: ver lista de barrios")
        print("2: ver datos completos de un barrios")
        print("3: ingresar una barrios")
        eleccion = int(input())
        if eleccion == 1:
            print("ingrese el codigo de la ciudad")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1 / 100)
            n3 = int(n2 / 100)
            for item in Continentes:
                if item.Codigo == n3:
                    for item2 in item.Paises:
                        if item2.Codigo == n2:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == n1:
                                    for item4 in item3.Ciudades:
                                        if item4.Codigo == codigo:
                                            for item5 in item4.Barrios:
                                                print("Nombre: ", item5.Nombre, " Codigo: ", item5.Codigo, " Coordenadas W: ",
                                                item5.Coordenada[0], " S: ", item5.Coordenada[1])
        if eleccion == 2:
            print("ingrese el codigo del barrio")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1 / 100)
            n3 = int(n2 / 100)
            n4 = int(n3 / 100)
            for item in Continentes:
                if item.Codigo == n4:
                    for item2 in item.Paises:
                        if item2.Codigo == n3:
                            for item3 in item2.ProvinciaEstados:
                                if item3.Codigo == n2:
                                    for item4 in item3.Ciudades:
                                        if item4.Codigo == n1:
                                            for item5 in item4.Barrios:
                                                if item5.Codigo == codigo:
                                                    print("Nombre: ", item5.Nombre)
                                                    print("Codigo: ", item5.Codigo)
                                                    print("Coordenadas W: ", item5.Coordenada[0], " S: ", item5.Coordenada[1])
                                                    print("Poblacion: ", item5.Poblacion)
        if eleccion == 3:
            print("ingrese el codigo de la ciudad")
            codigo = int(input())
            n1 = int(codigo / 100)
            n2 = int(n1 / 100)
            n3 = int(n2 / 100)
            for item in Continentes:
                if item.Codigo == n3:
                    for item2 in item.Paises:
                        if item2.Codigo == n2:
                            for item3 in item.ProvinciaEstados:
                                if item3.Codigo == n1:
                                    for item4 in item3.Ciudades:
                                        if item4.Codigo == codigo:
                                            nuevoBarrio = Barrio()
                                            nuevoBarrio.Nombre = input("Nombre: ")
                                            nuevoBarrio.Coordenada.append(input("Coordenada W: "))
                                            nuevoBarrio.Coordenada.append(input("Coordenada S: "))
                                            nuevoBarrio.Poblacion = input("Poblacion: ")
                                            if len(item4.Ciudades) != 0:
                                                nuevoBarrio.Codigo = item4.Barrios[len(item4.Barrios) - 1] + 1
                                            else:
                                                nuevoBarrio.Codigo = (item4.Codigo * 100) + 1
                                                item4.Barrios.append(nuevoBarrio)
    elif eleccion == 6:
        print("Adios")