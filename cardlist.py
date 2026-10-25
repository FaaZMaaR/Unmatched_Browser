from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel

class CardList(QtWidgets.QWidget):
    cardSelected = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.rows = 3
        self.cols = 6
        self.images = []
        self.titles = []
        for i in range(self.rows * self.cols):
            image = ImageLabel(self)
            image.clicked.connect(self.onImageClicked)
            image.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.images.append(image)
            self.titles.append(QtWidgets.QLabel(self))
            
        grid = QtWidgets.QGridLayout()
        for i in range(self.rows):
            for j in range(self.cols):
                grid.addWidget(self.images[j + self.cols * i], i * 2, j, QtCore.Qt.AlignmentFlag.AlignCenter)
                grid.addWidget(self.titles[j + self.cols * i], i * 2 + 1, j, QtCore.Qt.AlignmentFlag.AlignCenter)
                self.titles[j + self.cols * i].setWordWrap(True)
                self.titles[j + self.cols * i].setFixedHeight(50)
                self.titles[j + self.cols * i].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)
        
    def setCards(self, heroName, data):
        count = len(data)
        for i in range(count):
            self.titles[i].setText(f"{data[i][2]} x {data[i][1]}")
            self.images[i].id = data[i][0]
            self.images[i].setImage(f"Images/Heroes/{heroName}/{i + 1}.png", 180, 250)
            self.images[i].show()
        for i in range(count, self.rows * self.cols):
            self.titles[i].setText("")
            self.images[i].id = 0
            self.images[i].removeImage()
            self.images[i].hide()
            
    def onImageClicked(self, id):
        self.cardSelected.emit(id)