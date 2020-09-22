# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMedico.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 336)
        MainWindow.setStyleSheet("background-color: rgb(192, 255, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameLoginRecepcao = QtWidgets.QFrame(self.centralwidget)
        self.frameLoginRecepcao.setGeometry(QtCore.QRect(0, 0, 591, 331))
        self.frameLoginRecepcao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLoginRecepcao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLoginRecepcao.setObjectName("frameLoginRecepcao")
        self.labelSenhaMedico = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelSenhaMedico.setGeometry(QtCore.QRect(170, 221, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSenhaMedico.setFont(font)
        self.labelSenhaMedico.setObjectName("labelSenhaMedico")
        self.lineEditSenhaMedico = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditSenhaMedico.setGeometry(QtCore.QRect(250, 231, 141, 21))
        self.lineEditSenhaMedico.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditSenhaMedico.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSenhaMedico.setObjectName("lineEditSenhaMedico")
        self.labelLoginMedico = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLoginMedico.setGeometry(QtCore.QRect(170, 171, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelLoginMedico.setFont(font)
        self.labelLoginMedico.setObjectName("labelLoginMedico")
        self.labelTituloMedico = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelTituloMedico.setGeometry(QtCore.QRect(250, 71, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(22)
        self.labelTituloMedico.setFont(font)
        self.labelTituloMedico.setObjectName("labelTituloMedico")
        self.labelLogo = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo.setGeometry(QtCore.QRect(140, 41, 91, 81))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("logoHospital.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.lineEditLoginMedico = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditLoginMedico.setGeometry(QtCore.QRect(250, 180, 141, 21))
        self.lineEditLoginMedico.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditLoginMedico.setObjectName("lineEditLoginMedico")
        self.labelLogo_2 = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo_2.setGeometry(QtCore.QRect(140, 60, 91, 71))
        self.labelLogo_2.setText("")
        self.labelLogo_2.setPixmap(QtGui.QPixmap("Formularios/logoHospital.png"))
        self.labelLogo_2.setObjectName("labelLogo_2")
        self.pushButtoneEntrarMedico = QtWidgets.QPushButton(self.frameLoginRecepcao)
        self.pushButtoneEntrarMedico.setGeometry(QtCore.QRect(290, 280, 61, 21))
        self.pushButtoneEntrarMedico.setStyleSheet("background-color: rgb(57, 175, 48);\n"
"color: rgb(85, 0, 0);")
        self.pushButtoneEntrarMedico.setObjectName("pushButtoneEntrarMedico")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSenhaMedico.setText(_translate("MainWindow", "Senha:"))
        self.labelLoginMedico.setText(_translate("MainWindow", "Login:"))
        self.labelTituloMedico.setText(_translate("MainWindow", "Medico"))
        self.pushButtoneEntrarMedico.setText(_translate("MainWindow", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
