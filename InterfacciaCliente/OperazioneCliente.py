from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QLayout

from GUI.InterfacciaMain import InterfacciaMain
import InserimentoCliente

class OperazioneCliente(QWidget):
    def __int__(self, parent):
        super(OperazioneCliente, self).__int__(parent)
        self.metodi = InterfacciaMain()
        l = QGridLayout()
        testo = QLabel()
        testo.setText("Scegli l'operazione per il cliente: ")
        l.addWidget(testo)
        l.addWidget(self.metodi.get_generic_button("Registra",self.go_crea()),1,0)
        l.addWidget(self.metodi.get_generic_button("Modifica",self.go_modifica()),1,1)
        l.addWidget(self.metodi.get_generic_button("Visualizza",self.go_visualizza()),2,0)
        l.addWidget(self.metodi.get_generic_button("Elimina",self.go_elimina()),2,0)
        l.addWidget()
        self.resize(500,500)
        self.setWindowTitle()


    def go_crea(self):
        self.inserimento_cliente = InserimentoCliente()
        self.inserimento_cliente.show()

    def go_modifica(self):
        pass
    def go_visualizza(self):
        pass
    def go_elimina(self):
        pass

    def go_indietro(self):
        self.indietro = InterfacciaMain()
        self.show()


