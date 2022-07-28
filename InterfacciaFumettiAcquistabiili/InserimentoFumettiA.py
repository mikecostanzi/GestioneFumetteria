from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Gestione.GestoreFumettiA import GestoreFumettiA
import math as math


class InserimentoFumettiA(QWidget):
    def __init__(self, parent=None):
        super(InserimentoFumettiA, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("categoria", "Categoria")
        self.add_info_text("distributore", "Distributore")
        self.add_info_text("editore", "Editore")
        self.add_info_text("collana", "Collana")
        self.add_info_text("sotto_collana", "Sotto collana")
        self.add_info_text("barcodeA", "Bar-code")
        self.add_info_text("prezzo", "Prezzo")

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

    def aggiungi_fumettiA(self): ###IMPORTANTE### Credo che il problema e' dell'inserimento del Barcode
                                                # il for funziona, il primo try/except anche, il secondo si inceppa

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
                    return

        fumettoA = GestoreFumettiA()

        try:
            collana = int(self.qlines["collana"].text())
            sotto_collana = int(self.qlines["sotto_collana"].text())
            prezzo = float(self.qlines["prezzo"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci un valore corretto (Collana, Sottocollana, Prezzo)', QMessageBox.Ok, QMessageBox.Ok)
            return



        try:
            categoria = str(self.qlines["categoria"].text())
            distributore = str(self.qlines["distributore"].text())
            editore = str(self.qlines["editore"].text())
            barcodeA = int(self.qlines["barcode"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci un nome corretto (Categoria, Distributore, Editore, Barcode)', QMessageBox.Ok, QMessageBox.Ok)
            return

        fumettoA.aggiungi_fumettoA(categoria, distributore, editore, collana, sotto_collana, barcodeA, prezzo)

        self.parent()
        self.close()
