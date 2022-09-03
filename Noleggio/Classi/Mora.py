import datetime


class Mora:
    def __init__(self):
        self.idMora = -1
        self.importoMora = -1.01
        self.dataEmissione =datetime.datetime
        self.motivazione = ""

    def getMora(self):
        return {
            "idMora": self.idMora,
            "importoMora": self.importoMora,
            "dataEmissione": self.dataEmissione,
            "motivazione": self.motivazione
        }

    def setMora(self, idMora, importoMora, dataEmissione, motivazione):
        self.idMora = idMora
        self.importoMora = importoMora
        self.dataEmissione = dataEmissione
        self.motivazione = motivazione


