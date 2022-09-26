import datetime
from Cliente.Model.Cliente import Cliente

class Tessera(Cliente):
    def __init__(self):
        super.__init__()
        self.dataIscrizione = datetime.datetime(day=15, month=10, year=1970)
        self.numeroPunti = -1

    def getTessera(self):
        return {
            "dataIscrizione": self.dataIscrizione,
            "numeroPunti": self.numeroPunti
        }

    def setTessera(self, idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti):
        self.setCliente(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email)
        self.dataIscrizione = dataIscrizione
        self.numeroPunti = numeroPunti

