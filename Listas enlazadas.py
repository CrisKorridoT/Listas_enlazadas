class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class Lista:
    def __init__(self, cabecera = None):
        self.primero = cabecera
        
    def imprimir(self):
        print("Lista")
        nodo_actual = self.primero
            while(nodo_actual):
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
            
    def nodo_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def nodo_final(self, valor):
        nuevo_nodo =Nodo(valor)
        nodo_actual = self.primero
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, valor):
        nodo_actual=self.primero
        while nodo_actual.siguiente.dato != valor:
            nodo_actual = nodo_actual.siguiente
        borrar_nodo = nodo_actual.siguiente
        nodo_actual.siguiente = borrar_nodo.siguiente

    def buscar(self, valor):
        nodo_actual=self.primero
        while nodo_actual.siguiente.dato != valor:
            nodo_actual = nodo_actual.siguiente
        print("Si existe")

    def contar(self):
        contador = 0
        nodo_actual = self.primero
        while nodo_actual != None:
            contador += 1
            nodo_actual=nodo_actual.siguiente
        print(contador)
    
      
  
     
nombres = Lista()

Juan = Nodo("Juan")
efmamjjasond = Nodo("efmamjjasond")
Nomin = Nodo("Nomin")

nombres.primero = Nomin
Nomin.siguiente = efmamjjasond
efmamjjasond.siguiente = Juan

nombres.imprimir()
nombres.contar()
nombres.nodo_inicio("Andres")
nombres.nodo_final("Camilo")
nombres.imprimir()
nombres.contar()
nombres.buscar("Juan")