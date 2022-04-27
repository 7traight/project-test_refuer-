from PyQt5.QtWidgets import*
from instr import *
from PyQt5.QtCore import *

class FinalWin(QWidget):
    def __init__(self, age, test1, test2, test3):
        super().__init__()
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.set_appear()
        self.results()
        self.initUI()
        self.connects()
        self.show()
    def results(self):
        self.index = (4*(int(self.test1)+int(self.test2)+int(self.test3))- 200) / 10
        if self.age == 7 or self.age == 8:
            if self.index <= 6.4:
                self.resultTest = txt_res5
            elif self.index >= 6.5 and self.index <= 11.9:
                self.resultTest = txt_res4
            elif self.index >= 12 and self.index <= 16.9:
                self.resultTest = txt_res3
            elif self.index >= 17 and self.index <= 20.9:
                self.resultTest = txt_res2
            elif self.index >= 21:
                self.resultTest = txt_res1
        elif self.age == 9 or self.age == 10:
            if self.index <= 4.9:
                self.resultTest = txt_res5
            elif self.index >= 5 and self.index <= 10.4:
                self.resultTest = txt_res4
            elif self.index >= 10.5 and self.index <= 15.4:
                self.resultTest = txt_res3
            elif self.index >= 15.5 and self.index <= 19.4:
                self.resultTest = txt_res2
            elif self.index >= 19.5:
                self.resultTest = txt_res1
        elif self.age == 11 or self.age == 12:
            if self.index <= 3.4:
                self.resultTest = txt_res5
            elif self.index >= 3.5 and self.index <= 8.9:
                self.resultTest = txt_res4
            elif self.index >= 9 and self.index <= 13.9:
                self.resultTest = txt_res3
            elif self.index >= 14 and self.index <= 17.9:
                self.resultTest = txt_res2
            elif self.index >= 18:
                self.resultTest = txt_res1
        elif self.age == 13 or self.age == 14:
            if self.index <= 1.9:
                self.resultTest = txt_res5
            elif self.index >= 2 and self.index <= 7.4:
                self.resultTest = txt_res4
            elif self.index >= 7.5 and self.index <= 12.4:
                self.resultTest = txt_res3
            elif self.index >= 12.5 and self.index <= 16.4:
                self.resultTest = txt_res2
            elif self.index >= 18:
                self.resultTest = txt_res1
        elif self.age >= 15:
            if self.inidex <= 0.4:
                self.resultTest = txt_res5
            elif self.index >= 0.5 and self.index <= 5.9:
                self.resultTest = txt_res4
            elif self.index >= 6 and self.index <= 10.9:
                self.resultTest = txt_res3
            elif self.index >= 11 and self.index <= 14.9:
                self.resultTest = txt_res2
            elif self.index >= 15:
                self.resultTest = txt_res1
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.Layout = QVBoxLayout()
        self.yourIndex = QLabel(txt_index + str(self.index))
        self.yourResults = QLabel(txt_workheart + self.resultTest)
        self.Layout.addWidget(self.yourIndex, alignment= Qt.AlignCenter)
        self.Layout.addWidget(self.yourResults, alignment= Qt.AlignCenter)
        self.setLayout(self.Layout)
        self.setStyleSheet('background: pink;')
    def connects(self):
        pass