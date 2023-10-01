class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

    def obtener_nodo(self):
        return self.dato

    def obtener_nodo_siguiente(self):
        return self.siguiente


class Lista:
    def __init__(self, cabecera=None):
        self.primero = cabecera

    def imprimir(self):
        print("Lista")
        nodo_actual = self.primero
        while (nodo_actual):
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def nodo_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def nodo_final(self, valor):
        nuevo_nodo = Nodo(valor)
        nodo_actual = self.primero
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, valor):
        nodo_actual = self.primero
        while nodo_actual.siguiente.dato != valor:
            nodo_actual = nodo_actual.siguiente
        borrar_nodo = nodo_actual.siguiente
        nodo_actual.siguiente = borrar_nodo.siguiente

    def lista_vacia(self):
        if (self.primero == None):
            print("La lista esta vacia")
        else:
            print("La lista no esta vacia")

    def agregar_nodo_entre_elementos(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        if posicion == 0:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            return
        recorrer_lista = self.primero
        contador = 0
        while recorrer_lista and contador < posicion:
            if contador == posicion-1:
                nuevo_nodo.siguiente = recorrer_lista.siguiente
                recorrer_lista.siguiente = nuevo_nodo
                return
            recorrer_lista = recorrer_lista.siguiente
            contador += 1
        if contador == posicion:
            recorrer_lista.siguiente = nuevo_nodo



nombres = Lista()

Juan = Nodo("Juan")
efmamjjasond = Nodo("efmamjjasond")
Nomin = Nodo("Nomin")

nombres.primero = Nomin
Nomin.siguiente = efmamjjasond
efmamjjasond.siguiente = Juan

nombres.nodo_inicio("Andres")
nombres.nodo_final("Camilo")
nombres.imprimir()
nombres.eliminar_nodo("Nomin")
nombres.eliminar_nodo("Camilo")
nombres.agregar_nodo_entre_elementos("David",2)
nombres.imprimir()
nombres.lista_vacia()
