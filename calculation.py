from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Калькулятор')

text = ''
q = 2
WINDOW_SIZE = 235*q
DISPLAY_HEIGHT = 35*q
BUTTON_SIZE = 40*q

main_win.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)

def button(t):
    def handler():
        global text
        text = text+t
        display.setText(text)
    return handler









#Лэйауты
main_layout = QVBoxLayout()
grid_layout = QGridLayout()


#Виджеты
display = QTextEdit()
display.setFixedHeight(DISPLAY_HEIGHT)
display.setAlignment(Qt.AlignmentFlag.AlignRight)
display.setReadOnly(True)


keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]






buttons = []

main_layout.addWidget(display)
c=0
for k in range(4):
    for i in range(5):
        b = QPushButton(keyBoard[c][i])
        b.setFixedSize(BUTTON_SIZE,BUTTON_SIZE)
        buttons.append(b)
        grid_layout.addWidget(b,c,i)
    c+=1






main_layout.addLayout(grid_layout)
main_win.setLayout(main_layout)



buttons[0].clicked.connect(button('7'))
buttons[1].clicked.connect(button('8'))



main_win.show()
app.exec_()
