from PyQt5.QtWidgets import*
from instr import *

txt_title = 'Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()# устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show() # старт
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
        pass
    def connects(self): 
        pass

    app = QApplication([])
    mw = MainWin()
    app.exec_()
