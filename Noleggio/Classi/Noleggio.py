import array as arr
from Cliente.Classi.Cliente import Cliente
import datetime
from Fumetto.Classi.FumettoNoleggibile import FumettoNoleggiabile
class Noleggio:
    def __init__(self):
        self.idNoleggio = -1
        self.FumettoNoleggiabile = FumettoNoleggiabile()
        self.dataInizioNoleggio = datetime.datetime
        self.dataRestituzione = self.dataInizioNoleggio
        self.mora = False

    def getNoleggio(self):
        return {
            "idNoleggio": self.idNoleggio,
            "fumetto": self.FumettoNoleggiabile,
            "dataInizioNoleggio": self.dataInizioNoleggio,
            "dataRestituzione": self.dataRestituzione,
            "mora": self.Mora
        }

    def setNoleggio(self, idNoleggio, noleggi, dataInizioNoleggio, dataRestituzione, Mora):
        self.idNoleggio = idNoleggio
        self.noleggi = noleggi
        self.dataInizioNoleggio = dataInizioNoleggio
        self.dataRestituzione = dataRestituzione
        self.Mora = Mora
