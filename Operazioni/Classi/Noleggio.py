import array as arr
import datetime
import Mora
import Fumetto
class Noleggio:
    def __init__(self):
        self.idNoleggio = -1
        self.FumettoNoleggiabile = Fumetto.Classi.FumettoNoleggibile
        self.noleggi = arr.array(Fumetto.Classi.FumettoNoleggibile)
        self.dataInizioNoleggio = datetime.datetime
        self.dataRestituzione = datetime.datetime
        self.Mora = Mora

    def getNoleggio(self):
        return {
            "idNoleggio": self.idNoleggio,
            "noleggi": self.noleggi,
            "dataInizioNoleggio": self.dataInizioNoleggio,
            "dataRestituzione": self.dataRestituzione,
            "Mora": self.Mora
        }

    def setNoleggio(self, idNoleggio, noleggi, dataInizioNoleggio, dataRestituzione, Mora):
        self.idNoleggio = idNoleggio
        self.noleggi = noleggi
        self.dataInizioNoleggio = dataInizioNoleggio
        self.dataRestituzione = dataRestituzione
        self.Mora = Mora
