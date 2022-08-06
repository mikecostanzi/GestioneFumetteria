import datetime
#import Tessera
from Cliente.Classi.Tessera import Tessera


class Cliente:
    def __init__(self):
        self.idCliente = -1
        self.nome = " "
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.indirizzo = ""
        self.telefono = -2
        self.email = ""

        #self.Tessera = Tessera

    def getCliente(self):
        return {
            "idCliente": self.idCliente,
            "cognome": self.cognome,
            "nome": self.nome,
            "dataNascita": self.dataNascita,
            "indirizzo": self.indirizzo,
            "telefono": self.telefono,
            "email": self.email,

            #"Tessera": self.Tessera
        }

    def setCliente(self, idCliente,nome, cognome, dataNascita,indirizzo, telefono, email): #Tessera):
        self.idCliente = idCliente
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email

        #self.Tessera = Tessera

    def rimossoCliente(self):
        self.idCliente = -1
        self.nome = " "
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.indirizzo = ""
        self.telefono = -2
        self.email = ""
