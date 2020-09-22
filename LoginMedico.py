# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMedico.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLoginMedico(object):
    def setupUi(self, DialogLoginMedico):
        DialogLoginMedico.setObjectName("DialogLoginMedico")
        DialogLoginMedico.resize(594, 334)
        DialogLoginMedico.setStyleSheet("background-color: rgb(192, 255, 218);")
        self.frameLoginRecepcao = QtWidgets.QFrame(DialogLoginMedico)
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

        self.retranslateUi(DialogLoginMedico)
        QtCore.QMetaObject.connectSlotsByName(DialogLoginMedico)

    def retranslateUi(self, DialogLoginMedico):
        _translate = QtCore.QCoreApplication.translate
        DialogLoginMedico.setWindowTitle(_translate("DialogLoginMedico", "Login do Medico"))
        self.labelSenhaMedico.setText(_translate("DialogLoginMedico", "Senha:"))
        self.labelLoginMedico.setText(_translate("DialogLoginMedico", "Login:"))
        self.labelTituloMedico.setText(_translate("DialogLoginMedico", "Medico"))
        self.pushButtoneEntrarMedico.setText(_translate("DialogLoginMedico", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogLoginMedico = QtWidgets.QDialog()
    ui = Ui_DialogLoginMedico()
    ui.setupUi(DialogLoginMedico)
    DialogLoginMedico.show()
    sys.exit(app.exec_())
