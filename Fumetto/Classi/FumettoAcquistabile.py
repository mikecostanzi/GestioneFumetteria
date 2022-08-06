from Fumetto.Classi.Fumetto import Fumetto
class FumettoAcquistabile(Fumetto):
    def __init__(self):
        super().__init__()
        self.barcodeA = -1
        self.prezzo = -1.01
        self.quantita = 0

    def getFumettoAcquistabile(self):
        return {
            "fumetto": self.getFumetto(),
            "barcodeA": self.barcodeA,
            "prezzo": self.prezzo,
            "quantita": self.quantita
        }

    def setFumettoAcquistabile(self,categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo,quantita):
        self.setFumetto(categoria,distributore,editore,collana,sottocollana)
        self.barcodeA = barcodeA
        self.prezzo = prezzo
        self.quantita

    def rimossoFumettoA(self):
        self.rimossoFumetto()
        self.barcodeA = -2
        self.prezzo = -1.01
        self.quantita = -1
