import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import math


def calculate(line):
    operations = set(list('/x+-'))
    n1 = 0
    n2 = 2
    if len(line) <= 2:
        raise Exception
    for i in operations:
        while i in line:
            base = line.rindex(i)
            num_1 = ''
            num_2 = ''
            for j in range(base + 1, len(line)):
                if line[j].isdigit():
                    num_2 += line[j]
                else:
                    n2 = j
                    break
            line = line[::-1]
            base -= len(line)
            base *= - 1
            for k in range(base, len(line)):
                if line[k].isdigit():
                    num_1 += line[k]
                else:
                    num_1 = num_1[::-1]
                    n1 = k
                    break
            line = line[::-1]


def cut(obj, ind_1, ind_2):
    obj = obj[:ind_1] + calculate(obj[ind_1:ind_2]) + obj[ind_2+1:]
    return ''.join(obj)


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
        self.brvn.clicked.connect(self.summary)
        self.bste.clicked.connect(lambda: self.write(symbol='^'))
        self.bsum.clicked.connect(lambda: self.write(symbol='+'))
        self.bumn.clicked.connect(lambda: self.write(symbol='x'))
        self.bdel.clicked.connect(lambda: self.write(symbol='/'))
        self.bscl.clicked.connect(lambda: self.write(symbol='('))
        self.bscr.clicked.connect(lambda: self.write(symbol=')'))
        self.bc.clicked.connect(self.clear)

    def write(self, symbol='0'):
        if self.label.text() not in ['Error', '0']:
            self.label.setText(self.label.text() + symbol)
        else:
            self.label.setText(symbol)

    def summary(self):
        primer = self.label.text()
        while '(' in primer:
            try:
                ind_l = primer.rindex('(')
                ind_r = primer.index(')', ind_l)
                if ind_r - ind_l == 1:
                    raise Exception
                elif primer[ind_l-1].isdigit() or not primer[ind_l+1].isdigit():
                    raise Exception
                primer = cut(primer, ind_l, ind_r)
            except:
                self.label.setText('Error')
                primer = ''
        print(primer)

    def clear(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
