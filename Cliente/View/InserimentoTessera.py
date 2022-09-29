from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

from Cliente.Controller.GestoreTessera import GestoreTessera

class InserimentoTessera(QWidget):

    def __init__(self, callback):
        super(InserimentoTessera, self).__init__()
        self.callback = callback
        self.it = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("idCliente", "ID")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("dataNascita", "Data di nascita")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("email", "Email")
        self.add_info_text("dataIscrizione", "Data iscrizione")
        self.add_info_text("numeroPunti", "Numero punti")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungiTessera)
        self.qlines["btn_ok"] = btn_ok
        self.it.addWidget(btn_ok)

        self.setLayout(self.it)
        self.setWindowTitle("Nuova Tessera")

    def add_info_text(self, nome, label):
        self.it.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.it.addWidget(current_text)

    def aggiungiTessera(self):

        idCliente = int(self.qlines["idCliente"].text())

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, "Errore", "Alcuni campi sembrano vuoti", QMessageBox.Ok, QMessageBox.Ok)
                    return

        tessera = GestoreTessera
        try:
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            dataNascita = datetime.strptime(self.qlines["dataNascita"].text())
            indirizzo = self.qlines["indirizzo"].text()
            telefono = self.qlines["telefono"].text()
            email = self.qlines["email"].text()
            dataIscrizione = datetime.strptime(self.qlines["dataIscrizione"].text())
            numeroPunti = int(self.qlines["numeroPunti"].text())
        except:
            QMessageBox.critical(self, "Errore", "Alcuni campi sembrano errati", QMessageBox.Ok, QMessageBox.Ok)
            return

        tessera.creaTessera(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti)

        self.callback()
        self.close()