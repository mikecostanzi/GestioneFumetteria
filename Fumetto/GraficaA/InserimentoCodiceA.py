from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit,QPushButton


class InserimentoCodiceA(QWidget):

    def __int__(self,parent=None):
        super(InserimentoCodiceA, self).__int__(parent)

        self.grid_layout = QGridLayout()
        self.dato = QLabel("Digita il codice")
        self.codice = QLineEdit()
        self.button = QPushButton("Avvia Ricerca")
        self.button.clicked.connect(self.load_fumetti)
        self.grid_layout.addWidget(self.dato, 0, 1)
        self.grid_layout.addWidget(self.codice,0,2)
        self.grid_layout.addWidget(self.button,0,3)
        self.setLayout(self.grid_layout)
        self.resize(500,500)
        self.setWindowTitle("Elimina/Modifica")


    def load_fumetti(self):
        pass