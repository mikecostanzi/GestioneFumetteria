class Fumetto:
    def __init__(self):
        self.categoria = " "
        self.distributore = " "
        self.editore = " "
        self.collana = -1
        self.sottocollana = -2

    def getFumetto(self):
        return {
            "categoria": self.categoria,
            "distributore": self.distributore,
            "editore": self.editore,
            "collana": self.collana,
            "sottocollana": self.sottocollana
        }

    def setFumetto(self, categoria, distributore, editore, collana, sottocollana):
        self.categoria = categoria
        self.distributore = distributore
        self.editore = editore
        self.collana = collana
        self.sottocollana = sottocollana

    def rimossoFumetto(self):
        self.categoria = ""
        self.distributore = ""
        self.editore = ""
        self.collana = -1
        self.sottocollana = -2
