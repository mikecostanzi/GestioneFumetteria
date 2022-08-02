from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from InterfacciaFumettiAcquistabiili.InserimentoCodiceA import InserimentoCodiceA

class EliminaA(QWidget):
    def __init__(self,parent=None):
        super(EliminaA, self).__init__(parent)
        q = InserimentoCodiceA
        v = QGridLayout()
        b = QLabel()
        b.setText("Annichilito")
        v.addWidget(b, 1, 0)

        self.setLayout(v)
        self.resize(500, 500)
        self.setWindowTitle("Annichilito")

