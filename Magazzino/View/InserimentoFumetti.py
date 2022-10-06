from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Magazzino.Controller.GestoreFumetti import GestoreFumetti


class InserimentoFumetti(QWidget):
    def __init__(self, parent = None):
        super(InserimentoFumetti, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("barcode", "Barcode")
        self.add_info_text("categoria", "Categoria")
        self.add_info_text("distributore", "Distributore")
        self.add_info_text("editore", "Editore")
        self.add_info_text("collana", "Collana")
        self.add_info_text("sotto_collana", "Sotto collana")
        self.add_info_text("quantita", "Quantità")
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

    def aggiungi_fumettiA(self):
        fumetto = GestoreFumetti()
        try:
            collana = int(self.qlines["collana"].text())
            print("Ciao1")
            sotto_collana = int(self.qlines["sotto_collana"].text())
            print("Ciao1")
            barcode = int(self.qlines["barcode"].text())
            print("Ciao1")
            prezzo = float(self.qlines["prezzo"].text())
            print("Ciao1")
            quantita = int(self.qlines["quantita"].text())
            print("Ciao1")
            categoria = self.qlines["categoria"].text()
            print("Ciao3")
            distributore = self.qlines["distributore"].text()
            print("Ciao2")
            editore = self.qlines["editore"].text()


        except:

            QMessageBox.critical(self, "Errore", "Errore di paramentri", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            fumetto.aggiungi_fumetto(categoria, distributore, editore, collana, sotto_collana, barcode, prezzo, quantita)
        except:
            QMessageBox.critical(self, "Errore", "Pickle", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.parent()
        self.close()
