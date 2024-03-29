import array as arr
import datetime
import Magazzino.Model.FumettoAcquistabile
class Acquisto:
    def __init__(self):
        self.idAcquisto = -1
        self.FumettoAcquistabile = Magazzino.Classi.FumettoAcquistabile
        self.acquisti = arr.array(Magazzino.Classi.FumettoAcquistabile)
        self.dataAcquisto =datetime.datetime
        self.importo = -1.01


    def getAcquisto(self):
        return {
            "idAcquisto": self.idAcquisto,
            "Acquisti": self.acquisti,
            "dataAcquisto": self.dataAcquisto,
            "importo": self.importo
        }

    def setAcquisto(self, idAcquisto, acquisti, dataAcquisto, importo):
        self.idAcquisto = idAcquisto
        self.acquisti = acquisti
        self.dataAcquisto = dataAcquisto
        self.importo = importo
