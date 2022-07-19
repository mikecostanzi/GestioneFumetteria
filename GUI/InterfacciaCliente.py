from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from Gestione.GestoreCliente import GestoreCliente


class InterfacciaCliente(QWidget):
    def __init__(self, cliente):
        super(InterfacciaCliente,self).__init__()

        v_layout = QVBoxLayout()

        info = {}
        if isinstance(cliente,GestoreCliente):
            nome = f"Cliente{cliente.idCliente}"
            info = cliente.creaCliente()
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"id: {info['idCliente']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['dataNascita']}"))
        #v_layout.addWidget(QLabel(f"Codice Fiscale: {info['codiceFiscale']}"))
        #v_layout.addWidget(QLabel(f"Email: {info['email']}"))
        #v_layout.addWidget(QLabel(f"Telefonoo: {info['telefono']}"))

        self.setLayout(v_layout)
        self.setWindowTitle("Cliente")
