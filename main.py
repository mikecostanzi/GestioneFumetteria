import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#from GUI.InterfacciaCliente import InterfacciaCliente

from GUI.InterfacciaMain import InterfacciaMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Inizio")
    gui_main = InterfacciaMain()

    gui_main.show()
    print("Fine")
    sys.exit(app.exec())
