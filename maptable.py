from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel
from explorebutton import ExploreButton

class MapTable(QtWidgets.QWidget):
    mapClicked = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.maps = []
        for i in range(2):
            map = [i, ImageLabel(self)]
            for j in range(4):
                map.append(QtWidgets.QLabel(f"{i}{j}", self))
            explore = ExploreButton(self)
            explore.exploreClicked.connect(self.onMapExploreClicked)
            map.append(explore)
            map[6].hide()
            self.maps.append(map)
        
        self.lb_mapTitle = QtWidgets.QLabel("Поле", self)
        self.lb_startTitle = QtWidgets.QLabel("Количество стартовых ячеек", self)
        self.lb_zoneTitle = QtWidgets.QLabel("Количество зон", self)
        self.lb_spaceTitle = QtWidgets.QLabel("Количество ячеек", self)
                
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.lb_mapTitle, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_startTitle, 0, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_zoneTitle, 0, 3, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_spaceTitle, 0, 4, QtCore.Qt.AlignmentFlag.AlignCenter)
        for i in range(len(self.maps)):
            for j in range(1, len(self.maps[0])):
                self.grid.addWidget(self.maps[i][j], i + 1, j - 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.grid)
        
    def setTable(self, data):
        mapCount = len(data)
        for i in range(mapCount):
            self.maps[i][0] = data[i][0]
            self.maps[i][1].setImage(f"Images/Maps/{data[i][1]}.png", 108, 70)
            for j in range(2, 6):
                self.maps[i][j].setText(str(data[i][j]))
            self.maps[i][6].show()
            self.maps[i][6].id = data[i][0]
        rest = len(self.maps) - mapCount
        if rest > 0:
            for i in range(mapCount, len(self.maps)):
                self.maps[i][0] = 0
                self.maps[i][1].removeImage()
                for j in range(2, 6):
                    self.maps[i][j].setText("")
                self.maps[i][6].hide()
                
    def onMapExploreClicked(self, mapId):
        self.mapClicked.emit(mapId)