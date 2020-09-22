# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginRecepcao.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowLoginRecepcao(object):
    def setupUi(self, MainWindowLoginRecepcao):
        MainWindowLoginRecepcao.setObjectName("MainWindowLoginRecepcao")
        MainWindowLoginRecepcao.resize(605, 337)
        MainWindowLoginRecepcao.setStyleSheet("background-color: rgb(192, 255, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindowLoginRecepcao)
        self.centralwidget.setObjectName("centralwidget")
        self.frameLoginRecepcao = QtWidgets.QFrame(self.centralwidget)
        self.frameLoginRecepcao.setGeometry(QtCore.QRect(30, 0, 591, 331))
        self.frameLoginRecepcao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLoginRecepcao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLoginRecepcao.setObjectName("frameLoginRecepcao")
        self.labelSenhaRecepcao = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelSenhaRecepcao.setGeometry(QtCore.QRect(170, 221, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSenhaRecepcao.setFont(font)
        self.labelSenhaRecepcao.setObjectName("labelSenhaRecepcao")
        self.lineEditSenhaRecepcao = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditSenhaRecepcao.setGeometry(QtCore.QRect(250, 231, 141, 21))
        self.lineEditSenhaRecepcao.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditSenhaRecepcao.setText("")
        self.lineEditSenhaRecepcao.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSenhaRecepcao.setObjectName("lineEditSenhaRecepcao")
        self.labelLoginRecepcao = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLoginRecepcao.setGeometry(QtCore.QRect(170, 171, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelLoginRecepcao.setFont(font)
        self.labelLoginRecepcao.setObjectName("labelLoginRecepcao")
        self.labelTituloRecepcao = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelTituloRecepcao.setGeometry(QtCore.QRect(250, 71, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(22)
        self.labelTituloRecepcao.setFont(font)
        self.labelTituloRecepcao.setObjectName("labelTituloRecepcao")
        self.labelLogo = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo.setGeometry(QtCore.QRect(140, 41, 91, 81))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("logoHospital.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.lineEditLoginRecepcao = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditLoginRecepcao.setGeometry(QtCore.QRect(250, 180, 141, 21))
        self.lineEditLoginRecepcao.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditLoginRecepcao.setText("")
        self.lineEditLoginRecepcao.setObjectName("lineEditLoginRecepcao")
        self.labelLogo_2 = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo_2.setGeometry(QtCore.QRect(120, 50, 91, 71))
        self.labelLogo_2.setText("")
        self.labelLogo_2.setPixmap(QtGui.QPixmap("Formularios/logoHospital.png"))
        self.labelLogo_2.setObjectName("labelLogo_2")
        self.pushButtoneEntrarRecepcao = QtWidgets.QPushButton(self.frameLoginRecepcao)
        self.pushButtoneEntrarRecepcao.setGeometry(QtCore.QRect(290, 280, 61, 21))
        self.pushButtoneEntrarRecepcao.setStyleSheet("background-color: rgb(57, 175, 48);\n"
"color: rgb(85, 0, 0);")
        self.pushButtoneEntrarRecepcao.setObjectName("pushButtoneEntrarRecepcao")
        MainWindowLoginRecepcao.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowLoginRecepcao)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLoginRecepcao)

    def retranslateUi(self, MainWindowLoginRecepcao):
        _translate = QtCore.QCoreApplication.translate
        MainWindowLoginRecepcao.setWindowTitle(_translate("MainWindowLoginRecepcao", "Login da Recepção"))
        self.labelSenhaRecepcao.setText(_translate("MainWindowLoginRecepcao", "Senha:"))
        self.labelLoginRecepcao.setText(_translate("MainWindowLoginRecepcao", "Login:"))
        self.labelTituloRecepcao.setText(_translate("MainWindowLoginRecepcao", "Recepção"))
        self.pushButtoneEntrarRecepcao.setText(_translate("MainWindowLoginRecepcao", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowLoginRecepcao = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLoginRecepcao()
    ui.setupUi(MainWindowLoginRecepcao)
    MainWindowLoginRecepcao.show()
    sys.exit(app.exec_())
