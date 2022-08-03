from PyQt5.QtWidgets import QWidget,QLineEdit, QGridLayout, QPushButton, QSizePolicy, QLabel
import ModificaA
import EliminaA


class InserimentoCodiceA(QWidget):

    def __init__(self, parent=None):
        super(InserimentoCodiceA, self).__init__(parent)
        grid_layout = QGridLayout()
        testo_opzione = QLabel()
        testo_opzione.setText("Inserisci il Bar-Code: ")
        grid_layout.addWidget(testo_opzione, 1, 0)
        self.testo_ingresso = QLineEdit()
        grid_layout.addWidget(self.testo_ingresso, 1, 1)
        grid_layout.addWidget(self.get_generic_button("Registra", self.go_modifica), 2, 0)

        grid_layout.addWidget(self.get_generic_button("Visualizza", self.go_elimina), 2, 1)
        #grid_layout.addWidget(self.get_generic_button("Elimina/Modifica", self.go_inserimento_codice), 2, 0, 1, 2)
        #grid_layout.addWidget(self.get_generic_button("Gestisci Sistema", self.go_sistema), 2, 0, 1, 2) DA CAMBIARE

        self.setLayout(grid_layout)
        self.resize(500, 500)
        self.setWindowTitle("Inserimento Bar-Code")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button



    def go_modifica(self):
        self.modificaA = ModificaA()
        self.modificaA.show()


    def go_elimina(self):
        self.eliminaA = EliminaA()
        self.eliminaA.show()



