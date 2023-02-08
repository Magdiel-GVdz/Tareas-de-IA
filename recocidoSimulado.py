import numpy as np
import numpy.random as rn
import math
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

tempInicial = 10000
tempFinal = 0.001
alpha = 0.85
pasosMaximos = 100
tempActual = tempInicial
intervalo = (0,1)

def solucionAleatorea():
    a, b = intervalo
    return a + (b - a) * rn.random_sample()

def f(x):
    return x ** 2

def calcularEnergia(x):
    return f(x)

def clip(x):
    a, b = intervalo
    return max(min(x, b), a)

def perturbar(x, fraction=1):
    amplitude = (max(intervalo) - min(intervalo)) * fraction / 10
    delta = (-amplitude/2.) + amplitude * rn.random_sample()
    return clip(x + delta)

S = solucionAleatorea()
E = calcularEnergia(S)

soluciones = [S]
energias = [E]

SMejor = S
EMejor = E

print(SMejor)
print(EMejor)

for paso in range(pasosMaximos):
    
    fraction = paso / float(pasosMaximos)
    SNuevo = perturbar(S,fraction)
    ENuevo = calcularEnergia(SNuevo)
    
    print("Paso #{:>2}/{:>2} : Temperatura Actual = {:>4.3g}, Solucion = {:>4.3g}, Energia = {:>4.3g}, Nueva Solucion = {:>4.3g}, Nueva Eenergia = {:>4.3g} ...".format(paso, pasosMaximos, tempActual, S, E, SNuevo, ENuevo))
    
    dif = ENuevo - E
    if dif < 0:
        S = SNuevo
        E = ENuevo
        soluciones.append(S)
        energias.append(E)
        if E < EMejor:
            SMejor = S
            EMejor = E
    else:
        if random.uniform(0, 1) < math.exp(-dif / tempActual):
            S = SNuevo
            E = ENuevo
            
    tempActual = alpha*tempActual
    
print("Mejor Solucion {}n\
      Energia: {} ".format(SMejor,EMejor))

def verRecocido(soluciones, energias):
    plt.figure()
    plt.suptitle("Evolución de la solucion y la energia del recocido simulado")
    plt.subplot(121)
    plt.plot(soluciones, 'r')
    plt.title("Solucion")
    plt.subplot(122)
    plt.plot(energias, 'b')
    plt.title("Energia")
    plt.show()
    
verRecocido(soluciones, energias)



