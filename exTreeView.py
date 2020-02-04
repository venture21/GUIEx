from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class TreeDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)

        #타이틀은 Dialog Tree
        self.setWindowTitle("Dialog Tree")

        #QTreeView를 사용
        self.mainTree = QTreeView()

        model = QFileSystemModel()
        model.setRootPath('')
        self.mainTree.setModel(model)

        layout = QGridLayout()
        layout.addWidget(self.mainTree)
        self.setLayout(layout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    dialog = TreeDialog()
    dialog.show()
    sys.exit(app.exec_())
