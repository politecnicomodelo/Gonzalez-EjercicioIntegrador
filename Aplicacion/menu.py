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
                    print("Paises: ")
                    for newItem in item.Paises:
                        print("   " + newItem.Nombre, "   " , newItem.Codigo)
            a = input("precione enter para continuar")
        if eleccion == 3:
            print("ingrese los sguientes datos")
            nuevoContinente = Continente()
            nuevoContinente.Nombre = input("Nombre: ")
            nuevoContinente.Coordenada.append(input("Coordenada W: "))
            nuevoContinente.Coordenada.append(input("Coordenada S: "))
            if(len(Continentes) != 0):
                nuevoContinente.Codigo = Continentes[len(Continentes) - 1].Codigo + 1
            else:
                nuevoContinente.Codigo = 1
            Continentes.append(nuevoContinente)

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
            a = 1
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
        a = 1
    elif eleccion == 5:
        a = 1
    elif eleccion == 6:
        print("Adios")