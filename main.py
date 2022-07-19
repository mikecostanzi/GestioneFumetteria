import sys

from PyQt5.QtWidgets import QApplication

from GUI.InterfacciaCliente import InterfacciaCliente

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui_cliente = InterfacciaCliente()
    gui_cliente.show()
    sys.exit(app.exec())
