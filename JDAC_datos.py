# JDAC_datos.py
# GDS0152 - Aguilar Cano Juan Daniel

class Datos():
    def data(self,diccionario):
        print("================================================")
        print("            Datos del diccionario               ")
        print("================================================")
        print("Nombre: " + diccionario['Nombre'])
        print("Edad: " + str(diccionario['Edad']))
        print("Teléfono: " + diccionario['Telefono'])
        print("Correo: " + diccionario['Correo'])
        print("Codigo Postal: " + str(diccionario['CodigoPostal']))
        print("================================================")
        

datos = Datos()
name=input("Ingresa tu nombre: \n")
age=int(input("Ingresa tu edad: \n"))
phone=input("Ingresa tu teléfono: \n")
email=input("Ingresa tu correo: \n")
zipcode=int(input("Ingresa tu código postal: \n"))

diccionario ={'Nombre':name,'Edad':age,'Telefono':phone,'Correo':email,'CodigoPostal':zipcode}
datos.data(diccionario)
