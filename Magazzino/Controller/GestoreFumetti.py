import pickle
import os.path

from Magazzino.Model.Fumetto import Fumetto


class GestoreFumetti(Fumetto):
    def __init__(self):
        super(Fumetto).__init__()
        self.fumetti = []
        if os.path.isfile('../GestioneFumetteria/Magazzino/Database/Fumetti.pickle'):
            with open('../GestioneFumetteria/Magazzino/Database/Fumetti.pickle', 'rb') as f:
                self.fumetti = list(pickle.load(f))

    def save_data(self):
        with open('../GestioneFumetteria/Magazzino/Database/Fumetti.pickle', 'wb') as f:
            pickle.dump(self.fumetti, f,pickle.HIGHEST_PROTOCOL)


    def aggiungi_fumetto(self, barcode, categoria, distributore, editore, collana, sottocollana,quantita, prezzo):
        fumetto = Fumetto()
        fumetto.setFumetto(barcode, categoria, distributore, editore, collana, sottocollana, quantita, prezzo)
        self.fumetti.append(fumetto)
        self.save_data()

    def ricerca_fumetto(self,barcode):
        print('Inizio ricerca')
        for fumetto in self.fumetti:
            if barcode == fumetto.barcode:
                return fumetto
                print('Ricerca avvenuta con successo')
            return None

    def rimuovi_fumetto(self,barcode):
        for fumetto in self.fumetti:
            if barcode == fumetto.barcode:
                self.fumetti.remove(fumetto)
    def getInfoFumetto(self):
        info = self.getInfoFumetto()
        return info
