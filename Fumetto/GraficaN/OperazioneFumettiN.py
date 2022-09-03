from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel

from Fumetto.GraficaN.InserimentoFumettiN import InserimentoFumettiN

class OperazioneFumettiN(QWidget):

    def __init__(self, parent=None):
        super(OperazioneFumettiN, self).__init__(parent)
        grid_layout = QGridLayout()
        testo_opzione = QLabel()
        testo_opzione.setText("Scegli l'operazione per il fumetto noleggiabile: ")
        grid_layout.addWidget(testo_opzione)
        grid_layout.addWidget(self.get_generic_button("Registra", self.go_crea), 1, 0)

        grid_layout.addWidget(self.get_generic_button("Visualizza", self.go_visualizza), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Elimina/Modifica", self.go_inserimento_codice), 2, 0, 1, 2)
        #grid_layout.addWidget(self.get_generic_button("Gestisci Sistema", self.go_sistema), 2, 0, 1, 2) DA CAMBIARE

        self.setLayout(grid_layout)
        self.resize(500, 500)
        self.setWindowTitle("Fumetti Noleggia")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_inserimento_codice(self):
        pass
        #self.inserimento_codiceA = InserimentoCodiceA()
        #print("Nicola")
        #self.inserimento_codiceA.show()

    def go_crea(self):
        self.inserimento_fumettiN = InserimentoFumettiN()
        self.inserimento_fumettiN.show()

    def go_visualizza(self):
        pass

    def go_elimina(self):
        pass
