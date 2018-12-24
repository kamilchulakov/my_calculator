import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from math import *


def my_round(obj, rounding):
        if '.' in obj:
            dot = obj.index('.')
            after = obj[dot:]
            if len(after) > rounding:
                obj_copy = str(obj)
                last_num = obj_copy[dot + rounding]
                if int(last_num) >= 5:
                    prev_num = int(obj_copy[dot + rounding-1]) + 1
                    if prev_num == 10:
                        prev_num = 0
                        prev_prev_num = obj_copy[dot + rounding-2]
                        obj = obj[:dot] + after[:rounding-1] + str(prev_prev_num) + str(prev_num)
                    else:
                        obj = obj[:dot] + after[:rounding-1] + str(prev_num)
                else:
                    obj = obj[:dot] + after[:rounding]
        return obj


def check_int(obj):
        if obj == int(obj):
            return str(int(obj))
        return str(obj)


class Calculation:
    def main(self, line, rounding):
        while '(' in line:
            try:
                if line.count(')') != line.count('('):
                    raise Exception
                ind_l = line.rindex('(')
                ind_r = line.index(')', ind_l)
                if ind_r - ind_l == 1:
                    raise Exception
                elif line[ind_l-1].isdigit():
                    print(line[ind_r+1], line[ind_r+1].isdigit())
                    raise Exception
            except Exception:
                return 'Error'
            line = line[:ind_l] + self.calculate(line[ind_l+1:ind_r]) + line[ind_r+1:]
        otv = self.calculate(line)
        otv = my_round(otv, rounding)
        return otv

    def findx(self, line, ind):
        num_1 = ''
        k = 0
        for k in range(ind):
            if line[ind-1-k].isdigit():
                num_1 += line[ind-1-k]
            elif line[ind-1-k] == '.':
                num_1 += '.'
            else:
                break
        num_1 = num_1[::-1]
        n1 = ind - 1 - k
        if not line[n1].isdigit():
            n1 += 1
        return num_1, n1

    def findy(self, line, ind):
        num_2 = ''
        n2 = 0
        for j in range(ind + 1, len(line)):
            n2 = j
            if line[j].isdigit() or line[j] == '.':
                num_2 += line[j]
            else:
                if line[ind:ind+3] == 'mod':
                    for y in range(ind + 3, len(line)):
                        n2 = y
                        if line[y].isdigit() or line[y] == '.':
                            num_2 += line[y]
                break
        return num_2, n2

    def calculate(self, line):
        done = False
        if len(line) <= 1:
            raise Exception
        small_operations = ['!', 'sin', 'cos', 'tg', 'ctg', 'log', ]
        for i in small_operations:
            while i in line:
                base = line.rindex(i) + len(i) - 1
                num_1, n1 = self.findy(line, base)
                num_1 = float(num_1)
                line = line[:line.rindex(i)] + self.small_operations(num_1, i) + line[n1+1:]
                done = True
        big_operations = '^ √ / mod x % + -'.split(' ')
        for i in big_operations:
            while i in line and (i != '-' or i != line[0]):
                base = line.rindex(i)
                num_1, n1 = self.findx(line, base)
                num_2, n2 = self.findy(line, base)
                if num_1 == '':
                    return 'Error'
                if num_2 == '':
                    return 'Error'
                num_1 = float(num_1)
                num_2 = float(num_2)
                result = self.big_operations(num_1, num_2, i)
                if result == 'Error':
                    return 'Error'
                line = line[:n1] + result + line[n2+1:]
                done = True
        if not done:
            line = 'Error'
        return line

    def big_operations(self, num1, num2, operation):
        res = 0
        if operation == 'x':
            res = num1 * num2
        elif operation == '-':
            res = num1 - num2
        elif operation == '/':
            if num2 == 0:
                return 'Error'
        elif operation == '+':
            res = num1 + num2
        elif operation == '^':
            res = num1 ** num2
        elif operation == '%':
            res = (num1 * num2) / 100
        elif operation == 'mod':
            res = fmod(num1, num2)
        return str(res)

    def small_operations(self, num1, operation):
        res = 0
        if operation == 'sin':
            res = sin(num1)
        elif operation == 'cos':
            res = cos(num1)
        elif operation == 'tg':
            res = tan(num1)
        elif operation == 'ctg':
            res = 1 / tan(num1)
        elif operation == 'log':
            res = log(num1)
        elif operation == '√':
            res = num1 ** 0.5
        elif operation == '!':
            res = factorial(num1)
        return str(res)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.position = 0
        self.rounding = 5

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
        self.bpi.clicked.connect(lambda: self.write(symbol=str(pi)))
        self.be.clicked.connect(lambda: self.write(symbol=str(e)))
        self.brvn.clicked.connect(self.summary)
        self.bste.clicked.connect(lambda: self.write(symbol='^'))
        self.bsum.clicked.connect(lambda: self.write(symbol='+'))
        self.bumn.clicked.connect(lambda: self.write(symbol='x'))
        self.bdel.clicked.connect(lambda: self.write(symbol='/'))
        self.bscl.clicked.connect(lambda: self.write(symbol='('))
        self.bscr.clicked.connect(lambda: self.write(symbol=')'))
        self.bc.clicked.connect(self.clear)
        self.bright.clicked.connect(self.change_position_right)
        self.bleft.clicked.connect(self.change_position_left)
        self.b10.clicked.connect(lambda: self.write(symbol='10^'))
        self.bdel_2.clicked.connect(self.delete)
        self.bmod.clicked.connect(lambda: self.write(symbol='mod'))
        self.brzn.clicked.connect(lambda: self.write(symbol='-'))
        self.radio_group.buttonClicked.connect(self.change_round)

    def write(self, symbol='0'):
        if self.label.text() not in ['Error', '0']:
            now = self.label.text()
            now = now[:self.position] + symbol + now[self.position:]
            self.label.setText(now)
            self.position += len(symbol)
        else:
            self.label.setText(symbol)
            self.position += len(symbol)

    def delete(self):
        self.label.setText(self.label.text()[:-1])

    def change_position_left(self):
        if self.position >= 1:
            self.position -= 1

    def change_position_right(self):
        if self.position >= 1:
            self.position += 1

    def summary(self):
        primer = self.label.text()
        a = Calculation()
        self.clear()
        main_result = a.main(primer, self.rounding)
        if main_result == 'Error':
            self.label.setText('Error')
        else:
            self.label.setText(check_int(float(main_result)))

    def clear(self):
        self.label.setText('')

    def change_round(self, button):
        self.rounding = int(button.text()) + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
