from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QLayout

from InterfacciaCliente.OperazioneCliente import OperazioneCliente


class InterfacciaMain(QWidget):

    def __init__(self, parent=None):
        super(InterfacciaMain, self).__init__(parent)
        l = QGridLayout()

        b = QLabel()
        b.setText("Scegli l'operazione:")
        l.addWidget(b)
        l.addWidget(self.get_generic_button("Acquisto", self.go_acquisto), 1, 0)
        l.addWidget(self.get_generic_button("Noleggioi", self.go_noleggio), 1, 1)
        l.addWidget(self.get_generic_button("Cliente", self.go_clienti), 1, 2)
        l.addWidget(self.get_generic_button("Fumetti Acquistabili", self.go_fumettiA), 2, 0)
        l.addWidget(self.get_generic_button("Fumetti Noleggiabili", self.go_fumettiN), 2, 1)
        l.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 2,2)

        self.setLayout(l)
        self.resize(500, 500)
        self.setWindowTitle("Main")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_acquisto(self):
        pass

    def go_clienti(self):
        self.vista_gestisci_clienti = OperazioneCliente
        self.vista_gestisci_clienti.show()

    def go_noleggio(self):
        pass

    def go_fumettiA(self):
        pass

    def go_fumettiN(self):
        pass

    def go_statistiche(self):
        pass