from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from instr import*

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
    def start_timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()   
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def start_timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()   
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def start_timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()   
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def initUI(self): 
        self.text_timer1 = QLabel('00:00:00')
        self.txt1 = QLabel(txt_name)

        self.text_timer2 = QLabel('00:00:00')
        self.txt1 = QLabel(txt_name)

        self.text_timer3 = QLabel('00:00:00')
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
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.txt_next = QPushButton(txt_next)
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

        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer1, alignment = Qt.AlignRight)
        self.r_line.addWidget(self.text_timer2, alignment = Qt.AlignRight)
        self.r_line.addWidget(self.text_timer3, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.txt_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line, 50)  

        self.h_line.addLayout(self.r_line, 50)
        self.setLayout(self.h_line)
    def connects(self): 
        ##################################################################################
        self.btn_test1.clicked.connect(self.start_timer1)
        self.btn_test2.clicked.connect(self.start_timer2)
        self.btn_test3.clicked.connect(self.start_timer3)
        self.txt_next.clicked.connect(self.next_click)
        #####################################################################################################################################
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer1.setText(time.toString("hh:mm:ss"))
        self.text_timer1.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer1.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer2.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer2.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer2.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer3.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer3.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer3.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer3.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        
    def next_click(self):
        self.hide()
        self.mw = FinalWin()

app = QApplication([])
mw = MainWin()
app.exec_()
