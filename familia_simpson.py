from typing import Self


class Familia_Simpson:
    def __init__(self, ser_un_meme=False):
        pass

class Abraham_Simpson:
    Familia_Simpson.__init__(True)
    def __init__(self):
        pass
    def divorciado(self, divorciado=False):
        divorciado=True
        print(f"¿Este Simpson es divorciado? {divorciado}")
    def demente(self, demente=False):
        demente=True
    def es_viejo(self, es_viejo=False):
        es_viejo=True
    def hacer_chistes_racistas(self, hacer_chistes_racistas=False):
        hacer_chistes_racistas=True
        if hacer_chistes_racistas==True:
            return "Entra un negro, un mexicano y un chino a un bar, entonces el bar tender dice: ¡LARGO DE AQUÍ!"
        else:
            pass
    def sufrir_estres_postrauma(self, estres=False):
        estres=True
    def ser_irreverente(self, irreverente=True):
        irreverente=True

class Homero_Simpson:
    Abraham_Simpson.__init_subclass__
    Abraham_Simpson.divorciado=False
    Abraham_Simpson.demente=True
    Abraham_Simpson.es_viejo=False
    Abraham_Simpson.hacer_chistes_racistas=True
    Abraham_Simpson.sufrir_estres_postrauma=False
    Abraham_Simpson.ser_irreverente=True

    def __init__(self):
        pass
    def irresponsabilidad(self, irresponsable):
        irresponsable=True
    def amor_familia(self, amor):
        amor=True
    def casado(self, estado_civil):
        estado_civil="Casado con Marge"
    def comer_donas(self, comer_dona):
        comer_dona=True
    def beber_alcohol(self, cheve):
        cheve=True
    def trabajar(self, trabajar):
        trabajar=True

class Bart_Simpson:
    Homero_Simpson.__init_subclass__

