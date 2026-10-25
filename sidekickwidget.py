from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel

class SidekickWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.lb_title = QtWidgets.QLabel(self)
        self.lb_chars = QtWidgets.QLabel(self)
        self.images = []
        for i in range(4):
            self.images.append(ImageLabel(self))
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb_title, 0, 0, 1, 4)
        for i in range(len(self.images)):
            grid.addWidget(self.images[i], 1, i, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_chars, 2, 0, 1, 4)
        self.setLayout(grid)
        
        self.lb_chars.setWordWrap(True)
        
    def setSidekick(self, data):
        if len(data) == 0:
            self.lb_title.setText("Помощник: Нет")
            self.lb_chars.setText("")
            for i in range(len(self.images)):
                self.images[i].removeImage()
        else:
            self.lb_title.setText(f"Помощник: {data[0][0]}")
            self.lb_chars.setText(f"Характеристики:\nАтака: {data[0][4]}\nСтартовое здоровье: {data[0][1]}")
            if data[0][2] < 2:
                self.images[0].setImage(f"Images/Sidekicks/{data[0][3]}.png", 64, 64)
            else:
                for i in range(data[0][2]):
                    self.images[i].setImage(f"Images/Sidekicks/{data[0][3]}_{i + 1}.png", 64, 64)
            for i in range(data[0][2], len(self.images)):
                self.images[i].removeImage()