from PyQt5.QtWidgets import QWidget
from Magazzino.Controller.GestoreFumetti import GestoreFumetti

class VistaFumetto(QWidget):
    def __int__(self,fumetto,elimina_callback):
        super(VistaFumetto, self).__int__()
        self.elimina_callback = elimina_callback
