import random
from itertools import combinations_with_replacement

def crearMochila(m):
    lista = []
    for j in range(m):
        lista.append(random.randint(0, 1))
    return lista

def DiversificationGenerationMethod(n,m):
    poblacion = []
    for i in range(0,n):
        poblacion.append(crearMochila(m))
    return poblacion

def ImprovementMethod(listaDeListas):
    maximo = len(listaDeListas)-1
    m = len(listaDeListas[0])
    nuevaLista = []
    for lis in listaDeListas:
        if lis not in nuevaLista:
            nuevaLista.append(lis)
    topeNuevaLista = len(nuevaLista)-1
    while(topeNuevaLista < maximo):
        nuevaMochila = crearMochila(m)
        nuevaLista.append(nuevaMochila)
        topeNuevaLista = len(nuevaLista)-1
    return nuevaLista

def calcularCalidad(mochila):
    i = 0
    calidad = 0
    pesoTotal= 0
    caloriasTotales=0
    for esta in mochila:    
        if esta:
            pesoTotal = despensa[i][1] + pesoTotal
            caloriasTotales = despensa[i][2] + caloriasTotales
            calidad = caloriasTotales / pesoTotal
        i = i + 1
    return calidad

def ReferenceSetUpdateMethod(conjunto,Ref):
    calidadMayor = 0.0
    posicion = 0
    mejorPosicion = 0
    refSet = []
    conjunto = conjunto + Ref
    while(len(refSet) < tamañoRefSef):
        for obj in conjunto:
            calidadObj = calcularCalidad(obj)
            if calidadMayor < calidadObj:
                calidadMayor = calidadObj
                mejorPosicion = posicion
        
            posicion = posicion +1
        calidadMayor = 0.0
        posicion = 0

        mejorElemento = conjunto.pop(mejorPosicion)
        refSet.append(mejorElemento)

        mostrar = False
        if mostrar:
            print("#####################################################")
            print(f"tamaño de refsef {len(refSet)}")
            print(f"mejor posicion {mejorPosicion}")
            print(f"mejor elemento {mejorElemento}")
            print(f"calidad {calcularCalidad(mejorElemento)}")
        
    return refSet

def SubsetGenerationMethod(Ref):
    subSet = list(combinations_with_replacement(Ref, 2))
    return subSet

def combine_genes(parent1,parent2):
    parent1 = list(parent1)
    parent2 = list(parent2)
    new_order = parent1.copy()
    for i in range(len(parent1)):
        if(random.randint(0, 1) == 1): #flip a coin
            idx = new_order.index(parent2[i])
            new_order[idx] = new_order[i]
            new_order[i] = parent2[i]
    return new_order

def SolutionCombinationMethod(subSet):
    hijos = []
    for padres in subSet:
        hijo = combine_genes(padres[0],padres[1])
        hijos.append(hijo)
        #print(hijo)
    return hijos

def mostrarLista(listaAMostrar, mostrarCalidad):
    for lista in listaAMostrar:
        print(lista)
        if mostrarCalidad:
            cal = calcularCalidad(lista)
            print(f"calidad {cal}")
    print("#####################################################")

tamañoPoblacion = 100
tamañoRefSef = 10
tamañoMochila = 10
p = []
pMejorada = []
RefSef = []
subSetCombination = []
subSet = []

despensa = [
    ["",4,100],
    ["",2,360],
    ["",5,650],
    ["",4,200],
    ["",7,850],
    ["",4,300],
    ["",6,250],
    ["",5,500],
    ["",9,850],
    ["",7,500]
]  

"""
Algoritmo Scatter Search

1.  Comenzar con P = Ø. Utilizar el método de
    generación para construir una solución y el
    método de mejora para tratar de mejorarla; sea x 
    la solución obtenida. Si x ∉ P entonces añadir x a
    P. (i.e., P = P u x), en otro caso, rechazar x.
    Repetir esta etapa hasta que P tenga un tamaño
    prefijado.
"""

p = DiversificationGenerationMethod(tamañoPoblacion,tamañoMochila)
pMejorada = ImprovementMethod(p)

mostrarSolucionesIniciales = True
if(mostrarSolucionesIniciales):
    print("")
    print("poblacion inicial mejorada: ")
    print("")
    mostrarLista(pMejorada,True)

"""
2.  Construir el conjunto de referencia RefSet = { x1, ..., xb} 
    con las b/2 mejores soluciones de P
    y las b/2 soluciones de P más diversas a las ya
    incluidas.
3.  Evaluar las soluciones en RefSet y ordenarlas de
    mejor a peor respecto a la función objetivo.
"""

RefSef = ReferenceSetUpdateMethod(pMejorada, RefSef)
RefSefOriginal = list(RefSef)

mostrarRefSef = True
if(mostrarRefSef):
    print("")
    print("conjunto de referecnia inicial: ")
    print("")
    mostrarLista(RefSef,True)

"""
4.  Hacer NuevaSolución = TRUE
Mientras (NuevaSolución)
"""

nuevaSolucion = True

i = 1
while(nuevaSolucion):

    """
    5.  NuevaSolucion = FALSE
    """
    nuevaSolucion = False

    """
    6.  Generar los subconjuntos de RefSet en los que
        haya al menos una nueva solución.
    """

    subSet = SubsetGenerationMethod(RefSef)

    mostarSubSet = True
    if mostarSubSet:
        print("")
        print("subconjuntos: ")
        print("")
        mostrarLista(subSet,False)

    """        
    7.  Seleccionar un subconjunto y etiquetarlo
        como examinado.           
    8.  Aplicar el método de combinación a las
        soluciones del subconjunto.
    """

    subSetCombination = SolutionCombinationMethod(subSet)

    mostarsubSetComb = True
    if mostarsubSetComb:
        print("")
        print("combinaciones de subSet: ")
        print("")
        mostrarLista(subSetCombination,True)

    """
    9.  Aplicar el método de mejora a cada
        solución obtenida por combinación. Sea
        x la solución mejorada:
        Si(f(x) < f(xb) y x no está en RefSet)
    10. Hacer xb = x y reordenar Refset
        Hacer NuevaSolucion = TRUE
    """

    subSetCombinationMejorada = ImprovementMethod(subSetCombination)

    RefSefActualizado = ReferenceSetUpdateMethod(subSetCombinationMejorada,RefSef)

    mostrarRefSef = False
    if(mostrarRefSef):
        print("")
        print("nuevo RefSet: ")
        print("")
        mostrarLista(RefSefActualizado,True)
    
    if RefSefActualizado != RefSef:
        nuevaSolucion = True
        RefSef = RefSefActualizado

mostrarRefSef = True
if(mostrarRefSef):
    print("")
    print("conjunto de referecnia inicial: ")
    print("")
    mostrarLista(RefSefOriginal,True)

mostrarRefSef = True
if(mostrarRefSef):
    print("")
    print("RefSet sin mas soluciones: ")
    print("")
    mostrarLista(RefSefActualizado,True)
