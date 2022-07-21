from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from InterfacciaCliente.OperazioneCliente import OperazioneCliente



class InterfacciaMain(QWidget):

    def __int__(self, parent):
        super(InterfacciaMain, self).__int__(parent)

        l = QGridLayout()
        l.addWidget(self.get_button("Acquisto", self.go_acquisto), 0,0)
        l.addWidget(self.get_button("Noleggio",self.go_noleggio), 0,1)
        l.addWidget(self.get_button("Cliente",self.go_cliente),0,2)
        l.addWidget(self.get_button("FumettiAcquistabili", self.go_fumettiA),1,0)
        l.addWidget(self.get_button("FumettiNoleggiabili", self.go_fumettiN), 1, 1)
        l.addWidget(self.get_button("Statistiche", self.go_statistiche), 1, 2)
        #b = QLabel()
        #b.setLayout(l)
        #b.setText("Quale operazione vuoi effettuare?")
        self.setLayout(l)
        self.resize(400,300)
        self.setWindowTitle("MAIN")



    def get_button(self,opzione,click):
        button = QPushButton(opzione)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.click.connect(click)
        pass

    def go_acquisto(self):
        pass
    def go_noleggio(self):
        pass
    def go_cliente(self):
        pass
    def go_fumettiA(self):
        pass
    def go_fumettiN(self):
        pass
    def go_statistiche(self):
        pass