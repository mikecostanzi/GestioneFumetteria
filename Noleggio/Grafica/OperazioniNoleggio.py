from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton


class OperazioniNoleggio(QWidget):

    def __int__(self,parent=None):
        super(OperazioniNoleggio, self).__int__(parent)
        l = QGridLayout()
        b = QLabel("Scegli l'operazione:")
        l.addWidget(b)
        l.addWidget(self.generic_button("Inserimento Noleggio",self.get_inserimento),1,0)
        l.addWidget(self.generic_button("Restituzione Noleggio",self.get_restituzione),1,1)
        l.addWidget(self.generic_button("Ricerca Noleggio",self.get_ricerca),2,0)
        self.setLayout(l)
        self.resize(300,500)
        self.setWindowTitle("Operazioni sul Noleggio")


    def generic_button(self,titolo,click):
        button = QPushButton(titolo)
        button.clicked.connect(click)
        return button
    def get_inserimento(self):
        pass
    def get_restituzione(self):
        pass
    def get_ricerca(self):
        pass
