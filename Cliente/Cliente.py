import datetime
#import Tessera
class Cliente:
    def __init__(self):
        self.cognome = ""
        self.nome = ""
        self.idCliente = -1
        self.indirizzo = ""
        self.telefono = -2
        self.email = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        #self.Tessera = Tessera

    def getCliente(self):
        return {
            "cognome": self.cognome,
            "nome": self.nome,
            "idCliente": self.idCliente,
            "indirizzo": self.indirizzo,
            "telefono": self.telefono,
            "email": self.email,
            "dataNascita": self.dataNascita,
            #"Tessera": self.Tessera
        }

    def setCliente(self, nome, cognome, idCliente, indirizzo, telefono, email, dataNascita): #Tessera):
        self.nome = nome
        self.cognome = cognome
        self.idCliente = idCliente
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email
        self.dataNascita = dataNascita
        self.Tessera = Tessera
