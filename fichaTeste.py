import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit

class FichaAmbulatorial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 50
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo=" Ficha Ambulatorial "

        self.textBoxNome = QLineEdit(self)
        self.textBoxNome.move(100, 50)
        self.textBoxNome.resize(300, 30)

        botao1 = QPushButton('Enviar Para Enfermeira', self)
        botao1.move(400, 500)
        botao1.resize(150, 30)
        botao1.setStyleSheet('QPushButton {background-color:#66c000;font:bold;font-size:12px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Enviar Para Medico', self)
        botao2.move(600, 500)
        botao2.resize(150, 30)
        botao2.setStyleSheet('QPushButton {background-color:#309d54;font:bold;font-size:12px}')
        botao2.clicked.connect(self.botao2_click)

        botao3 = QPushButton('Enviar Texto', self)
        botao3.move(100, 500)
        botao3.resize(150, 30)
        botao3.setStyleSheet('QPushButton {background-color:#66c270;font:bold;font-size:12px}')
        botao3.clicked.connect(self.botao3_click)

        self.labelNome = QLabel(self)
        self.labelNome.setText('Nome:')
        self.labelNome.move(50, 50)
        self.labelNome.resize(150, 30)
        self.labelNome.setStyleSheet('QLabel {color:#004d00;font:bold;font-size:12px}')

        self.labelEnviar = QLabel(self)
        self.labelEnviar.setText('Enviar:')
        self.labelEnviar.move(500, 450)
        self.labelEnviar.resize(500, 30)
        self.labelEnviar.setStyleSheet('QLabel {color:#004d00;font:bold;font-size:12px}')

        self.labelMostra = QLabel(self)
        self.labelMostra.setText('Mostra:')
        self.labelMostra.move(50, 100)
        self.labelMostra.resize(500, 30)
        self.labelMostra.setStyleSheet('QLabel {color:#004d00;font:bold;font-size:12px}')


        self.CarregarFichaAmbulatorial()

    def CarregarFichaAmbulatorial (self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('Enviado para triagem!')
        self.labelEnviar.setText('Enviado para triagem')
        self.labelEnviar.setStyleSheet('QLabel {color:#a526ff;font:bold;font-size:12px}')

    def botao3_click(self):
        conteudo = self.textBoxNome.text()
        self.labelMostra.setText('Mostra: ' + conteudo)

    def botao2_click(self):
        print('Enviado para o consultorio!')
        self.labelEnviar.setText('Enviado para consultorio')
        self.labelEnviar.setStyleSheet('QLabel {color:#ff7c00;font:bold;font-size:12px}')



aplicacao = QApplication(sys.argv)
ficha = FichaAmbulatorial()
sys.exit(aplicacao.exec())






