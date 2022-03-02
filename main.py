import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/calculator.ui')[0] # ui 불러오기

class Calculator(QMainWindow, form_class):
    def __init__(self): # 초기화자
        super().__init__()
        self.setupUi(self) # 만들어 놓은 test.ui 연결
        self.setWindowTitle('계산기') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/calcu.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Calculator Ver 1.0') # 윈도우 상태표시줄 입력
        self.num1_button.clicked.connect(self.num1_output)
        self.num2_button.clicked.connect(self.num2_output)
        self.num3_button.clicked.connect(self.num3_output)
        self.num4_button.clicked.connect(self.num4_output)
        self.num5_button.clicked.connect(self.num5_output)
        self.num6_button.clicked.connect(self.num6_output)
        self.num7_button.clicked.connect(self.num7_output)
        self.num8_button.clicked.connect(self.num8_output)
        self.num9_button.clicked.connect(self.num9_output)
        self.num0_button.clicked.connect(self.num0_output)
        self.plus_button.clicked.connect(self.plus_output)
        self.minus_button.clicked.connect(self.minus_output)
        self.mul_button.clicked.connect(self.mul_output)
        self.div_button.clicked.connect(self.div_output)
        self.reset_button.clicked.connect(self.reset)
        self.result_button.clicked.connect(self.result_output)


    def num1_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '1'
        self.result_label.setText(label_value)

    def num2_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '2'
        self.result_label.setText(label_value)

    def num3_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '3'
        self.result_label.setText(label_value)

    def num4_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '4'
        self.result_label.setText(label_value)

    def num5_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '5'
        self.result_label.setText(label_value)

    def num6_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '6'
        self.result_label.setText(label_value)

    def num7_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '7'
        self.result_label.setText(label_value)

    def num8_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '8'
        self.result_label.setText(label_value)

    def num9_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '9'
        self.result_label.setText(label_value)

    def num0_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '0'
        self.result_label.setText(label_value)

    def plus_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '+'
        self.result_label.setText(label_value)

    def minus_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '-'
        self.result_label.setText(label_value)

    def mul_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '*'
        self.result_label.setText(label_value)

    def div_output(self):
        label_value = self.result_label.text()
        label_value = label_value + '/'
        self.result_label.setText(label_value)

    def reset(self):
        self.result_label.clear()

    def result_output(self):
        label_value = self.result_label.text()
        ret = eval(label_value)
        cal_result = f"{label_value}={ret}"
        self.result_label.setText(cal_result)








app = QApplication(sys.argv)
window = Calculator()
window.show()
app.exec_()