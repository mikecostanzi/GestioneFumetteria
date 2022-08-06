import json
import os
from Cliente.Classi.Cliente import Cliente
class GestoreCliente(Cliente):

    def __int__(self):
        super().__init__()


    def creaCliente(self,idCliente, nome, cognome, dataNascita, indirizzo,telefono,email):
        self.setCliente(idCliente,nome,cognome,dataNascita,indirizzo,telefono,email,)


        clienti = []
        if os.path.isfile('DatabaseCliente/Clienti.json'):
            with open('DatabaseCliente/Clienti.json', 'r') as f:
                clienti = json.load(f)
        clienti[idCliente] = self
        print(clienti)
        with open('DatabaseCliente/Clienti.json', 'w') as f:
            json.dump(clienti,f)

    def getInfoCliente(self):
        info = self.getCliente()
        return info

    def ricercaCliente(self, nome, cognome, telefono, idCliente):
        if os.path.isfile('DatabaseCliente/Clienti.json'):
            with open('DatabaseCliente/Clienti.json', 'r') as f:
                clienti = dict(json.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome and cliente.telefono == telefono:
                        print("E' entrato qua:"+ cliente)
                        print(clienti.get(idCliente,None))
                        return cliente
                return ("Finita la ricerca")
        else:
            return print("File non trovato")


    def rimuoviCliente(self):
        if os.path.isfile('DatabaseCliente/Clienti.json'):
            with open('DatabaseCliente/Clienti.json','r') as f:
                clienti = dict(json.load(f))
                del clienti[self.idCliente]
            with open('DatabaseCliente/Clienti.json', 'w') as f:
                json.dump(clienti,f)
        self.rimossoCliente()
        del self




