import Fumetto
class FumettoAcquistabile:
    def __init__(self):
        self.Fumetto = Fumetto
        self.idFumettoAcquistabile = -1
        self.prezzo = -1.01

    def getFumettoAcquistabile(self):
        return {
            "Fumetto": self.Fumetto,
            "idFumettoAcquistabile": self.idFumettoAcquistabile,
            "prezzo": self.prezzo
        }

    def setFumettoAcquistabile(self,Fumetto , idFumettoAcquistabile, prezzo):
        self.Fumetto = Fumetto
        self.idFumettoAcquistabile = idFumettoAcquistabile
        self.prezzo = prezzo

