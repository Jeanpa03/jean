def MostrarMenu():
    opcion = -1

    while opcion < 0 or opcion > 7:
        print("selecione una opcion del menu:/n/n")
        print("/t1: capturar una lista.")
        print("/t2: sacar los ultimos J valores.")
        print("/t3: invertir lista.")
        print("/t4: mostrar sub-conjunto.")
        print("/t5: mostrar elemnto dada una posicion.")
        print("/t6: buscar un elemento.")
        print("/t7: modificar la lista.")
        print("/n/n/t0: Salir.")

        opcion = int(input("opcion: "))

    return opcion

def MostrarSubMenu():
    opcion = -1

    while opcion < 0 or opcion > 6:
        print("selecione una opcion del submenu:/n/n")
        print("/t1: agregar elemento al final de la lista.")
        print("/t2: agregar elemento al inicio de la lista.")
        print("/t3: agregar elemento en una posicion dada.")
        print("/t4: agregar una nueva lista.")
        print("/t5: eliminar un elemento de una posicion dada.")
        print("/t6: buscar y eliminar un elemento.")
        print("/t7: modificar la lista.")
        print("\t0: salir")
       

        opcion = int(input("opcion: "))

    return opcion
def CapturarLista ():
    nuevaLista = []

    nuevaLista = [int(valor) for valor in input ().split()]

    return nuevaLista
def SacarValores (lista, j,l,k,m):
    lista = [j]
    lista.remove (j,l,k,m)
    print ('updated j set: ' , (lista))
    
        
    return lista

def InvertirLista(Lista):
    return lista [::-1]

def Subconjunto(lista, a ,h, s):
    return lista[d:h:s]

def ObtenerElemento(lista, posicion):
    return lista[posicion]

def BusquedaSecuencial(lista, Valor):
    return lista.index(Valor)

def AgregarElemento (lista, elemento, posicion) :
    lista.insert(posicion, elemento)

def AgregarNuevaLista(lista, alFinal):
    nuevaLista = CapturarLista()

    return lista + nuevaLista if alFinal else nuevaLista + lista

def EliminarPosicion(lista, posicion):
    del lista[posicion]

def EliminarElemento(lista, elemento):
    try:
        lista.remove(elemento)
    except:
        print("{0} no esta en la lista.".format (elemento))

listado = []
seleccion = -1

print(list(map(len, ["äbcd", "efg", "hijklm"])))
while seleccion !=0:
    print("la lista es: {0}, y su longitud {1}".format(listado, len(listado))) 
    seleccion = MostrarMenu()

    if seleccion == 1:
        listado = CapturarLista()
    elif seleccion ==2:
            nuevaEntrada = int(input("Digite la cantidad de valores a sacar: "))
            listado = SacarValores(listado, nuevaEntrada)
    elif seleccion ==3:
        print(InvertirLista(listado))
    elif seleccion ==4:
        desde = int(input("Desde: "))
        hasta = int(input("Hasta: "))
        step = int(input("Step: "))
        SubConjunto(listado, desde, hasta, step)
    elif seleccion == 5:
        pos = int(input("digite la posicion : "))
        print(ObtenerElemento(listado, pos))
    elif seleccion == 6:
        val = int(input("digite el valor: "))
        print(BusquedaSecuencial (listado, val))
    elif seleccion == 7:
        nuevaSeleccion = -1

    while nuevaSeleccion !=0:
        nuevaSeleccion = MostrarSubMenu()

        if nuevaSelecccion == 1:
            AgregarElemento(listado , int(input("Digite el nuevo valor:")), len(listado) )

        elif nuevaSeleccion == 2:
            AgregarElemento(listado , int(input("Digite el nuevo valor:")), 0)

        elif nuevaSeleccion ==3:
            AgregarElemento(listado , int(input("Digite el nuevo valor:")),int(input("Indique la posicion:")))

        elif nuevaSeleccion ==4:
            alFinal = input("Digite 1 para agregar al inicio, o 2 para agregar al final.") =="2" 
            listado = AgregarNuevaLista(listado, alFinal)        
 
        elif nuevaSeleccion == 5:

            EliminarPosicion(listado, int(input("Digite la posicion a eliminar: ")))  

        elif nuevaSeleccion == 6:
            EliminarElemento(listado, int(input("Digite el elemento a eliminar: ")))
                
        
