import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from Cliente.Controller.GestoreTessera import GestoreTessera

class InserimentoTessera(QWidget):
    def __int__(self, parent = None):
        super(InserimentoTessera, self).__init__(parent)
        
        self.t = QVBoxLayout()
        self.qLines = {}

        self.add_info_text("idCliente", "Codice")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("dataNascita", "Data Nascita")
        self.add_info_text("indirizzo", "Indirizzo di residenza")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("email", "Email")
        self.add_info_text("dataIscrizione", "Data")
        self.add_info_text("numeroPunti", "Punti")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_tessera)
        self.qlines["btn_ok"] = btn_ok
        self.t.addWidget(btn_ok)

        self.setLayout(self.t)
        self.setWindowTitle("Nuova Tessera")

    def add_info_text(self, nome, label):
        self.t.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.t.addWidget(current_text)

    def aggiungi_Tessera(self):

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
                    return

        tessera = GestoreTessera()

        idCliente = int(self.qlines["idCliente"].text())
        nome = self.qlines["nome"].text()
        cognome = self.qlines["cognome"].text()
        dataNascita = datetime.strptime(self.qlines["dataNascita"].text(), '%d/%m/%Y')
        indirizzo = self.qlines["indirizzo"].text()
        email = self.qlines["email"].text()
        telefono = self.qlines["telefono"].text()
        dataIscrizione = self.qLines["dataIscrizione"].text()
        numeroPunti = self.qLines["numeroPunti"].text()

        tessera.creaTessera(idCliente, nome, cognome, dataNascita, indirizzo, telefono, email, dataIscrizione, numeroPunti)

        self.parent()
        self.close()
