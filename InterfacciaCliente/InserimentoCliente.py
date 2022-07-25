import math
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from Gestione.GestoreCliente import GestoreCliente

class InserimentoCliente(QWidget):
    def __init__(self, parent=None):
        super(InserimentoCliente, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.qlines = {}

        self.add_info_text("idCliente", "Codice")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("dataNascita", "Data Nascita")
        self.add_info_text("indirizzo", "Indirizzo di residenza")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("email", "Email")


        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_cliente)
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo cliente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_cliente(self): ##### IMPORTANTISSIMO ###### # Nicola mi ha obbligato a scrivere il commento così la prox volta controllo questo metodo
        #ti devi ricordare di inserire cose senza contestare ;)
        try:
            telefono = int(self.qlines["telefono"].text())
            if telefono == 0 or telefono < 1000000000 or telefono > 9999999999:
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci il numero correttamente',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        except:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        try:
            codice = int(self.qlines["idCliente"].text()) # PER IL CODICE ID
        except:
            QMessageBox.critical(self, 'Errore', 'Nicolaaa hai sbagliato, devi mettere un intero!!!', QMessageBox.Ok,
                                     QMessageBox.Ok)
            return

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return
        cliente = GestoreCliente()
        try:
            idCliente = self.qlines["idCliente"].text()
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            dataNascita = datetime.strptime(self.qlines["dataNascita"].text(), '%d/%m/%Y')
            indirizzo = self.qlines["indirizzo"].text()
            email = self.qlines["email"].text()


            cliente.creaCliente(idCliente, nome, cognome, dataNascita, indirizzo,telefono,email)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene i dati inseriti',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()


