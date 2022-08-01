from PyQt5 import QtWidgets
from InterfacciaFumettiAcquistabiili.InserimentoCodiceA import InserimentoCodiceA

class ModificaA(QtWidgets):

    def __int__(self,perent=None):
        inserimento = InserimentoCodiceA()
        self.codice = inserimento.inserimento_codice()
        pass
    pass
