import pickle
import os.path

from Magazzino.Model.Fumetto import Fumetto


class GestoreFumetti(Fumetto):
    def __init__(self):
        super(Fumetto).__init__()
        self.fumetti = []
        if os.path.isfile('/home/mike/Scrivania/GestioneFumetteria/Magazzino/Database/Fumetti.pickle'):
            with open('/home/mike/Scrivania/GestioneFumetteria/Magazzino/Database/Fumetti.pickle', 'rb') as f:
                self.fumetti = list(pickle.load(f))
    def save_data(self):
        with open('/home/mike/Scrivania/GestioneFumetteria/Magazzino/Database/Fumetti.pickle', 'wb') as f:
            pickle.dump(self.fumetti, f,pickle.HIGHEST_PROTOCOL)


    def aggiungi_fumetto(self, barcode, categoria, distributore, editore, collana, sottocollana,quantita, prezzo):
        self.setFumetto(barcode, categoria, distributore, editore, collana, sottocollana, quantita, prezzo)
        self.fumetti.append(self.setFumetto)
        self.save_data()

    def getInfoFumetto(self):
        info = self.getInfoFumetto()
        return info
