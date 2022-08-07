from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Fumetto.Classi.GestoreFumettiA import GestoreFumettiA


class ModificaA(QWidget):
    def __init__(self, parent = None):
        super(ModificaA, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("quantita", "Quantità")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_fumettiA)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica fumetto acquistabile")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def modifica_fumettiA(self): ##### IMPORTANTISSIMO ###### # sistemare le varie verifiche, il codice prende il primo try/exept che incontra

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == " ":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        fumettoA = GestoreFumettiA()  # modificare gestore fumetti

        try:
            quantita = int(self.qlines["quantita"].text())
        except:
            QMessageBox.critical(self, "Errore", 'Numero non corretto!')
            return



        fumettoA.aggiungi_fumettoA(quantita)
        self.parent()
        self.close()
