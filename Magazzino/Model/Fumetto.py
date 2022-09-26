class Fumetto:
    def __init__(self):
        self.categoria = " "
        self.distributore = " "
        self.editore = " "
        self.collana = -1
        self.sottocollana = -2
        self.barcode = -3
        self.prezzo = -1.01
        self.quantita = 0

    def getFumetto(self):
        return {
            "categoria": self.categoria,
            "distributore": self.distributore,
            "editore": self.editore,
            "collana": self.collana,
            "sottocollana": self.sottocollana,
            "barcode": self.barcode,
            "prezzo": self.prezzo,
            "quantita": self.quantita
        }

    def setFumetto(self, categoria, distributore, editore, collana, sottocollana,barcode, prezzo, quantita):
        self.categoria = categoria
        self.distributore = distributore
        self.editore = editore
        self.collana = collana
        self.sottocollana = sottocollana
        self.barcode = barcode
        self.prezzo = prezzo
        self.quantita = quantita

    def rimossoFumetto(self):
        self.categoria = ""
        self.distributore = ""
        self.editore = ""
        self.collana = -1
        self.sottocollana = -2
        self.barcode = -3
        self.prezzo = -1.01
        self.quantita = -1
