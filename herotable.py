from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel
from explorebutton import ExploreButton

class HeroTable(QtWidgets.QWidget):
    heroClicked = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.heroesCount = 4

        self.heroes = []
        for i in range(self.heroesCount):
            hero = [i, ImageLabel(self)]
            for j in range(4):
                hero.append(QtWidgets.QLabel(f"{i}{j}", self))
            explore = ExploreButton(self)
            explore.exploreClicked.connect(self.onHeroExploreClicked)
            hero.append(explore)
            hero[6].hide()
            self.heroes.append(hero)
        
        self.lb_heroTitle = QtWidgets.QLabel("Герой", self)
        self.lb_hpTitle = QtWidgets.QLabel("Стартовое здоровье", self)
        self.lb_moveTitle = QtWidgets.QLabel("Перемещение", self)
        self.lb_attackTitle = QtWidgets.QLabel("Атака", self)
        
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.lb_heroTitle, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_hpTitle, 0, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_moveTitle, 0, 3, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.lb_attackTitle, 0, 4, QtCore.Qt.AlignmentFlag.AlignCenter)
        for i in range(self.heroesCount):
            for j in range(1, len(self.heroes[0])):
                self.grid.addWidget(self.heroes[i][j], i + 1, j - 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.grid)
        
    def setTable(self, data):
        heroCount = len(data)
        for i in range(heroCount):
            self.heroes[i][0] = data[i][0]
            self.heroes[i][1].setImage(f"Images/Heroes/{data[i][1]}/back.png", 72, 100)
            for j in range(2, 6):
                self.heroes[i][j].setText(str(data[i][j]))
            self.heroes[i][6].show()
            self.heroes[i][6].id = data[i][0]
        rest = self.heroesCount - heroCount
        if rest > 0:
            for i in range(heroCount, self.heroesCount):
                self.heroes[i][0] = 0
                self.heroes[i][1].removeImage()
                for j in range(2, 6):
                    self.heroes[i][j].setText("")
                self.heroes[i][6].hide()
                
    def onHeroExploreClicked(self, heroId):
        self.heroClicked.emit(heroId)