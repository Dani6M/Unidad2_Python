# JDAC_par_impar.py
# GDS0152- Juan Daniel Aguilar Cano

class Numero():
    def div(self,num):
        if num % 2 ==0:
            print("El número "+str(num)+ " es par.")    
        if num % 2 !=0:
            print("El número "+str(num)+ " es impar.")

            
numero = Numero()
num = int(input("Ingresa un número entero: \n"))
numero.div(num)
resp = input("¿Quieres ingresar otro número Si/No?")
if  resp == "SI" or resp == "Si" or resp == "si" or resp == "sI":
    numero = Numero()
    num = int(input("Ingresa un número entero: \n"))
    numero.div(num)
    resp = input("¿Quieres ingresar otro número Si/No?")
    
    


