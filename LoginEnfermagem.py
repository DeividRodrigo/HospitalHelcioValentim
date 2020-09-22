# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginEnfermagem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLoginEnfermagem(object):
    def setupUi(self, DialogLoginEnfermagem):
        DialogLoginEnfermagem.setObjectName("DialogLoginEnfermagem")
        DialogLoginEnfermagem.resize(598, 331)
        DialogLoginEnfermagem.setStyleSheet("background-color: rgb(192, 255, 218);")
        self.frameLoginRecepcao = QtWidgets.QFrame(DialogLoginEnfermagem)
        self.frameLoginRecepcao.setGeometry(QtCore.QRect(0, 0, 591, 331))
        self.frameLoginRecepcao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLoginRecepcao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLoginRecepcao.setObjectName("frameLoginRecepcao")
        self.labelLoginEnfermagem_2 = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLoginEnfermagem_2.setGeometry(QtCore.QRect(170, 221, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelLoginEnfermagem_2.setFont(font)
        self.labelLoginEnfermagem_2.setObjectName("labelLoginEnfermagem_2")
        self.lineEditEnfermagem = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditEnfermagem.setGeometry(QtCore.QRect(250, 231, 141, 21))
        self.lineEditEnfermagem.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditEnfermagem.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditEnfermagem.setObjectName("lineEditEnfermagem")
        self.labelLoginEnfermagem = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLoginEnfermagem.setGeometry(QtCore.QRect(170, 171, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelLoginEnfermagem.setFont(font)
        self.labelLoginEnfermagem.setObjectName("labelLoginEnfermagem")
        self.labelTituloEnfermagem = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelTituloEnfermagem.setGeometry(QtCore.QRect(250, 71, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(22)
        self.labelTituloEnfermagem.setFont(font)
        self.labelTituloEnfermagem.setObjectName("labelTituloEnfermagem")
        self.labelLogo = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo.setGeometry(QtCore.QRect(140, 41, 91, 81))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("logoHospital.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.lineEditLoginEnfermagem = QtWidgets.QLineEdit(self.frameLoginRecepcao)
        self.lineEditLoginEnfermagem.setGeometry(QtCore.QRect(250, 180, 141, 21))
        self.lineEditLoginEnfermagem.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEditLoginEnfermagem.setObjectName("lineEditLoginEnfermagem")
        self.labelLogo_2 = QtWidgets.QLabel(self.frameLoginRecepcao)
        self.labelLogo_2.setGeometry(QtCore.QRect(130, 60, 91, 71))
        self.labelLogo_2.setText("")
        self.labelLogo_2.setPixmap(QtGui.QPixmap("Formularios/logoHospital.png"))
        self.labelLogo_2.setObjectName("labelLogo_2")
        self.pushButtoneEntrarEnfermagem = QtWidgets.QPushButton(self.frameLoginRecepcao)
        self.pushButtoneEntrarEnfermagem.setGeometry(QtCore.QRect(290, 280, 61, 21))
        self.pushButtoneEntrarEnfermagem.setStyleSheet("background-color: rgb(57, 175, 48);\n"
"color: rgb(85, 0, 0);")
        self.pushButtoneEntrarEnfermagem.setObjectName("pushButtoneEntrarEnfermagem")

        self.retranslateUi(DialogLoginEnfermagem)
        QtCore.QMetaObject.connectSlotsByName(DialogLoginEnfermagem)

    def retranslateUi(self, DialogLoginEnfermagem):
        _translate = QtCore.QCoreApplication.translate
        DialogLoginEnfermagem.setWindowTitle(_translate("DialogLoginEnfermagem", "Login da Enfermagem"))
        self.labelLoginEnfermagem_2.setText(_translate("DialogLoginEnfermagem", "Senha:"))
        self.labelLoginEnfermagem.setText(_translate("DialogLoginEnfermagem", "Login:"))
        self.labelTituloEnfermagem.setText(_translate("DialogLoginEnfermagem", "Enfermagem"))
        self.pushButtoneEntrarEnfermagem.setText(_translate("DialogLoginEnfermagem", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogLoginEnfermagem = QtWidgets.QDialog()
    ui = Ui_DialogLoginEnfermagem()
    ui.setupUi(DialogLoginEnfermagem)
    DialogLoginEnfermagem.show()
    sys.exit(app.exec_())
