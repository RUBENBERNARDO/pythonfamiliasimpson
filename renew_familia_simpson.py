class FAM_Simpson:
    
    def __init__(self, meme):
        self.meme=True

class Abraham(FAM_Simpson):

    def __init__(self, viejo, demente, divorciado):
        self.meme=True
        self.viejo=True
        self.demente=True
        self.divorciado=True

    def hacer_chiste_racista(self, racista):
        self.racista=True
        if racista==True:
            print("Entra un negro, un mexicano y un chino a un bar, entonces el cantinero dice: ¡LARGO DE AQUÍ!")
        else:
            print("")

    def sufrir_estres_postrauma(self, estres):
        self.estres=True

    def ser_irreverente(self, irreverencia):
        self.irreverencia=True

class Homer(Abraham):

    def __init__(self, viejo, demente, divorciado, irresponsabilidad, amor_familia, casado):
        super().__init__(viejo, demente, divorciado)
        self.viejo=False
        self.demente=True
        self.divorciado=False
        self.racista=False
        self.estres=False
        self.irreverencia=True
        self.irresponsabilidad=True
        self.amor_familia=True
        self.casado=True
    
    def comer_donas(self, comer_dona):
        self.comer_dona=True
    
    def beber_alcohol(self, tomar_cheve):
        self.tomar_cheve=True

    def estar_casado(self, casado):
        self.casado=True
    
class Bart(Homer):
    def __init__(self, viejo, demente, divorciado, irresponsabilidad, amor_familia, casado, inmadurez, rebeldia, intuicion):
        super().__init__(viejo, demente, divorciado, irresponsabilidad, amor_familia, casado)
        self.viejo=False
        self.demente=True
        self.divorciado=False
        self.irresponsabilidad=True
        self.amor_familia=True
        self.casado=False
        self.inmadurez=True
        self.rebeldia=True
        self.intuicion=True

    def skating(self, skate):
        self.skate=True
        if skate==True:
            print("Este Simpson patina")
        else:
            print("")
    
    def inventar_chiste(self, chiste):
        chiste=True
        if chiste==True:
            print("the game")
        else: 
            print("")
    
    def mentir(self, mentira):
        self.mentira=True
        if mentira==True:
            print("La clase del master cheno se entiende a la perfección")
        else:
            print("")       