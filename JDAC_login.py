# JDAC_login.py
# GDS0152 - Aguilar Cano Juan Daniel

class Login():
    def __init__(self):
        self.usuario="utng"
        self.contrasena="mexico"
                    
    def validar(self,usuario,contrasena):
        if self.usuario == usuario and self.contrasena == contrasena:
            print("¡Bienvenido!")
        else:
            print("Usuario o contraseña, incorrecto")
            
log = Login()
usuario=input("Ingresa tu usuario: \n")
contrasena=input("Ingresa tu contraeña: \n")
log.validar(usuario,contrasena)
    
