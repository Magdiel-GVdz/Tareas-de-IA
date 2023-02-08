
grafo = {'a': [('b',4), ('c',15), ('d',1)],
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
pila = []

origen = input("Ingresa un nodo: ")
print("\nLista de recorrido en profundidad\n")
# Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
pila.append(origen)
# Paso 2: MIENTRAS LA PILA NO ESTE VACÍA
while pila:
    # paso 3: DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
    actual = pila.pop()

    # paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
    if actual not in visitados:
        # paso 5: IMPRIMIR EL VÉRTICE ACTUAL
        print("Vertice actual -> ", actual)
        # paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
        visitados.append(actual)
    # paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
    #        Y QUE NO HA SIDO VISITADO:
    #        APILAR EL VERTICE
    for key, lista in grafo[actual]:
        if key not in visitados:
            pila.append(key)
