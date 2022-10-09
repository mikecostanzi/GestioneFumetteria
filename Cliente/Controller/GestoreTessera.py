import os.path
import pickle

from Cliente.Model.Tessera import Tessera

class GestoreTessera(Tessera):

    def __int__(self):
        super(Tessera).__init__()
        self.tessere = []

    def creaTessera(self, idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti):
        self.setTessera(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti)

        if os.path.isfile(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl'):
            with open(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl', 'rb') as f:
                self.tessere = pickle.load(f)
                print("Gestore tessera--> r fatto")

        with open(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl', 'wb') as f:
            pickle.dump(self.tessere, f, pickle.HIGHEST_PROTOCOL)
            print("Gestore tessera--> w fatto")
        print("tessera creata")

    def infoTessera(self):
        return self.getTessera()

    def ricercaTessera(self, idCliente):
        if os.path.isfile(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl'):
            with open(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl', 'rb') as f:
                tessere = dict(pickle.load(f))
                for tessera in tessere.values():
                    if tessera.idCliente == idCliente:
                        return tessera
                return None
        else:
            return None

    def eliminaTessera(self):
        if os.path.isfile(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl'):
            with open(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl', 'rb') as f:
                tessere = dict(pickle.load(f))
                del tessere[self.idCliente]
            with open(os.getcwd()+'\\..\\Cliente\\Database\\Clienti.pkl', 'wb') as f:
                pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)
            self.delTessera()
            del self