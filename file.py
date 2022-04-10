from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

my_programm = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('испытай везение!')
main_win.resize(400, 400)
main_win.setStyleSheet("background: #cc66ff; color: #800000; font-size: 100px")

btn1 = QLabel('Python')
btn2 = QLabel('PHP')
btn3 = QLabel('Java')
btn4 = QLabel('C++')
btn5 = QLabel('C')
btn6 = QLabel('Pascal')

layot_main = QVBoxLayout()

line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()

line_h1.addWidget(btn1, alignment= Qt.AlignCenter)
line_h1.addWidget(btn2, alignment= Qt.AlignCenter)

line_h2.addWidget(btn3, alignment= Qt.AlignCenter)
line_h2.addWidget(btn6, alignment= Qt.AlignCenter)

line_h3.addWidget(btn4, alignment= Qt.AlignCenter)
line_h3.addWidget(btn5, alignment= Qt.AlignCenter)

layot_main.addLayout(line_h1)
layot_main.addLayout(line_h2)
layot_main.addLayout(line_h3)

main_win.setLayout(layot_main)
main_win.show()
my_programm.exec_()