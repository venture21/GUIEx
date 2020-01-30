import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QTime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 메인 타이머
        self.timer1 = QTimer(self)  # 타이머 객체 생성
        self.timer1.start(1000 * 1)  # 1초마다 타이머 실행, 시작
        self.timer1.timeout.connect(self.timeout)  # 슬롯 timeout() 객체 호출

        self.timer2 = QTimer(self)
        self.timer2.start(1000 * 2)
        self.timer2.timeout.connect(self.timeout)

    def timeout(self):
        # 타임아웃 이벤트가 발생하면 호출되는 메서드
        # 어떤 타이머에 의해서 호출되었는지 확인
        sender = self.sender()

        currentTime = QTime.currentTime().toString("hh:mm:ss")

        if id(sender) == id(self.timer1):
            print("timer1 호출 -->", currentTime)

        if id(sender) == id(self.timer2):
            print("timer2 호출 -->", currentTime)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    sys.exit(app.exec_())