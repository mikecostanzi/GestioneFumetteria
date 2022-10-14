import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#from GUI.InterfacciaCliente import InterfacciaCliente

from Main.InterfacciaMain import InterfacciaMain
from Main.Login import Login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Inizio")
    gui_main = Login()

    gui_main.show()
    sys.exit(app.exec())
