import Fumetto
class FumettoAcquistabile:
    def __init__(self):
        self.fumetto = Fumetto()
        self.barcodeA = -1
        self.prezzo = -1.01

    def getFumettoAcquistabile(self):
        return {
            "fumetto": self.fumetto.getFumetto(),
            "barcodeA": self.barcodeA,
            "prezzo": self.prezzo
        }

    def setFumettoAcquistabile(self,categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo):
        self.fumetto.setFumetto(categoria,distributore,editore,collana,sottocollana)
        self.barcodeA = barcodeA
        self.prezzo = prezzo

    def rimossoFumettoA(self):
        self.fumetto.rimossoFumetto()
        self.barcodeA = -1
        self.prezzo = -1.01

