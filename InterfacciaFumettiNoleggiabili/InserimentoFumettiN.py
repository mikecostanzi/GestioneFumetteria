from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Fumetto.Fumetto import Fumetto
from Gestione.GestoreFumettiN import GestoreFumettiN

class InserimentoFumettiN(QWidget):
    def __init__(self, parent=None):
        super(InserimentoFumettiN, self).__init__(parent)
        self.v_layout = QVBoxLayout
        self.qlines = {}

        self.add_info_text("idFumetto", "Fumetto")
        self.add_info_text("categoria", "Categoria")
        self.add_info_text("distributore", "Distributore")
        self.add_info_text("editore", "Editore")
        self.add_info_text("collana", "Coollana")
        self.add_info_text("sotto_collana", "Sotto collana")
        self.add_info_text("barcode", "Barcode")
        self.add_info_text("prezzo", "Prezzo")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_fumettoN)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_fumettoN(self):

        fumettoN = GestoreFumettiN()
        try:
            barcodeN = int(self.qlines["barcodeN"].text())# PER IL CODICE ID
            collana = int(self.qlines["collana"].text())
            sottocollana = int(self.qlines["sottocollana"].text())
            prezzo = float(self.qlines["prezzo"].text())
        except:
            QMessageBox.critical(self, 'Errore', 'Nicolaaa hai sbagliato, devi mettere un numero!!!',
                                    QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        for value in self.qlines.values():
             if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        try:
            categoria = self.qlines["categoria"].text()
            distributore = self.qlines["cognome"].text()

            editore = self.qlines["indirizzo"].text()
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        fumettoN.aggiungi_fumettoN(categoria,distributore, editore, collana, sottocollana , barcodeN, prezzo)
        self.parent()
        self.close()



