
import sys
import cv2
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        fnames = []

        self.listview = QListView()
        self.model = QStandardItemModel()


        path = QDir.rootPath()

        btn1 = QPushButton('Add File', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.openFile)

        btn2 = QPushButton('Del File', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.openFile)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(self.listview)
        vLayout.addWidget(btn1)
        vLayout.addWidget(btn2)

    def openFile(self):
        fnames = QFileDialog.getOpenFileNames(self, 'Open file','./', "Images (*.png *.jpg *.bmp)")
        for fname in fnames[0]:
            print(fname)
            self.model.appendRow(QStandardItem(fname))
            self.listview.setModel(self.model)

            #self.cvImage = cv2.imread(fname)
            #resizeImage = cv2.resize(self.cvImage, dsize=(self.width, self.height))
            #RGBImage = cv2.cvtColor(resizeImage, cv2.COLOR_BGR2RGB)
            #self.mQImage = QImage(RGBImage, self.width, self.height, RGBImage.strides[0], QImage.Format_RGB888)
            #self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())