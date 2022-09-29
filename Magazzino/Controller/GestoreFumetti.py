import pickle
import os.path

from Magazzino.Model.Fumetto import Fumetto

class GestoreFumetti(Fumetto):
    def __init__(self):
        super(Fumetto).__init__()
        self.fumetti = []
        if os.path.isfile('Magazzino/Database/Fumetti.pickle'):
            with open('Magazzino/Database/Fumetti.pickle','r') as f:
                self.fumetti = list(pickle.load(f))

    def save_data(self):
        with open('Database/Fumetti.pickle', 'wb') as f:
            pickle.dump(self.fumetti,f,pickle.HIGHEST_PROTOCOL)
    def aggiungi_fumetto(self,categoria,distributore, editore, collana, sottocollana , barcode, prezzo, quantita):
        self.setFumetto(categoria,distributore, editore, collana, sottocollana , barcode, prezzo, quantita)
        self.fumetti.append(self.setFumetto)
        self.save_data()
    def getInfoFumetto(self):
        info = self.getInfoFumetto()
        return info
    def ricercaFumetto(self, barcode):
        for fumetto in self.fumetti:
            if fumetto.barcode == barcode:
                return fumetto
            else:
                return None
    def rimuoviFumetto(self, barcode):
        for fumetto in self.fumetti:
            if fumetto.barcode == barcode:
                self.fumetti.remove(fumetto)
        self.save_data()



