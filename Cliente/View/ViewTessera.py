from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Cliente.Controller import GestoreTessera

class ViewTessera(QWidget):
    def __init__(self, tessera, elimina_callback):
        super(ViewTessera, self).__init__()
        self.elimina_callback = elimina_callback

        t = QVBoxLayout()
        nome = ""
        info = {}
        if isinstance(tessera, GestoreTessera):
            nome = f"Tessera {tessera.IdCliente}"
            info = tessera.getInfoCliente()
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        t.addWidget(label_nome)

        t.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        t.addWidget(QLabel(f"Nome: {info['nome']}"))
        t.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        t.addWidget(QLabel(f"Data nascita: {info['dataNascita']}"))
        t.addWidget(QLabel(f"Codice Fiscale: {info['codiceFiscale']}"))
        t.addWidget(QLabel(f"Email: {info['email']}"))
        t.addWidget(QLabel(f"Telefono: {info['telefono']}"))
        t.addWidget(QLabel(f"Data: {info['dataIscrizione']}"))
        t.addWidget(QLabel(f"Punti: {info['numeroPunti']}"))

        t.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_tessera_click(tessera))
        t.addWidget(btn_elimina)

        self.setLayout(t)
        self.setWindowTitle("Tessera")

    def elimina_Tessera_click(self, tessera):
        if isinstance(tessera, GestoreTessera):
            tessera.eliminaTessera()
        self.elimina_callback()
        self.close()
