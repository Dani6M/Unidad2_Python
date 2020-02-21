# JDAC_usuario.py
import operator

class Estructura():            
      def datos(self,usuarios,contras):         
          resul1 = sorted(usuarios)
          resul2 = sorted(contras)
          resul1.sort()
          resul2.sort()
          print("Los usuarios de forma ascendente son:")
          print(resul1)
          print("Las contraseña de forma ascendente son:")
          print(resul2)                                                    
            
est = Estructura()
us1=input("Ingresa el usuario 1: ")
pas1=input("Ingresa la contraseña1: ")
us2=input("Ingresa el usuario 2: ")
pas2=input("Ingresa la contraseña2: ")
us3=input("Ingresa el usuario 3: ")
pas3=input("Ingresa la contraseña3: ")
us4=input("Ingresa el usuario 4: ")
pas4=input("Ingresa la contraseña4: ")
us5=input("Ingresa el usuario 5: ")
pas5=input("Ingresa la contraseña5: ")
usuarios=[us1,us2,us3,us4,us5]
contras=[pas1,pas2,pas3,pas4,pas5]
est.datos(usuarios,contras)




            
            


        
