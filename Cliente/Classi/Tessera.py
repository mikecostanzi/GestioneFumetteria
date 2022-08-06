import datetime
class Tessera:
    def __init__(self):
        self.idTessera = -1
        self.dataIscrizione = datetime.datetime(year=1914, month=10, day=15)
        self.numeroPunti = -2

    def getTessera(self):
        return {
            "idTessera": self.idTessera,
            "dataIscrizione": self.dataIscrizione,
            "numeroPunti": self.numeroPunti
        }

    def setTessera(self, idTessera, dataIscrizione, numeroPunti):
        self.idTessera = idTessera
        self.dataIscrizione = dataIscrizione
        self.numeroPunti = numeroPunti

