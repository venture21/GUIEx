## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def changeEnable(self):
        if self.btn1.isChecked():
            self.btn3.setEnabled(True)
            self.btn3.setText('Enable')
        else:
            self.btn3.setDisabled(True)
            self.btn3.setText('Disable')

    def initUI(self):
        self.btn1 = QPushButton('&Button1', self)
        self.btn1.setCheckable(True)
        self.btn1.toggle()

        self.btn2 = QPushButton(self)
        self.btn2.setText('Button&2')

        self.btn3 = QPushButton('Button3', self)
        self.btn3.setEnabled(False)

        self.btn1.clicked.connect(self.changeEnable)


        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())