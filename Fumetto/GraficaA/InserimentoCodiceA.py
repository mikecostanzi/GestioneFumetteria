from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit,QPushButton


class InserimentoCodiceA(QWidget):

    def __int__(self,parent=None):
        super(InserimentoCodiceA, self).__int__(parent)

        grid_layout = QGridLayout()
        dato = QLabel("Digita il codice")
        self.codice = QLineEdit()
        button = QPushButton("Avvia Ricerca")
        button.clicked.connect(self.load_fumetti)
        grid_layout.addWidget(dato,0,1)
        grid_layout.addWidget(self.codice,0,2)
        grid_layout.addWidget(button,0,3)


    def load_fumetti(self):
        pass




