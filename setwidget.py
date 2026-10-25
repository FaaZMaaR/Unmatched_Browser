from PyQt6 import QtCore, QtGui, QtWidgets
from herotable import HeroTable
from maptable import MapTable
from imagelabel import ImageLabel

class SetWidget(QtWidgets.QWidget):
    heroExploreClicked = QtCore.pyqtSignal(int)
    mapExploreClicked = QtCore.pyqtSignal(int)
    
    def __init__(self, database, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.umdata = database
        self.data = []
        
        self.comb_sets = QtWidgets.QComboBox(self)
        self.lb_release = QtWidgets.QLabel(self)
        self.lb_image = ImageLabel(self)
        self.heroTable = HeroTable(self)
        self.mapTable = MapTable(self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.comb_sets, 0, 0, 1, 2)
        grid.addWidget(self.lb_release, 1, 0)
        grid.addWidget(self.heroTable, 2, 0)
        grid.addWidget(self.mapTable, 3, 0)
        grid.addWidget(self.lb_image, 1, 1, 3, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)
        
        self.comb_sets.currentIndexChanged.connect(self.onSetChanged)
        self.heroTable.heroClicked.connect(self.onHeroClicked)
        self.mapTable.mapClicked.connect(self.onMapClicked)
        
        self.data = self.umdata.fetchSetData()
        for i in range(len(self.data)):
            self.comb_sets.addItem(self.data[i][1])
        self.select(0)
        
    def select(self, id):
        self.lb_release.setText(f"Дата выпуска: {self.getMonthString(self.data[id][2])} {self.data[id][3]}")
        self.lb_image.setImage(f"Images/Sets/{self.data[id][4]}.png", 400, 400)
        heroes = self.umdata.fetchSetHeroesData(id + 1)
        self.heroTable.setTable(heroes)
        maps = self.umdata.fetchSetMapsData(id + 1)
        self.mapTable.setTable(maps)
        
    def getMonthString(self, mon):
        if mon == 1:
            return "Январь"
        elif mon == 2:
            return "Февраль"
        elif mon == 3:
            return "Март"
        elif mon == 4:
            return "Апрель"
        elif mon == 5:
            return "Май"
        elif mon == 6:
            return "Июнь"
        elif mon == 7:
            return "Июль"
        elif mon == 8:
            return "Август"
        elif mon == 9:
            return "Сентябрь"
        elif mon == 10:
            return "Октябрь"
        elif mon == 11:
            return "Ноябрь"
        elif mon == 12:
            return "Декабрь"
        else:
            return ""
        
    def onSetChanged(self, index):
        self.select(index)
        
    def onHeroClicked(self, heroId):
        self.heroExploreClicked.emit(heroId)
        
    def onMapClicked(self, mapId):
        self.mapExploreClicked.emit(mapId)