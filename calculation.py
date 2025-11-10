from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


WINDOW_SIZE = 470
DISPLAY_HEIGHT = 70
BUTTON_SIZE = 80
text = ''

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Калькулятор')
main_win.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)

def button(t):
    def handler():
        global text
        text = text+str(t)
        display.setText(text)
    return handler


def result():
    global text
    try:
        text = str(eval(text))
        display.setText(text)
    except:
        text = ''
        display.setText("Error")


def clear_display():
    global text
    text = ''
    display.setText(text)
    
main_layout = QVBoxLayout()
grid_layout = QGridLayout()

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

for i in range (20):
    if buttons[i].text() != '=' and buttons[i].text() != 'C'        :
        buttons[i].clicked.connect(button(buttons[i].text()))
    elif buttons[i].text() == '=':
        buttons[i].clicked.connect(result)
    elif buttons[i].text() == 'C':
        buttons[i].clicked.connect(clear_display)

main_win.show()
app.exec_()


