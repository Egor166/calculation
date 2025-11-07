from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Калькулятор')

#! Виджеты
#? Кноки
# Цифры
button_0 = QPushButton('0')
button_1 = QPushButton('1')
button_2 = QPushButton('2')
button_3 = QPushButton('3')
button_4 = QPushButton('4')
button_5 = QPushButton('5')
button_6 = QPushButton('6')
button_7 = QPushButton('7')
button_8 = QPushButton('8')
button_9 = QPushButton('9')
# Арифметические операторы
button_plus = QPushButton('+')
button_minus = QPushButton('-')
button_multiplication = QPushButton('*')
button_division = QPushButton(':')
button_equally = QPushButton('=')
# Прочие символы
button_point = QPushButton('.')
button_left_bracket = QPushButton('(')
button__right_bracket = QPushButton(')')
button_delete = QPushButton('c')
button_backspace = QPushButton('<=')
#? Дисплэй
text_win = QTextEdit()







text_win = QTextEdit()

















main_win.show()
app.exec_()
