from PyQt6 import QtCore, QtGui, QtWidgets

class ImageLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(int)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit(self.id)
    
    def __init__(self, parent = None):
        QtWidgets.QLabel.__init__(self, parent)
        self.id = 0
        
    def setImage(self, path, width = 0, height = 0):
        image = QtGui.QPixmap(path)
        if image.isNull():
            print(path)
        else:
            if width != 0 and height != 0:
                scaled = image.scaled(width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
                self.setPixmap(scaled)
                self.resize(scaled.width(), scaled.height())
            else:
                self.setPixmap(image)
                self.resize(image.width(), image.height())
            self.setStyleSheet("background-color: rgb(26, 22, 42);")
            
    def removeImage(self):
        image = QtGui.QPixmap()
        self.setPixmap(image)
        self.resize(image.width(), image.height())
        self.setStyleSheet("")