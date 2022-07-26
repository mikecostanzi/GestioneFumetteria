import Fumetto

class FumettoNoleggiabile:
    def __init__(self):
        self.fumetto = Fumetto()
        self.barcodeN = -1
        self.prezzo = -1.01

    def getFumettoNoleggibile(self):
        return {
            "fumetto": self.fumetto.getFumetto(),
            "barcodeN": self.barcodeN,
            "prezzo": self.prezzo
        }

    def setFumettoNoleggiabile(self,categoria,distributore, editore, collana, sottocollana , barcodeN, prezzo):
        self.fumetto.setFumetto(self,categoria,distributore, editore, collana, sottocollana)
        self.barcodeN = barcodeN
        self.prezzo = prezzo

    def rimossoFumettoN(self):
        self.fumetto.rimossoFumetto()
        self.barcodeN = -1
        self.prezzo = -1.01