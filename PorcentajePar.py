""""Problema No. 1:
Del tiempo dado calcular el valor de llamada"""

print("----------------------------------------------------------------------")
print("-----------------PORCENTAJE PAR DE NÚMEROS RANDÓMICOS-----------------")
print("----------------------------------------------------------------------")

import random 
import time

#Input
n = int(input("Ingrese la cantidad de números: "))

#processing
inicioTiempo = time.time()

def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
        lista[i] = random.randint(0, 1000)  
      return lista


aleatorios = listaAleatorios(n)

finalTiempo = time.time()

tiempoEjecucion = finalTiempo - inicioTiempo

#Output

print("Lista de números randómicos: " , aleatorios)
print(tiempoEjecucion)



