""""Problema No. 2:
Analisis del promedio, mejor y peor caso"""

print("----------------------------------------------------------------------")
print("------------------------- ANALISIS PROMEDIO --------------------------")
print("----------------------------------------------------------------------")

import random 
import time

#Input
vector = []

#processing
inicioTiempo = time.time()

for i in range(800):
    vector.append(random.randint(1, 400))
for i in range(800):
    vector.append(random.randint(401, 800))
for i in range(800):
    vector.append(random.randint(801, 1200))
for i in range(800):
    vector.append(random.randint(1201, 1600))
for i in range(800):
    vector.append(random.randint(1601, 2000))

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
ord_burbuja(vector)

#Output
print("Lista de números randómicos ordenados: ", vector)

finalTiempo = time.time()

tiempoEjecucion = finalTiempo - inicioTiempo
print(f"El programa se tardó: {tiempoEjecucion:.4f}")