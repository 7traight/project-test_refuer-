from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from instr import*

class TestWin(QWidget):
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
    def start_timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()   
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        

    def initUI(self): 
        self.text_timer = QLabel('00:00:00')
        self.txt1 = QLabel(txt_name)
        self.line_name1 = QLineEdit(txt_hintname)
        self.txt2 = QLabel(txt_age)
        self.line_name2 = QLineEdit(txt_hintage)
        self.txt3 = QLabel(txt_test1)
        self.line_name3 = QLineEdit(txt_hinttest1)
        self.txt4 = QLabel(txt_test2)
        self.line_name4 = QLineEdit(txt_hinttest2)
        self.txt5 = QLabel(txt_test3)
        self.line_name5 = QLineEdit(txt_hinttest3)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt1)
        self.l_line.addWidget(self.line_name1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt2)
        self.l_line.addWidget(self.line_name2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt3)
        self.l_line.addWidget(self.line_name3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt4)
        self.l_line.addWidget(self.line_name5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt5)
        self.l_line.addWidget(self.line_name4, alignment = Qt.AlignLeft )

        self.l_line.addWidget(self.btn_test1)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line, 50)  
        self.h_line.addLayout(self.r_line, 50)
        self.setLayout(self.h_line)
    def connects(self): 
        ##################################################################################
        self.btn_test1.clicked.connect(self.start_timer1)
        #####################################################################################################################################
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    #def timer2Event(self):
    #global time
    #    time = time.addSecs(-1)
    #    self.text_timer.setText(time.toString("hh:mm:ss"))
    #    self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
    #    self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    #    if time.toString("hh:mm:ss") == "00:00:00":
    #        self.timer.stop()
    #self.text_timer.setText(time.toString("hh:mm:ss")[6:8])    
#


