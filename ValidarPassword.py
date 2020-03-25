import re

#Creando la clase que contiene el metodo de validacion
class ExpresionRegular():

    def __init__(self,expresion):
        self.expresion = expresion

    #Metodo que valida la contraseña
    def validar(self):
        #Se crea la expresion regular
        patron=(r'^[A-Z]{1}[0-9]{3}[a-z]{3}[\W]{3}$')

        resultado = re.match(patron, self.expresion)
        if resultado is not None:
            print("es valida la expresion regular")
        else:
            print("no es valida la expresion regular")

#Pidiendo la contraseña
expresion = input("Ingrese la contraseña: ")
print(expresion)

expresionregular = ExpresionRegular(expresion)
expresionregular.validar()