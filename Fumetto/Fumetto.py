class Fumetto:
    def __init__(self):
        self.categoria = ""
        self.distributore = ""
        self.editore = ""
        self.barcode = ""
        self.collana = -1
        self.sottocollana = -2

    def getFumetto(self):
        return {
            "categoria": self.categoria,
            "distributore": self.distributore,
            "editore": self.editore,
            "barcode": self.barcode,
            "collana": self.collana,
            "sottocollana": self.sottocollana
        }

    def setFumetto(self, categoria, distributore, editore, barcode, collana, sottocollana):
        self.categoria = categoria
        self.distributore = distributore
        self.editore = editore
        self.barcode = barcode
        self.collana = collana
        self.sottocollana = sottocollana

