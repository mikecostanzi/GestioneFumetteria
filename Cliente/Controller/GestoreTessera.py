import pickle
import os.path

from Cliente.Model.Tessera import Tessera

class GestoreTessera(Tessera):
    def __int__(self):
        super.__init__()

    def creaTessera(self, idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti):
        self.setTessera(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti)

        tessere = {}
        if os.path.isfile('Cliente/Database/Clienti.pickle'):
            with open('Cliente/Database/Clienti.pickle', 'rt') as f:
               tessere = dict(pickle.load(f))
            tessere[idCliente] = self
            with open('Cliente/Database/Clienti.pickle', 'at') as f:
                pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)

    def infoTessera(self):
        return self.getTessera()

    def ricercaTessera(self):
        pass

    def eliminaTessera(self):
        pass