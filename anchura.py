
grafo = {'a': [('b',4), ('c',15), ('d',15)],
         'b': [('a',1), ('e',2), ('f',2)],
         'c': [('a',15), ('g',2)],
         'd': [('a',4), ('h',15)],
         'e': [('i',2), ('j',3), ('b',2)],
         'f': [('b',2)],
         'g': [('c',3)],
         'h': [('d',3), ('k',4), ('l',1)],
         'i': [('m',10), ('e',5), ('n',5)],
         'j': [('e',4)],
         'k': [('h',6)],
         'l': [('h',2)],
         'm': [('i',4)],
         'n': [('i',3)]
         }

visitados = []
cola = []

origen = input("Ingresa un nodo: ")
print("\nLista de recorrido en anchura\n")
cola.append(origen)
while cola:
    actual = cola.pop(0)
    if actual not in visitados:
        print("Vertice actual -> ", actual)
        visitados.append(actual)
    for key, lista in grafo[actual]:
        if key not in visitados:
            cola.append(key)
