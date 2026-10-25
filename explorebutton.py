from PyQt6 import QtCore, QtGui, QtWidgets

class ExploreButton(QtWidgets.QPushButton):
    exploreClicked = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        QtWidgets.QPushButton.__init__(self, parent)
        self.id = 0
        self.setText("Просмотр")
        self.clicked.connect(self.onClicked)
        
    def onClicked(self):
        self.exploreClicked.emit(self.id)