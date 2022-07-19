from PyQt5 import QtCore, QtGui, QtWidgets


class InterfacciaHome(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 350)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(18, 179, 214, 255))")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 51))
        self.label.setStyleSheet(" \n"
"font: 28pt \"Cambria Math\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 171, 71))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Scegli l\'operazione per il cliente:"))
        self.pushButton.setText(_translate("Dialog", "Registra"))
