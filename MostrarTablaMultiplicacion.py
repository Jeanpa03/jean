def MostrarTabla(tablaMultiplicar):
    multiplicando = 1

    while multiplicando <=12:
        nuevoValor = tablaMultiplicar * multiplicando
        print("{0}*{1}={2}".format(tablaMultiplicar, multiplicando, nuevoValor))
        multiplicando = multiplicando + 1
        


tabla = int(input("digite la tabla que desea: "))
MostrarTabla(tabla)
