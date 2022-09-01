from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Fumetto.Classi.GestoreFumettiN import GestoreFumettiN


class InserimentoFumettiN(QWidget):
    def __init__(self, parent = None):
        super(InserimentoFumettiN, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("barcodeN", "Barcode")
        self.add_info_text("categoria", "Categoria")
        self.add_info_text("distributore", "Distributore")
        self.add_info_text("editore", "Editore")
        self.add_info_text("collana", "Collana")
        self.add_info_text("sotto_collana", "Sotto collana")
        self.add_info_text("quantita", "Quantità")
        self.add_info_text("prezzo", "Prezzo")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_fumettiN)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo fumetto noleggiabile")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_fumettiN(self):
        fumettoN = GestoreFumettiN()
        try:
            collana = int(self.qlines["collana"].text())
            sotto_collana = int(self.qlines["sotto_collana"].text())
            barcodeN = int(self.qlines["barcodeN"].text())
            prezzo = int(self.qlines["prezzo"].text())
            quantita = int(self.qlines["quantita"].text())
            categoria = self.qlines["categoria"].text()
            distributore = self.qlines["distributore"].text()
            editore = self.qlines["editore"].text()

        except:
            QMessageBox.critical(self, "Errore", "Campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            fumettoN.aggiungi_fumettoN(categoria, distributore, editore, collana, sotto_collana, barcodeN, prezzo, quantita)
        except:
            QMessageBox.critical(self, "Errore", "Json", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.parent()
        self.close()
