import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import math

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('calculate.ui', self)
        self.b0.clicked.connect(lambda: self.write(symbol='0'))
        self.b1.clicked.connect(lambda: self.write(symbol='1'))
        self.b2.clicked.connect(lambda: self.write(symbol='2'))
        self.b3.clicked.connect(lambda: self.write(symbol='3'))
        self.b4.clicked.connect(lambda: self.write(symbol='4'))
        self.b5.clicked.connect(lambda: self.write(symbol='5'))
        self.b6.clicked.connect(lambda: self.write(symbol='6'))
        self.b7.clicked.connect(lambda: self.write(symbol='7'))
        self.b8.clicked.connect(lambda: self.write(symbol='8'))
        self.b9.clicked.connect(lambda: self.write(symbol='9'))
        self.bcos.clicked.connect(lambda: self.write(symbol='cos'))
        self.bsin.clicked.connect(lambda: self.write(symbol='sin'))
        self.btg.clicked.connect(lambda: self.write(symbol='tg'))
        self.bctg.clicked.connect(lambda: self.write(symbol='ctg'))
        self.bdot.clicked.connect(lambda: self.write(symbol='.'))
        self.bfact.clicked.connect(lambda: self.write(symbol='!'))
        self.bkor.clicked.connect(lambda: self.write(symbol='√'))
        self.blog.clicked.connect(lambda: self.write(symbol='log'))
        self.bpi.clicked.connect(lambda: self.write(symbol='pi'))
        self.brvn.clicked.connect(lambda: self.write(symbol='='))
        self.bste.clicked.connect(lambda: self.write(symbol='^'))
        self.bsum.clicked.connect(lambda: self.write(symbol='-'))
        self.bumn.clicked.connect(lambda: self.write(symbol='x'))
        self.bdel.clicked.connect(lambda: self.write(symbol='/'))
        self.bscl.clicked.connect(lambda: self.write(symbol='('))
        self.bscr.clicked.connect(lambda: self.write(symbol=')'))


    def write(self, symbol='0'):
        self.label.setText(self.label.text() + symbol)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
