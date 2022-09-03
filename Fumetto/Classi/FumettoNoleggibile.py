from Fumetto.Classi.Fumetto import Fumetto

class FumettoNoleggiabile(Fumetto):
    def __init__(self):
        super().__init__()
        self.barcodeN = -1
        self.prezzo = -1.01
        self.quantita = -2

    def getFumettoNoleggibile(self):
        return {
            "fumetto": self.getFumetto(),
            "barcodeN": self.barcodeN,
            "prezzo": self.prezzo,
            "quantita": self.quantita
        }

    def setFumettoNoleggiabile(self, categoria,distributore, editore, collana, sottocollana , barcodeN, prezzo, quantita):
        self.setFumetto(self, categoria,distributore, editore, collana, sottocollana)
        self.barcodeN = barcodeN
        self.prezzo = prezzo
        self.quantita = quantita

    def rimossoFumettoN(self):
        self.rimossoFumetto()
        self.barcodeN = -1
        self.prezzo = -1.01
        self.quantita = -2