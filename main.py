import sys
import math
from PyQt5 import QtWidgets
from app import Calculator


class MainWindow(QtWidgets.QMainWindow, Calculator):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_0.clicked.connect(lambda: self.show_it('0'))
        self.button_1.clicked.connect(lambda: self.show_it('1'))
        self.button_2.clicked.connect(lambda: self.show_it('2'))
        self.button_3.clicked.connect(lambda: self.show_it('3'))
        self.button_4.clicked.connect(lambda: self.show_it('4'))
        self.button_5.clicked.connect(lambda: self.show_it('5'))
        self.button_6.clicked.connect(lambda: self.show_it('6'))
        self.button_7.clicked.connect(lambda: self.show_it('7'))
        self.button_8.clicked.connect(lambda: self.show_it('8'))
        self.button_9.clicked.connect(lambda: self.show_it('9'))
        self.button_add.clicked.connect(lambda: self.show_it('+'))
        self.button_sub.clicked.connect(lambda: self.show_it('-'))
        self.button_mul.clicked.connect(lambda: self.show_it('*'))
        self.button_div.clicked.connect(lambda: self.show_it('/'))
        self.button_mod.clicked.connect(lambda: self.show_it('%'))
        self.button_decimal.clicked.connect(lambda: self.show_it('.'))
        self.button_clear.clicked.connect(lambda: self.clear(True))
        self.button_backspace.clicked.connect(lambda: self.clear(False))
        self.button_equals.clicked.connect(self.equal)
        self.button_sign.clicked.connect(self.sign)
        self.button_bracket.clicked.connect(self.bracket)
        self.button_log.clicked.connect(self.log)
        self.button_ln.clicked.connect(self.ln)
        self.button_e.clicked.connect(self.exponent)

    def exponent(self):
        try:
            screen = self.display.text()
            ans = round(math.exp(eval(screen)), 4)
            self.display.setText(str(ans))
        except:
            self.display.setText('Error')

    def log(self):
        try:
            screen = int(self.display.text())
            ans = round(math.log(screen)/math.log(10), 4)
            self.display.setText(str(ans))
        except:
            self.display.setText('Error')

    def ln(self):
        try:
            screen = int(self.display.text())
            ans = round(math.log(screen), 4)
            self.display.setText(str(ans))
        except:
            self.display.setText('Error')

    def bracket(self):
        screen = self.display.text()
        if screen == '':
            screen = screen + '('
        elif screen[-1].isdigit():
            screen = screen + ')'
        else:
            screen = screen + '('
        self.display.setText(screen)

    def sign(self):
        screen = self.display.text()
        if screen[0] == '-':
            test_screen = screen[1:]
        else:
            test_screen = screen
        valid = True
        for i in test_screen:
            if not i.isdigit() and i != '.':
                valid = False
                break
        if valid:
            if screen[0] == '-':
                screen = screen[1:]
            else:
                screen = '-' + screen
            self.display.setText(screen)
        else:
            self.display.setText('Error')

    def show_it(self, val):
        screen = self.display.text()
        self.display.setText(screen + val)

    def clear(self, all):
        if all:
            self.display.setText('')
        else:
            screen = self.display.text()
            screen = screen[:-1]
            self.display.setText(screen)

    def equal(self):
        try:
            screen = self.display.text()
            ans = round(eval(screen), 4)
            self.display.setText(str(ans))
        except:
            self.display.setText('Error')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
