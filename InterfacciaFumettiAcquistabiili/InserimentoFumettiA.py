from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Gestione.GestoreFumettiA import GestoreFumettiA
import math as math

class InserimentoFumettiA(QWidget):
    def __init__(self, parent = None):
        super(InserimentoFumettiA, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("quantita", "Quantità")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_fumettiA)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo fumetto acquistabile")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_fumettiA(self): ##### IMPORTANTISSIMO ###### # sistemare le varie verifiche, il codice prende il primo try/exept che incontra

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == " ":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        fumettoA = GestoreFumettiA()  # modificare gestore fumetti

        try:
            collana = int(self.qlines["collana"].text())  # PER IL CODICE ID
            sotto_collana = int(self.qlines["sotto_collana"].text())
            barcodeA = int(self.qlines["barcodeA"].text())
            prezzo = float(self.qlines["prezzo"].text())
            quantita = int(self.qlines["quantita"].text())
        except:
            QMessageBox.critical(self, "Errore", 'Numero non corretto!')
            return
        categoria = self.qlines["categoria"].text()
        distributore = self.qlines["distributore"].text()
        editore = self.qlines["editore"].text()



        fumettoA.aggiungi_fumettoA(categoria, distributore, editore, collana, sotto_collana, barcodeA, prezzo,quantita)
        self.parent()
        self.close()
