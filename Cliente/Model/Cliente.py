import datetime

class Cliente:
    def __init__(self):
        self.idCliente = -1
        self.nome = " "
        self.cognome = ""
        self.dataNascita = datetime.datetime(day=1, month=1, year=1970)
        self.indirizzo = ""
        self.telefono = ""
        self.email = ""

    def getCliente(self):
        return {
            "idCliente": self.idCliente,
            "cognome": self.cognome,
            "nome": self.nome,
            "dataNascita": self.dataNascita,
            "indirizzo": self.indirizzo,
            "telefono": self.telefono,
            "email": self.email,
        }

    def setCliente(self, idCliente,nome, cognome, dataNascita,indirizzo, telefono, email):
        self.idCliente = idCliente
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email

    def rimossoCliente(self):
        self.idCliente = -1
        self.nome = " "
        self.cognome = ""
        self.dataNascita = datetime.datetime(day=1, month=1, year=1970)
        self.indirizzo = ""
        self.telefono = ""
        self.email = ""
