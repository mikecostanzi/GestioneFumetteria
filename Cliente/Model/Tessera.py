from datetime import datetime
from Cliente.Model.Cliente import Cliente

class Tessera(Cliente):
    def __init__(self):
        super.__init__()
        self.dataIscrizione = datetime.datetime(day=1, month=1, year=1922)
        self.numeroPunti = -2

    def getTessera(self):
        info = self.getCliente()
        info["dataIscrizione"] = self.dataIscrizione
        info["numeroPunti"] = self.numeroPunti
        return info

    def setTessera(self, idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti):
        self.setCliente(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email)
        self.dataIscrizione = dataIscrizione
        self.numeroPunti = numeroPunti

    def delTessera(self):
        self.delCliente()
        self.dataIscrizione = datetime.datetime(day=1, month=1, year=1922)
        self.numeroPunti = -2