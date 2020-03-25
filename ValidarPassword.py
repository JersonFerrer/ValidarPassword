from sys import argv
import re


class ExpresionRegular():

    def __init__(self,expresion):
        self.expresion = expresion

    def validar(self):
        patron=(r'^[A-Z]{1}[0-9]{3}[a-z]{3}[\W]{3}$')#Se crea la expresion regular

        resultado = re.match(patron, self.expresion)
        if resultado is not None:
            print("es valida la expresion regular")
        else:
            print("no es valida la expresion regular")
