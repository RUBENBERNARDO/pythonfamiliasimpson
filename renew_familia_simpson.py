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
        self.chiste=True
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
        
    class Jacqueline(FAM_Simpson):
        def __init__(self, meme, laringitis, narcicismo, mal_agradecida):
            super().__init__(meme)
            self.meme=True
            self.laringitis=True
            self.narcicismo=True
            self.mal_agradecida=True
        
        def preferir_zapatos_charol(self, preferir):
            self.preferir=True
        
        def tener_iguana_gigante_mascota(self, mascota_iguana):
            self.mascota_iguana=True
        
        def preferir_no_hablar(self, no_hablar):
            self.no_hablar=True

    class Marge(Jacqueline):
        def __init__(self, meme, laringitis, narcicismo, mal_agradecida, cabello_azul, collar_rojo, maternal):
            super().__init__(meme, laringitis, narcicismo, mal_agradecida)
            self.meme=True
            self.laringitis=False
            self.narcicismo=False
            self.mal_agradecida=False
            self.preferir=False
            self.mascota_iguana=False
            self.no_hablar=True
            self.cabello_azul=True
            self.collar_rojo=True
            self.maternal=True
        
        def hacer_pastel_favorito_lisa(self, pastel_fav):
            self.pastel_fav=True
        
        def liderar_familia(self, liderar):
            self.liderar=True
        
        def preocuparse_demasiado(self, preocuparse):
            self.preocuparse=True
        
    class Lisa(Marge):
        def __init__(self, meme, laringitis, narcicismo, mal_agradecida, cabello_azul, collar_rojo, maternal, inteligencia, oido_musical, intuicion):
            super().__init__(meme, laringitis, narcicismo, mal_agradecida, cabello_azul, collar_rojo, maternal)
            self.meme=True
            self.laringitis=False
            self.narcicismo=True
            self.mal_agradecida=True
            self.preferir=False
            self.mascota_iguana=False
            self.no_hablar=True
            self.cabello_azul=False
            self.collar_rojo=False
            self.maternal=False
            self.inteligencia=True
            self.oido_musical=True
            self.intuicion=True
        
        def tocar_saxofon(self, tocar_saxo):
            tocar_saxo=True
        
        def ir_a_la_Escuela(self, ir_escuela):
            self.ir_escuela=True

        def estudiar_diario(self, estudiar):
            estudiar=True

    class Amber(Abraham):
        def __init__(self, viejo, demente, divorciado, gusto_computacion, recien_casada, vive_Las_Vegas):
            super().__init__(viejo, demente, divorciado)
            self.meme=True
            self.viejo=False
            self.demente=True
            self.divorciado=True
            self.gusto_computacion=True
            self.recien_casada=True
            self.vive_Las_Vegas=False

        def ser_mesera(self, meserear):
            self.meserear=True
        
        def fumar_en_exceso(self, fumar):
            self.fumar=True

        def hacer_sandwich_para_homer(self, sandwich):
            self.sandwich=True


print("main")