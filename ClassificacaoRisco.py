# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassificacaoRisco.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FichaAmbulatorialVerso(object):
    def setupUi(self, FichaAmbulatorialVerso):
        FichaAmbulatorialVerso.setObjectName("FichaAmbulatorialVerso")
        FichaAmbulatorialVerso.resize(662, 997)
        FichaAmbulatorialVerso.setStyleSheet("background-color: rgb(192, 255, 218);")
        self.centralwidget = QtWidgets.QWidget(FichaAmbulatorialVerso)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetCabecalho = QtWidgets.QWidget(self.centralwidget)
        self.widgetCabecalho.setGeometry(QtCore.QRect(30, 10, 611, 61))
        self.widgetCabecalho.setObjectName("widgetCabecalho")
        self.labelSubTitulo = QtWidgets.QLabel(self.widgetCabecalho)
        self.labelSubTitulo.setGeometry(QtCore.QRect(80, 30, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelSubTitulo.setFont(font)
        self.labelSubTitulo.setObjectName("labelSubTitulo")
        self.line = QtWidgets.QFrame(self.widgetCabecalho)
        self.line.setGeometry(QtCore.QRect(0, 50, 611, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelTitulo = QtWidgets.QLabel(self.widgetCabecalho)
        self.labelTitulo.setGeometry(QtCore.QRect(140, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.widgetIdentificacaoPaciente = QtWidgets.QWidget(self.centralwidget)
        self.widgetIdentificacaoPaciente.setGeometry(QtCore.QRect(30, 70, 611, 291))
        self.widgetIdentificacaoPaciente.setObjectName("widgetIdentificacaoPaciente")
        self.labelEndereco = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelEndereco.setGeometry(QtCore.QRect(90, 170, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelEndereco.setFont(font)
        self.labelEndereco.setObjectName("labelEndereco")
        self.labelIdade = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelIdade.setGeometry(QtCore.QRect(0, 90, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelIdade.setFont(font)
        self.labelIdade.setObjectName("labelIdade")
        self.labelMae = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelMae.setGeometry(QtCore.QRect(260, 130, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelMae.setFont(font)
        self.labelMae.setObjectName("labelMae")
        self.labelEtnia = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelEtnia.setGeometry(QtCore.QRect(180, 90, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelEtnia.setFont(font)
        self.labelEtnia.setObjectName("labelEtnia")
        self.labelID = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelID.setGeometry(QtCore.QRect(550, 90, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")
        self.labelCidade = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelCidade.setGeometry(QtCore.QRect(200, 240, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelCidade.setFont(font)
        self.labelCidade.setObjectName("labelCidade")
        self.lineEditBairro = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditBairro.setGeometry(QtCore.QRect(50, 240, 131, 20))
        self.lineEditBairro.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditBairro.setText("")
        self.lineEditBairro.setObjectName("lineEditBairro")
        self.labelData = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelData.setGeometry(QtCore.QRect(370, 50, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelData.setFont(font)
        self.labelData.setObjectName("labelData")
        self.timeEditHoraInicio = QtWidgets.QTimeEdit(self.widgetIdentificacaoPaciente)
        self.timeEditHoraInicio.setGeometry(QtCore.QRect(550, 50, 61, 22))
        self.timeEditHoraInicio.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.timeEditHoraInicio.setObjectName("timeEditHoraInicio")
        self.lineEditIdade = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditIdade.setGeometry(QtCore.QRect(60, 90, 101, 20))
        self.lineEditIdade.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditIdade.setText("")
        self.lineEditIdade.setObjectName("lineEditIdade")
        self.lineEditMae = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditMae.setGeometry(QtCore.QRect(300, 130, 311, 20))
        self.lineEditMae.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditMae.setText("")
        self.lineEditMae.setObjectName("lineEditMae")
        self.lineEditCidade = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditCidade.setGeometry(QtCore.QRect(260, 240, 231, 20))
        self.lineEditCidade.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditCidade.setText("")
        self.lineEditCidade.setObjectName("lineEditCidade")
        self.labelIndentificacaoPaciente = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelIndentificacaoPaciente.setGeometry(QtCore.QRect(200, 0, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelIndentificacaoPaciente.setFont(font)
        self.labelIndentificacaoPaciente.setObjectName("labelIndentificacaoPaciente")
        self.lineEditEtnia = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditEtnia.setGeometry(QtCore.QRect(220, 90, 101, 20))
        self.lineEditEtnia.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditEtnia.setText("")
        self.lineEditEtnia.setObjectName("lineEditEtnia")
        self.dateEditDataNascimento = QtWidgets.QDateEdit(self.widgetIdentificacaoPaciente)
        self.dateEditDataNascimento.setGeometry(QtCore.QRect(410, 50, 81, 22))
        self.dateEditDataNascimento.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.dateEditDataNascimento.setObjectName("dateEditDataNascimento")
        self.labelNumero = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelNumero.setGeometry(QtCore.QRect(300, 210, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNumero.setFont(font)
        self.labelNumero.setObjectName("labelNumero")
        self.lineEditProfissao = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditProfissao.setGeometry(QtCore.QRect(140, 130, 111, 20))
        self.lineEditProfissao.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditProfissao.setText("")
        self.lineEditProfissao.setObjectName("lineEditProfissao")
        self.lineEditComplemento = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditComplemento.setGeometry(QtCore.QRect(490, 210, 121, 20))
        self.lineEditComplemento.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditComplemento.setText("")
        self.lineEditComplemento.setObjectName("lineEditComplemento")
        self.lineEditNaturalidade = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditNaturalidade.setGeometry(QtCore.QRect(430, 90, 111, 20))
        self.lineEditNaturalidade.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditNaturalidade.setText("")
        self.lineEditNaturalidade.setObjectName("lineEditNaturalidade")
        self.labelNaturalidade = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelNaturalidade.setGeometry(QtCore.QRect(330, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNaturalidade.setFont(font)
        self.labelNaturalidade.setObjectName("labelNaturalidade")
        self.line_2 = QtWidgets.QFrame(self.widgetIdentificacaoPaciente)
        self.line_2.setGeometry(QtCore.QRect(0, 270, 611, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEditNumero = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditNumero.setGeometry(QtCore.QRect(330, 210, 51, 20))
        self.lineEditNumero.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditNumero.setText("")
        self.lineEditNumero.setObjectName("lineEditNumero")
        self.lineEditRegistro = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditRegistro.setGeometry(QtCore.QRect(530, 20, 81, 20))
        self.lineEditRegistro.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditRegistro.setText("")
        self.lineEditRegistro.setObjectName("lineEditRegistro")
        self.lineEditLongradouro = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditLongradouro.setGeometry(QtCore.QRect(90, 210, 201, 20))
        self.lineEditLongradouro.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditLongradouro.setText("")
        self.lineEditLongradouro.setObjectName("lineEditLongradouro")
        self.lineEditUF = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditUF.setGeometry(QtCore.QRect(560, 240, 51, 20))
        self.lineEditUF.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditUF.setText("")
        self.lineEditUF.setObjectName("lineEditUF")
        self.labelBairro = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelBairro.setGeometry(QtCore.QRect(0, 240, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelBairro.setFont(font)
        self.labelBairro.setObjectName("labelBairro")
        self.lineEditID = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditID.setGeometry(QtCore.QRect(570, 90, 41, 20))
        self.lineEditID.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditID.setText("")
        self.lineEditID.setObjectName("lineEditID")
        self.labelLongradouro = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelLongradouro.setGeometry(QtCore.QRect(0, 210, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelLongradouro.setFont(font)
        self.labelLongradouro.setObjectName("labelLongradouro")
        self.lineEditNome = QtWidgets.QLineEdit(self.widgetIdentificacaoPaciente)
        self.lineEditNome.setGeometry(QtCore.QRect(60, 50, 301, 20))
        self.lineEditNome.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditNome.setText("")
        self.lineEditNome.setObjectName("lineEditNome")
        self.labelNome = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelNome.setGeometry(QtCore.QRect(0, 50, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelUF = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelUF.setGeometry(QtCore.QRect(520, 240, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelUF.setFont(font)
        self.labelUF.setObjectName("labelUF")
        self.labelHoraInicio = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelHoraInicio.setGeometry(QtCore.QRect(500, 50, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelHoraInicio.setFont(font)
        self.labelHoraInicio.setObjectName("labelHoraInicio")
        self.labelRegistro = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelRegistro.setGeometry(QtCore.QRect(460, 20, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelRegistro.setFont(font)
        self.labelRegistro.setObjectName("labelRegistro")
        self.labelProfissao = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelProfissao.setGeometry(QtCore.QRect(0, 130, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelProfissao.setFont(font)
        self.labelProfissao.setObjectName("labelProfissao")
        self.labelComplemento = QtWidgets.QLabel(self.widgetIdentificacaoPaciente)
        self.labelComplemento.setGeometry(QtCore.QRect(390, 210, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelComplemento.setFont(font)
        self.labelComplemento.setObjectName("labelComplemento")
        self.widgetClassificacaoRisco = QtWidgets.QWidget(self.centralwidget)
        self.widgetClassificacaoRisco.setGeometry(QtCore.QRect(30, 360, 611, 551))
        self.widgetClassificacaoRisco.setObjectName("widgetClassificacaoRisco")
        self.radioVerde = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioVerde.setGeometry(QtCore.QRect(440, 230, 71, 21))
        self.radioVerde.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.radioVerde.setObjectName("radioVerde")
        self.labelSaturacao = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelSaturacao.setGeometry(QtCore.QRect(0, 260, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelSaturacao.setFont(font)
        self.labelSaturacao.setObjectName("labelSaturacao")
        self.labelNumeroFluxograma = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelNumeroFluxograma.setGeometry(QtCore.QRect(530, 160, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelNumeroFluxograma.setFont(font)
        self.labelNumeroFluxograma.setObjectName("labelNumeroFluxograma")
        self.lineEditCoordenador = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditCoordenador.setGeometry(QtCore.QRect(130, 490, 191, 20))
        self.lineEditCoordenador.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditCoordenador.setText("")
        self.lineEditCoordenador.setObjectName("lineEditCoordenador")
        self.lineEditFC = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditFC.setGeometry(QtCore.QRect(570, 260, 41, 20))
        self.lineEditFC.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditFC.setText("")
        self.lineEditFC.setObjectName("lineEditFC")
        self.lineEditCoren = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditCoren.setGeometry(QtCore.QRect(380, 450, 51, 20))
        self.lineEditCoren.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditCoren.setText("")
        self.lineEditCoren.setObjectName("lineEditCoren")
        self.line_3 = QtWidgets.QFrame(self.widgetClassificacaoRisco)
        self.line_3.setGeometry(QtCore.QRect(-10, 520, 621, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.dateEditDataHoje = QtWidgets.QDateEdit(self.widgetClassificacaoRisco)
        self.dateEditDataHoje.setGeometry(QtCore.QRect(370, 490, 81, 22))
        self.dateEditDataHoje.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.dateEditDataHoje.setObjectName("dateEditDataHoje")
        self.labelTemperatura = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelTemperatura.setGeometry(QtCore.QRect(230, 260, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelTemperatura.setFont(font)
        self.labelTemperatura.setObjectName("labelTemperatura")
        self.radioAzul = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioAzul.setGeometry(QtCore.QRect(510, 230, 41, 21))
        self.radioAzul.setStyleSheet("color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.radioAzul.setObjectName("radioAzul")
        self.labelDestinoEncaminhamento = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelDestinoEncaminhamento.setGeometry(QtCore.QRect(10, 420, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelDestinoEncaminhamento.setFont(font)
        self.labelDestinoEncaminhamento.setObjectName("labelDestinoEncaminhamento")
        self.labelCoordenador = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelCoordenador.setGeometry(QtCore.QRect(10, 490, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelCoordenador.setFont(font)
        self.labelCoordenador.setObjectName("labelCoordenador")
        self.lineEditTemperatura = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditTemperatura.setGeometry(QtCore.QRect(270, 260, 51, 20))
        self.lineEditTemperatura.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditTemperatura.setText("")
        self.lineEditTemperatura.setObjectName("lineEditTemperatura")
        self.radioButtonDestinoPSF = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioButtonDestinoPSF.setGeometry(QtCore.QRect(390, 420, 82, 17))
        self.radioButtonDestinoPSF.setObjectName("radioButtonDestinoPSF")
        self.labelDiscriminador = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelDiscriminador.setGeometry(QtCore.QRect(10, 200, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelDiscriminador.setFont(font)
        self.labelDiscriminador.setObjectName("labelDiscriminador")
        self.labelClassificacaoRisco = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelClassificacaoRisco.setGeometry(QtCore.QRect(230, 0, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelClassificacaoRisco.setFont(font)
        self.labelClassificacaoRisco.setObjectName("labelClassificacaoRisco")
        self.radioButtonDestinoConsultorio = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioButtonDestinoConsultorio.setGeometry(QtCore.QRect(210, 420, 82, 17))
        self.radioButtonDestinoConsultorio.setObjectName("radioButtonDestinoConsultorio")
        self.lineEditNumeroFluxograma = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditNumeroFluxograma.setGeometry(QtCore.QRect(560, 160, 51, 20))
        self.lineEditNumeroFluxograma.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditNumeroFluxograma.setText("")
        self.lineEditNumeroFluxograma.setObjectName("lineEditNumeroFluxograma")
        self.radioAmarela = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioAmarela.setGeometry(QtCore.QRect(520, 200, 71, 21))
        self.radioAmarela.setStyleSheet("color: rgb(239, 239, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.radioAmarela.setObjectName("radioAmarela")
        self.labelEnfermeiro = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelEnfermeiro.setGeometry(QtCore.QRect(10, 450, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelEnfermeiro.setFont(font)
        self.labelEnfermeiro.setObjectName("labelEnfermeiro")
        self.lineEditFluxograma = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditFluxograma.setGeometry(QtCore.QRect(100, 160, 381, 20))
        self.lineEditFluxograma.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditFluxograma.setText("")
        self.lineEditFluxograma.setObjectName("lineEditFluxograma")
        self.lineEditDiscriminador = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditDiscriminador.setGeometry(QtCore.QRect(100, 200, 241, 20))
        self.lineEditDiscriminador.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditDiscriminador.setText("")
        self.lineEditDiscriminador.setObjectName("lineEditDiscriminador")
        self.labelFluxograma = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelFluxograma.setGeometry(QtCore.QRect(10, 160, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelFluxograma.setFont(font)
        self.labelFluxograma.setObjectName("labelFluxograma")
        self.labelGlasgow = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelGlasgow.setGeometry(QtCore.QRect(130, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelGlasgow.setFont(font)
        self.labelGlasgow.setObjectName("labelGlasgow")
        self.labelFC = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelFC.setGeometry(QtCore.QRect(540, 260, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelFC.setFont(font)
        self.labelFC.setObjectName("labelFC")
        self.radioLaranja = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioLaranja.setGeometry(QtCore.QRect(460, 200, 61, 21))
        self.radioLaranja.setStyleSheet("color: rgb(255, 138, 55);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.radioLaranja.setObjectName("radioLaranja")
        self.labelGlicemia = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelGlicemia.setGeometry(QtCore.QRect(330, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelGlicemia.setFont(font)
        self.labelGlicemia.setObjectName("labelGlicemia")
        self.radioButtonVermelha = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioButtonVermelha.setGeometry(QtCore.QRect(390, 200, 71, 21))
        self.radioButtonVermelha.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.radioButtonVermelha.setObjectName("radioButtonVermelha")
        self.labelCoren = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelCoren.setGeometry(QtCore.QRect(330, 450, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelCoren.setFont(font)
        self.labelCoren.setObjectName("labelCoren")
        self.labelSituacaoQueixa = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelSituacaoQueixa.setGeometry(QtCore.QRect(10, 40, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelSituacaoQueixa.setFont(font)
        self.labelSituacaoQueixa.setObjectName("labelSituacaoQueixa")
        self.labelData_2 = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelData_2.setGeometry(QtCore.QRect(330, 490, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelData_2.setFont(font)
        self.labelData_2.setObjectName("labelData_2")
        self.textEditDescricaoSituacaoQueixa = QtWidgets.QTextEdit(self.widgetClassificacaoRisco)
        self.textEditDescricaoSituacaoQueixa.setGeometry(QtCore.QRect(10, 60, 601, 91))
        self.textEditDescricaoSituacaoQueixa.setStyleSheet("background-color: rgb(255, 249, 248);")
        self.textEditDescricaoSituacaoQueixa.setObjectName("textEditDescricaoSituacaoQueixa")
        self.lineEditEnfermeiro = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditEnfermeiro.setGeometry(QtCore.QRect(110, 450, 211, 20))
        self.lineEditEnfermeiro.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditEnfermeiro.setText("")
        self.lineEditEnfermeiro.setObjectName("lineEditEnfermeiro")
        self.radioButtonDestinoAmbulatorio = QtWidgets.QRadioButton(self.widgetClassificacaoRisco)
        self.radioButtonDestinoAmbulatorio.setGeometry(QtCore.QRect(300, 420, 82, 17))
        self.radioButtonDestinoAmbulatorio.setObjectName("radioButtonDestinoAmbulatorio")
        self.labelGrauDor = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelGrauDor.setGeometry(QtCore.QRect(450, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelGrauDor.setFont(font)
        self.labelGrauDor.setObjectName("labelGrauDor")
        self.lineEditGrauDor = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditGrauDor.setGeometry(QtCore.QRect(510, 260, 21, 20))
        self.lineEditGrauDor.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditGrauDor.setText("")
        self.lineEditGrauDor.setObjectName("lineEditGrauDor")
        self.lineEditSaturacao = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditSaturacao.setGeometry(QtCore.QRect(70, 260, 51, 20))
        self.lineEditSaturacao.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditSaturacao.setText("")
        self.lineEditSaturacao.setObjectName("lineEditSaturacao")
        self.textEditDescricaoClassificacaoCor = QtWidgets.QTextEdit(self.widgetClassificacaoRisco)
        self.textEditDescricaoClassificacaoCor.setGeometry(QtCore.QRect(210, 300, 191, 91))
        self.textEditDescricaoClassificacaoCor.setStyleSheet("background-color: rgb(255, 249, 248);")
        self.textEditDescricaoClassificacaoCor.setObjectName("textEditDescricaoClassificacaoCor")
        self.labelCor = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelCor.setGeometry(QtCore.QRect(350, 200, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelCor.setFont(font)
        self.labelCor.setObjectName("labelCor")
        self.lineEditGlasgow = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditGlasgow.setGeometry(QtCore.QRect(190, 260, 31, 20))
        self.lineEditGlasgow.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditGlasgow.setText("")
        self.lineEditGlasgow.setObjectName("lineEditGlasgow")
        self.lineEditGlicemia = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditGlicemia.setGeometry(QtCore.QRect(390, 260, 51, 20))
        self.lineEditGlicemia.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditGlicemia.setText("")
        self.lineEditGlicemia.setObjectName("lineEditGlicemia")
        self.labelHoraFim = QtWidgets.QLabel(self.widgetClassificacaoRisco)
        self.labelHoraFim.setGeometry(QtCore.QRect(490, 490, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelHoraFim.setFont(font)
        self.labelHoraFim.setObjectName("labelHoraFim")
        self.timeEditHoraFim = QtWidgets.QTimeEdit(self.widgetClassificacaoRisco)
        self.timeEditHoraFim.setGeometry(QtCore.QRect(540, 490, 61, 22))
        self.timeEditHoraFim.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.timeEditHoraFim.setObjectName("timeEditHoraFim")
        self.lineEditGlicemia_2 = QtWidgets.QLineEdit(self.widgetClassificacaoRisco)
        self.lineEditGlicemia_2.setGeometry(QtCore.QRect(400, 450, 81, 20))
        self.lineEditGlicemia_2.setStyleSheet("background-color: rgb(242, 255, 250);")
        self.lineEditGlicemia_2.setText("")
        self.lineEditGlicemia_2.setObjectName("lineEditGlicemia_2")
        self.widgetRodapeHospital = QtWidgets.QWidget(self.centralwidget)
        self.widgetRodapeHospital.setGeometry(QtCore.QRect(30, 910, 611, 80))
        self.widgetRodapeHospital.setObjectName("widgetRodapeHospital")
        self.labelCNPJ = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelCNPJ.setGeometry(QtCore.QRect(200, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.labelCNPJ.setFont(font)
        self.labelCNPJ.setObjectName("labelCNPJ")
        self.labelTelefoneHosital = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelTelefoneHosital.setGeometry(QtCore.QRect(230, 60, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelTelefoneHosital.setFont(font)
        self.labelTelefoneHosital.setObjectName("labelTelefoneHosital")
        self.labelEnderecoHospital = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelEnderecoHospital.setGeometry(QtCore.QRect(190, 40, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelEnderecoHospital.setFont(font)
        self.labelEnderecoHospital.setObjectName("labelEnderecoHospital")
        self.labelAssociacao = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelAssociacao.setGeometry(QtCore.QRect(120, 0, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.labelAssociacao.setFont(font)
        self.labelAssociacao.setObjectName("labelAssociacao")
        self.labelLogo = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelLogo.setGeometry(QtCore.QRect(20, 0, 91, 71))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("logoHospital.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.labelLogo_2 = QtWidgets.QLabel(self.widgetRodapeHospital)
        self.labelLogo_2.setGeometry(QtCore.QRect(20, 0, 91, 71))
        self.labelLogo_2.setText("")
        self.labelLogo_2.setPixmap(QtGui.QPixmap("Formularios/logoHospital.png"))
        self.labelLogo_2.setObjectName("labelLogo_2")
        FichaAmbulatorialVerso.setCentralWidget(self.centralwidget)

        self.retranslateUi(FichaAmbulatorialVerso)
        QtCore.QMetaObject.connectSlotsByName(FichaAmbulatorialVerso)

    def retranslateUi(self, FichaAmbulatorialVerso):
        _translate = QtCore.QCoreApplication.translate
        FichaAmbulatorialVerso.setWindowTitle(_translate("FichaAmbulatorialVerso", "SISTEMA DE MANCHESTER"))
        self.labelSubTitulo.setText(_translate("FichaAmbulatorialVerso", "ACOLHIMENTO COM CLASSIFICAÇÃO DE RISCO - SISTEMA DE MANCHESTER"))
        self.labelTitulo.setText(_translate("FichaAmbulatorialVerso", "SECRETARIA DE ESTADO DE SAÚDE DE MINAS GERAIS"))
        self.labelEndereco.setText(_translate("FichaAmbulatorialVerso", "ENDEREÇO:  "))
        self.labelIdade.setText(_translate("FichaAmbulatorialVerso", "Idade:"))
        self.labelMae.setText(_translate("FichaAmbulatorialVerso", "Mãe:"))
        self.labelEtnia.setText(_translate("FichaAmbulatorialVerso", "Etnia:"))
        self.labelID.setText(_translate("FichaAmbulatorialVerso", "ID:"))
        self.labelCidade.setText(_translate("FichaAmbulatorialVerso", "Cidade:"))
        self.labelData.setText(_translate("FichaAmbulatorialVerso", "Data:"))
        self.labelIndentificacaoPaciente.setText(_translate("FichaAmbulatorialVerso", "IDENTIFICAÇÃO DO PACIENTE"))
        self.labelNumero.setText(_translate("FichaAmbulatorialVerso", "Nº:"))
        self.labelNaturalidade.setText(_translate("FichaAmbulatorialVerso", "Naturalidade:"))
        self.labelBairro.setText(_translate("FichaAmbulatorialVerso", "Bairro:"))
        self.labelLongradouro.setText(_translate("FichaAmbulatorialVerso", "Longradouro:"))
        self.labelNome.setText(_translate("FichaAmbulatorialVerso", "Nome:"))
        self.labelUF.setText(_translate("FichaAmbulatorialVerso", "UF:"))
        self.labelHoraInicio.setText(_translate("FichaAmbulatorialVerso", "Horas: "))
        self.labelRegistro.setText(_translate("FichaAmbulatorialVerso", "Registro:"))
        self.labelProfissao.setText(_translate("FichaAmbulatorialVerso", "Profissão/Ocupação:"))
        self.labelComplemento.setText(_translate("FichaAmbulatorialVerso", "Complemento:"))
        self.radioVerde.setText(_translate("FichaAmbulatorialVerso", "Verde"))
        self.labelSaturacao.setText(_translate("FichaAmbulatorialVerso", "Saturação:"))
        self.labelNumeroFluxograma.setText(_translate("FichaAmbulatorialVerso", "Nº:"))
        self.labelTemperatura.setText(_translate("FichaAmbulatorialVerso", "Temp:"))
        self.radioAzul.setText(_translate("FichaAmbulatorialVerso", "Azul"))
        self.labelDestinoEncaminhamento.setText(_translate("FichaAmbulatorialVerso", "DESTINO/ENCAMINHAMENTO:  "))
        self.labelCoordenador.setText(_translate("FichaAmbulatorialVerso", "Coordenador (a):"))
        self.radioButtonDestinoPSF.setText(_translate("FichaAmbulatorialVerso", "PSF"))
        self.labelDiscriminador.setText(_translate("FichaAmbulatorialVerso", "Discriminador: "))
        self.labelClassificacaoRisco.setText(_translate("FichaAmbulatorialVerso", "CLASSIFICAÇÃO DE RISCO"))
        self.radioButtonDestinoConsultorio.setText(_translate("FichaAmbulatorialVerso", "Consultório"))
        self.radioAmarela.setText(_translate("FichaAmbulatorialVerso", "Amarelo"))
        self.labelEnfermeiro.setText(_translate("FichaAmbulatorialVerso", "Enfermeiro (a):"))
        self.labelFluxograma.setText(_translate("FichaAmbulatorialVerso", "Fluxograma: "))
        self.labelGlasgow.setText(_translate("FichaAmbulatorialVerso", "Glasglow:"))
        self.labelFC.setText(_translate("FichaAmbulatorialVerso", "FC:"))
        self.radioLaranja.setText(_translate("FichaAmbulatorialVerso", "Laranja"))
        self.labelGlicemia.setText(_translate("FichaAmbulatorialVerso", "Glicemia:"))
        self.radioButtonVermelha.setText(_translate("FichaAmbulatorialVerso", "Vermelha"))
        self.labelCoren.setText(_translate("FichaAmbulatorialVerso", "COREN:"))
        self.labelSituacaoQueixa.setText(_translate("FichaAmbulatorialVerso", "Situação/Queixa: "))
        self.labelData_2.setText(_translate("FichaAmbulatorialVerso", "Data:"))
        self.radioButtonDestinoAmbulatorio.setText(_translate("FichaAmbulatorialVerso", "Ambulatório"))
        self.labelGrauDor.setText(_translate("FichaAmbulatorialVerso", "Grau Dor:"))
        self.labelCor.setText(_translate("FichaAmbulatorialVerso", "Cor:"))
        self.labelHoraFim.setText(_translate("FichaAmbulatorialVerso", "Horas: "))
        self.labelCNPJ.setText(_translate("FichaAmbulatorialVerso", "CNPJ: 07.605.010/0001-08"))
        self.labelTelefoneHosital.setText(_translate("FichaAmbulatorialVerso", " Telefone: (33) 3261-3115"))
        self.labelEnderecoHospital.setText(_translate("FichaAmbulatorialVerso", "Rua: Lajão, 93 – Centro– Conselheiro Pena/MG -"))
        self.labelAssociacao.setText(_translate("FichaAmbulatorialVerso", "Associação Prefeito Hélcio Valentim de Andrade"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FichaAmbulatorialVerso = QtWidgets.QMainWindow()
    ui = Ui_FichaAmbulatorialVerso()
    ui.setupUi(FichaAmbulatorialVerso)
    FichaAmbulatorialVerso.show()
    sys.exit(app.exec_())
