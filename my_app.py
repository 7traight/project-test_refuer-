from PyQt5.QtWidgets import *
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
        self.layout = QVBoxLayout()
        self.text_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.layout.addWidget(self.text_hello)
        self.layout.addWidget(self.txt_instruction)
        self.layout.addWidget(self.txt_next)
        self.setLayout(self.layout)
        self.setStyleSheet('background: pink; font-size: 15px')
        self.txt_next.setStyleSheet('background: red; font-size: 15px')
    def connects(self): 
        self.txt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    
app = QApplication([])
mw = MainWin()
app.exec_()
