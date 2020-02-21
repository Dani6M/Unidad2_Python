# JDAC_aleatorias.py
# GDS0152 - Juan Daniel Aguilar Cano 
import random

class ListaAleatoria():
    def generaLista(self,n):        
        aleatorios = [random.randint(0,1000) for _ in range(n)]
        print("Lista aleatoria")
        print(aleatorios)
        print(" \n")
        ordenada=sorted(aleatorios)
        print("Lista anterior ordenada \n")
        print(ordenada)
      
        

la = ListaAleatoria()
print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
la.generaLista(n)

        
    
