from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel

class MapWidget(QtWidgets.QWidget):
    def __init__(self, database, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.umdata = database
        self.data = []
        self.idData = {}
        
        self.comb_maps = QtWidgets.QComboBox(self)
        self.lb_set = QtWidgets.QLabel(self)
        self.lb_startSpacesTitle = QtWidgets.QLabel("Количество стартовых ячеек", self)
        self.lb_zonesTitle = QtWidgets.QLabel("Количество зон", self)
        self.lb_spacesTitle = QtWidgets.QLabel("Количество ячеек", self)
        self.lb_startSpaces = QtWidgets.QLabel(self)
        self.lb_zones = QtWidgets.QLabel(self)
        self.lb_spaces = QtWidgets.QLabel(self)
        self.lb_image = ImageLabel(self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.comb_maps, 0, 0, 1, 4)
        grid.addWidget(self.lb_startSpacesTitle, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_zonesTitle, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_spacesTitle, 1, 3, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_set, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_startSpaces, 2, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_zones, 2, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_spaces, 2, 3, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_image, 3, 0, 1, 4, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)
        
        self.lb_startSpacesTitle.setWordWrap(True)
        self.lb_startSpacesTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_zonesTitle.setWordWrap(True)
        self.lb_spacesTitle.setWordWrap(True)
        
        self.data = self.umdata.fetchMapData()
        for i in range(len(self.data)):
            self.comb_maps.addItem(self.data[i][1])
            self.idData[self.data[i][0]] = i

        self.comb_maps.currentIndexChanged.connect(self.onMapChanged)
        self.onMapChanged(0)
        
    def onMapChanged(self, index):
        self.lb_set.setText(self.data[index][6])
        self.lb_startSpaces.setText(str(self.data[index][2]))
        self.lb_zones.setText(str(self.data[index][3]))
        self.lb_spaces.setText(str(self.data[index][4]))
        self.lb_image.setImage(f"Images/Maps/{self.data[index][5]}.png", 924, 600)