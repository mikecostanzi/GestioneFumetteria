from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QPushButton
from Cliente.Controller.GestoreTessera import GestoreTessera

class ViewTessera(QWidget):
    def __init__(self, tessera, elimina_callback):
        super(ViewTessera, self).__init__()
        self.elimina_callback = elimina_callback

        vt = QVBoxLayout()
        nome = ""
        info = {}

        if isinstance(tessera, GestoreTessera):
            nome = f"GestoreTessera {tessera.idCliente}"
            info = tessera.infoTessera()
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        vt.addWidget(label_nome)

        vt.addWidget(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        vt.addWidget(QLabel(f"idCliente: {info['idCliente']}"))
        vt.addWidget(QLabel(f"nome: {info['nome']}"))
        vt.addWidget(QLabel(f"cognome: {info['cognome']}"))
        vt.addWidget(QLabel(f"dataNascita: {info['dataNascita']}"))
        vt.addWidget(QLabel(f"indirizzo: {info['indirizzo']}"))
        vt.addWidget(QLabel(f"telefono: {info['telefono']}"))
        vt.addWidget(QLabel(f"email: {info['email']}"))
        vt.addWidget(QLabel(f"dataIscrizione: {info['dataIscrizione']}"))
        vt.addWidget(QLabel(f"numeroPunti: {info['numeroPunti']}"))

        vt.addWidget(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_del = QPushButton('Elimina')
        btn_del.clicked.connect(lambda: self.del_tessera_click(tessera))
        vt.addWidget(btn_del)

        self.setLayout(vt)
        self.setWindowTitle("Tessera")

    def del_tessera_click(self, tessera):
        if isinstance(tessera, GestoreTessera):
            tessera.delTessera()
        self.elimina_callback()
        self.close()