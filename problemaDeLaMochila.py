import random
from collections import namedtuple
import numpy as np 

Comida = namedtuple('Comida', ['nombre', 'peso', 'calorias'])

productos = [
    Comida('Papas', 300, 400),
    Comida('Chocolate', 100, 450),
    Comida('Pan', 50, 500),
    Comida('Manzana', 80, 50),
    Comida('Pay', 70, 80),
    Comida('Naranja', 60, 100),
    Comida('Refresco', 150, 500),
    Comida('Dulces', 100, 600),
]

pesoLimite = 1300
caloriasMinimas = 800
poblacionTotal = 20
  
#creacion de la primera generacion
poblacionDeIndividuos = np.random.randint(2, size=(poblacionTotal, 8)) 

for i in poblacionDeIndividuos:
    print(i)




