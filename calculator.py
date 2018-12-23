import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from math import *


class Calculation:
    def findx(self, line, ind):
        num_1 = ''
        for k in range(ind):
            if line[ind-1-k].isdigit():
                num_1 += line[ind-1-k]
            else:
                break
        num_1 = num_1[::-1]
        n1 = ind - 1 - k
        if not line[n1].isdigit():
            n1 += 1
        return num_1, n1

    def findy(self, line, ind):
        num_2 = ''
        for j in range(ind + 1, len(line)):
            if line[j].isdigit() or line[j] == '.':
                num_2 += line[j]
            else:
                break
        n2 = j
        return num_2, n2

    def calculate(self, line):
        if len(line) <= 1:
            raise Exception
        small_operations = ['sin', 'cos', 'tg', 'ctg', 'log']
        big_operations = '√ / x + - ^'.split(' ')
        for i in big_operations:
            while i in line:
                base = line.rindex(i)
                num_1, n1 = self.findx(line, base)
                num_2, n2 = self.findy(line, base)
                print(line[:n1])
                num_1 = float(num_1)
                num_2 = float(num_2)
                line = line[:n1] + str(self.big_operations(num_1, num_2, i)) + line[n2+1:]
                print(line)
        return line

    def big_operations(self, num1, num2, operation):
        if operation == 'x':
            res = num1 * num2
        elif operation == '-':
            res = num1 - num2
        elif operation == '/':
            res = num1 / num2
        elif operation == '+':
            res = num1 + num2
        elif operation == '^':
            res = num1 ** num2
        elif operation == '√':
            res = num2 ** (1 / num1)
        return res

    def small_operations(self, num1, operation):
        if operation == 'sin':
            res = sin(num1)
        elif operation == 'cos':
            res = num1
        elif operation == 'tg':
            res = tan(num1)
        elif operation == 'ctg':
            res = 1 / tan(num1)
        elif operation == 'log':
            res = log(num1)
        return res


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
        a = Calculation()
        self.clear()
        self.label.setText(a.calculate(primer))


    def clear(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

