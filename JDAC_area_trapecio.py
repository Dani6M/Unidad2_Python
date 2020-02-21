# area_trapecio.py
# GDS0152 - Aguilar Cano Juan Daniel

class Trapecio():
    def __init__(self):        
        self.a:float
        self.b:float
        self.h:float        
        
    def calculo(self,a,b,h):
        rest = ((a + b)*h)/2
        print("El área del trapecio es: "+str(rest))
        
tr = Trapecio()                
a =float(input("Ingresa la base Mayor del trapecio: \n"))
b =float(input("Ingresa la base Menos del trapecio: \n"))
h =float(input("Ingresa la altura del trapecio: \n"))
tr.calculo(a,b,h)







