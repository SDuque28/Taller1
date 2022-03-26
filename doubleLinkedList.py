import math

class DoubleLinkedList:
    #Creamos la clase nodo anidada
    class Node:
        #Creamos el metodo inicializador
        def __init__(self,value):
            self.value = value
            self.next_node = None
            self.previous_node = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #Mostrar la lista
    def show_doubleLinkedList(self):
        #Esta lista es la que almacenara la lista doblemente enlazada
        array_doubleLinkedList = []
        current_node = self.head
        while current_node != None:
            #Unicamente almacenamos en la lista el valor del nodo
            array_doubleLinkedList.append(current_node.value)
            current_node = current_node.next_node
        print(array_doubleLinkedList)
    #Metodos para añadir nodos al inicio de la lista
    def prepend_node(self,value):
        #Al nuevo nodo le asignamos la estructura real de la clase node
        new_node = self.Node(value)
        #Validamos si no hay ni cabeza ni cola
        if self.head == None and self.tail == None:
            #La cabeza toma el valor del nuevo nodo
            self.head = new_node
            #La cola toma el valor del nuevo nodo
            self.tail = new_node
            self.length += 1
        else:
            #El enlace anterior de la actual cabeza conecta con un nuevo nodo
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            self.length += 1
    
    def append_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            #La cabeza toma el valor del nuevo nodo
            self.head = new_node
            #La cola toma el valor del nuevo nodo
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
            self.length += 1
    #Eliminar el primer nodo de la lista    
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            #El nodo a eliminar es la cabeza
            remove_node = self.head
            #La nueva cabeza sera el nodo siguente a la cabeza
            self.head = remove_node.next_node
            remove_node.next_node = None
            self.length -= 1
            print(f'El nodo que se elimino es: {remove_node.value}')
    #Eliminar el ultimo nodo de la lista
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.tail
            self.tail = remove_node.previous_node
            self.tail.next_node = None
            remove_node.previous_node = None
            self.length -= 1
            print(f'El nodo que se elimino fue: {remove_node.value}')
    #Método para obtener un nodo en una posicion especifica
    def get_node_value(self, index):
        if(index == self.length+1):
            return self.tail
        elif(index == 1):
            return self.head
        elif not (index > self.length+1 or index < 1):
            #Búsqueda rápida del nodo
            middle_index = int(self.length/2)
            if(index < middle_index):
                current_node = self.head
                count_node = 0
                while(count_node != index):
                    #Aumentamos en 1 el recorrido de los nodos
                    current_node = current_node.next_node
                    #Incrementamos en uno el contador de nodos
                    count_node += 1
                return current_node
            else:
                current_node = self.tail
                count_node = self.length 
                while(count_node != index):
                    current_node = current_node.previous_node
                    count_node -= 1
                return current_node
        else:
            print('El indice no pertenece a la lista')
        
    
    def insert(self,index,value):
        if index == self.length +1:
            return self.append_node(value)
        elif index == 1:
            return self.prepend_node(value)
        elif not index > self.length+1 or index < 1:
            new_node = self.Node(value)
            nodos_anteriores = self.get_node_value(index-1)
            nodos_siguientes = nodos_anteriores.next_node
            nodos_anteriores.next_node = new_node
            new_node.previous_node = nodos_anteriores
            new_node.next_node = nodos_siguientes
            nodos_siguientes.previous_node = new_node
            self.length += 1
        else:
            return None
        
    def Punto_1(self,index):
        nodo_objetivo = self.get_node_value(index)
        if nodo_objetivo != None:
            if nodo_objetivo.previous_node != None:
                try:
                    nodo_objetivo.value = str(math.pow(int(nodo_objetivo.previous_node.value),2))
                except ValueError:
                    print('El valor previo al nodo a cambiar no es un entero')
            else:
                print('No hay un nodo previo')
    
    def Punto_2(self,index,value):
        try:
            current_node = self.get_node_value(index)
            if(current_node != None):
                if(int(value) % int(current_node.value) == 0):
                    self.insert(index,value)
                else:
                    print('El numero selecionado no es multiplo del siguiente')
            else:
                print('El nodo no tiene numero siguiente')
        except ValueError:
            print('El valor debe de ser dado o del nodo siguiente debe de ser numerico')
    
    def Punto_3(self,index):
        if(index == 1):
            return self.shift_node()
        elif index == self.length:
            return self.pop_node()
        elif not index > self.length or index < 1:
            nodos_anteriores = self.get_node_value(index-1)
            nodos_siguientes = self.get_node_value(index+1)
            nodo_removido = nodos_anteriores.next_node
            nodos_anteriores.next_node = nodos_siguientes
            nodos_siguientes.previous_node = nodos_anteriores
            nodo_removido.next_node = None
            nodo_removido.previous_node = None
            self.length -= 1
            return nodo_removido
        else:
            return None
        
    def Punto_4(self):
        try:
            reverse_nodes = None
            current_node = self.head
            self.tail = current_node
            while current_node != None:
                current_node.value = str(round(math.sqrt(float(current_node.value)),2))
                next_node = current_node.next_node
                current_node.next_node = reverse_nodes
                reverse_nodes = current_node
                reverse_nodes.previous_node = next_node
                current_node = next_node
            self.head = reverse_nodes
        except ValueError:
            print('Todos los valores deven de ser numericos')
            