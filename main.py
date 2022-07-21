import sys

from PyQt5.QtWidgets import QApplication

#from GUI.InterfacciaCliente import InterfacciaCliente

from GUI.InterfacciaMain import InterfacciaMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui_main = InterfacciaMain()
    gui_main.show()
    sys.exit(app.exec())
