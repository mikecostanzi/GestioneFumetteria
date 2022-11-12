from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from Magazzino.Controller.GestoreFumetti import GestoreFumetti
from Magazzino.Model.Fumetto import Fumetto


class VistaFumetto(QWidget):
    def __int__(self, fumetto, call_back):
        super(VistaFumetto, self).__int__()
        self.call_back=call_back
        print('--- Inizio layout vista fumetto ---')
        v_layout = QVBoxLayout()

        barcode = f"Fumetto {fumetto.barcode}"
        label_barcode = QLabel(barcode)
        font_barcode = label_barcode.font()
        font_barcode.setPointSize(30)
        label_barcode.setFont(font_barcode)
        v_layout.addWidget(label_barcode)

        v_layout.addItem(QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Categoria: {fumetto.categoria}"))
        v_layout.addWidget(QLabel(f"Distributore: {fumetto.distributore}"))
        v_layout.addWidget(QLabel(f"Editore: {fumetto.editore}"))
        v_layout.addWidget(QLabel(f"Collana: {fumetto.collana}"))
        v_layout.addWidget(QLabel(f"Sottocollana: {fumetto.sottocollana}"))
        v_layout.addWidget(QLabel(f"Quantità: {fumetto.quantita}"))
        v_layout.addWidget(QLabel(f"Prezzo: {fumetto.prezzo}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        b_modifica = QPushButton("Modifica")
        b_modifica.clicked.connect(lambda : self.modifica(fumetto))
        v_layout.addWidget(b_modifica)

        b_elimina = QPushButton("Elimina")
        b_elimina.clicked.connect(lambda : self.elimina(fumetto))
        v_layout.addWidget(b_elimina)
        print('--- Fine layout vista fumetto ---')
        self.setLayout(v_layout)
        self.setWindowTitle("Fumetto")


    def modifica(self,fumetto):

        pass
    def elimina(self,fumetto):
        pass