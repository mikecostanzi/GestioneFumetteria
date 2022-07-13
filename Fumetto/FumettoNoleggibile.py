import Fumetto
class FumettoNoleggiabile:
    def __init__(self):
        self.Fumetto = Fumetto
        self.idFumettoNoleggiabile = -1
        self.prezzo = -1.01

    def getFumettoNoleggibile(self):
        return {
            "Fumetto": self.Fumetto,
            "idFumettoNoleggiabile": self.idFumettoNoleggiabile,
            "prezzo": self.prezzo
        }

    def setFumettoNoleggiabile(self,Fumetto , idFumettoNoleggiabile, prezzo):
        self.Fumetto = Fumetto
        self.idFumettoNoleggiabile = idFumettoNoleggiabile
        self.prezzo = prezzo