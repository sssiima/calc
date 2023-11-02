from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import numexpr as ne
import sys
import logging


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calc")
        self.resize(635, 725)
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
        logging.info("Archive")

        self.btnc = QPushButton("C", self)
        self.btnc.setGeometry(10, 200, 150, 100)
        self.btnc.setStyleSheet("font: 40pt; color: #f1efff; background-color: #7166c6")
        self.btnc.clicked.connect(self.enter)
        self.btnpm = QPushButton("+/-", self)
        self.btnpm.setGeometry(165, 200, 150, 100)
        self.btnpm.setStyleSheet("font: 40pt; color: #f1efff; background-color: #7166c6")
        self.btnpm.clicked.connect(self.enter)
        self.btnsqrt = QPushButton("^", self)
        self.btnsqrt.setGeometry(320, 200, 150, 100)
        self.btnsqrt.setStyleSheet("font: 40pt; color: #f1efff; background-color: #7166c6")
        self.btnsqrt.clicked.connect(self.enter)
        self.btndel = QPushButton("/", self)
        self.btndel.setGeometry(475, 200, 150, 100)
        self.btndel.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btndel.clicked.connect(self.enter)

        self.btn1 = QPushButton("1", self)
        self.btn1.setGeometry(10, 305, 150, 100)
        self.btn1.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn1.clicked.connect(self.enter)
        self.btn2 = QPushButton("2", self)
        self.btn2.setGeometry(165, 305, 150, 100)
        self.btn2.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn2.clicked.connect(self.enter)
        self.btn3 = QPushButton("3", self)
        self.btn3.setGeometry(320, 305, 150, 100)
        self.btn3.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn3.clicked.connect(self.enter)
        self.btnmul = QPushButton("x", self)
        self.btnmul.setGeometry(475, 305, 150, 100)
        self.btnmul.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btnmul.clicked.connect(self.enter)

        self.btn4 = QPushButton("4", self)
        self.btn4.setGeometry(10, 410, 150, 100)
        self.btn4.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn4.clicked.connect(self.enter)
        self.btn5 = QPushButton("5", self)
        self.btn5.setGeometry(165, 410, 150, 100)
        self.btn5.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn5.clicked.connect(self.enter)
        self.btn6 = QPushButton("6", self)
        self.btn6.setGeometry(320, 410, 150, 100)
        self.btn6.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn6.clicked.connect(self.enter)
        self.btnmin = QPushButton("-", self)
        self.btnmin.setGeometry(475, 410, 150, 100)
        self.btnmin.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btnmin.clicked.connect(self.enter)

        self.btn7 = QPushButton("7", self)
        self.btn7.setGeometry(10, 515, 150, 100)
        self.btn7.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn7.clicked.connect(self.enter)
        self.btn8 = QPushButton("8", self)
        self.btn8.setGeometry(165, 515, 150, 100)
        self.btn8.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn8.clicked.connect(self.enter)
        self.btn9 = QPushButton("9", self)
        self.btn9.setGeometry(320, 515, 150, 100)
        self.btn9.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn9.clicked.connect(self.enter)
        self.btnplus = QPushButton("+", self)
        self.btnplus.setGeometry(475, 515, 150, 100)
        self.btnplus.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btnplus.clicked.connect(self.enter)

        self.btn0 = QPushButton("0", self)
        self.btn0.setGeometry(10, 620, 305, 100)
        self.btn0.setStyleSheet("font: 40pt; color: #7166c6; background-color: #f1efff")
        self.btn0.clicked.connect(self.enter)
        self.btndot = QPushButton(".", self)
        self.btndot.setGeometry(320, 620, 150, 100)
        self.btndot.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btndot.clicked.connect(self.enter)
        self.btneq = QPushButton("=", self)
        self.btneq.setGeometry(475, 620, 150, 100)
        self.btneq.setStyleSheet("font: 46pt; color: #7166c6; background-color: #b2abe8")
        self.btneq.clicked.connect(self.equality)

        self.text = QLineEdit(self)
        self.text.setGeometry(10, 50, 615, 100)
        font = self.text.font()
        font.setPointSize(56)
        self.text.setFont(font)
        rx = QRegExp("[0-9-+/^*()]{17}")
        val = QRegExpValidator(rx)
        self.text.setValidator(val)

    def equality(self):
        con = self.text.text()
        try:
            if '^' in self.text.text():
                res = str(ne.evaluate(self.text.text().replace("^", "**")))
                self.text.setText(res)
            else:
                res = str(ne.evaluate(self.text.text()))
                self.text.setText(res)
        except SyntaxError:
            res = "Error"
            self.text.setText("")
        if ".0" in self.text.text():
            res = self.text.text()[:-2]
            self.text.setText(res)
        logging.info(con + "=" + res)

    def enter(self):
        btn = self.sender()
        if "C" in btn.text():
            self.text.setText("")
        elif "x" in btn.text():
            self.text.setText(self.text.text() + "*")
        elif "+/-" in btn.text():
            if self.text.text().startswith("-"):
                self.text.setText(self.text.text()[1:])
            else:
                self.text.setText("-" + self.text.text())
        else:
            self.text.setText(self.text.text() + btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())