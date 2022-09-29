import os.path
import pickle

from Cliente.Model.Tessera import Tessera

class GestoreTessera(Tessera):

    def __int__(self):
        super.__init__()

    def creaTessera(self, idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti):
        self.setTessera(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti)
        tessere = {}
        if os.path.isfile('Cliente/Database/Clienti.pickle'):
            with open('Cliente/Database/Clienti.pickle', 'rb') as f:
                tessere = pickle.load(f)
            tessere[idCliente] = self
            with open('Cliente/Database/Clienti.pickle', 'wb') as f:
                pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)

    def infoTessera(self):
        return self.getTessera()

    def ricercaTessera(self):
        if os.path.isfile('Cliente/Database/Clienti.pickle'):
            with open('Cliente/Database/Clienti.pickle', 'rb') as f:
                tessere = dict(pickle.load(f))
                # capire cosa s'intende per "for cliente in clienti.values():"
                pass

    def eliminaTessera(self):
        if os.path.isfile('Cliente/Database/Clienti.pickle'):
            with open('Clietne/Database/Clienti.pickle', 'rb') as f:
                tessere = dict(pickle.load(f))
                del tessere[self.idCliente]
            with open('Cliente/Database/Clienti.pickle', 'wb') as f:
                pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)
            self.delTessera()
            del self