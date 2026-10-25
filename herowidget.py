from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel
from sidekickwidget import SidekickWidget
from cardlist import CardList

class HeroWidget(QtWidgets.QWidget):
    def __init__(self, database, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.umdata = database
        self.data = []
        self.idData = {}
        
        self.comb_heroes = QtWidgets.QComboBox(self)
        self.lb_set = QtWidgets.QLabel(self)
        self.lb_ability = QtWidgets.QLabel(self)
        self.figureImages = []
        for i in range(3):
            self.figureImages.append(ImageLabel(self))
        self.lb_backImage = ImageLabel(self)
        self.lb_chars = QtWidgets.QLabel(self)
        self.wgt_sidekick = SidekickWidget(self)
        self.wgt_cardList = CardList(self)
                
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.comb_heroes, 0, 0, 1, 4)
        grid.addWidget(self.lb_set, 1, 0, 1, 4)
        grid.addWidget(self.lb_backImage, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        for i in range(len(self.figureImages)):
            grid.addWidget(self.figureImages[i], 2, i + 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_ability, 3, 0, 2, 2)
        grid.addWidget(self.lb_chars, 3, 2, 1, 2)
        grid.addWidget(self.wgt_sidekick, 4, 2, 1, 2)
        grid.addWidget(self.wgt_cardList, 5, 0, 1, 4)
        self.setLayout(grid)
        
        self.lb_ability.setWordWrap(True)
        self.lb_chars.setWordWrap(True)
        self.data = self.umdata.fetchHeroData()
        for i in range(len(self.data)):
            self.comb_heroes.addItem(self.data[i][1])
            self.idData[self.data[i][0]] = i
        
        self.comb_heroes.currentIndexChanged.connect(self.onHeroChanged)
        self.onHeroChanged(0)
        
    def onHeroChanged(self, index):
        self.lb_set.setText(self.data[index][8])
        self.lb_backImage.setImage(f"Images/Heroes/{self.data[index][6]}/back.png", 216, 300)
        if self.data[index][4] < 2:
            self.figureImages[0].setImage(f"Images/Heroes/{self.data[index][6]}/figure.png", 216, 300)
        else:
            for i in range(self.data[index][4]):
                self.figureImages[i].setImage(f"Images/Heroes/{self.data[index][6]}/figure_{i + 1}.png", 216, 300)
        for i in range(self.data[index][4], len(self.figureImages)):
            self.figureImages[i].removeImage()
        self.lb_ability.setText(self.data[index][5])
        self.lb_chars.setText(f"Характеристики:\nАтака: {self.data[index][7]}\nСтартовое здоровье: {self.data[index][2]}\nПеремещение: {self.data[index][3]}")
        sidekick = self.umdata.fetchHeroSidekickData(self.data[index][0])
        self.wgt_sidekick.setSidekick(sidekick)
        cards = self.umdata.fetchHeroCardsData(self.data[index][0])
        self.wgt_cardList.setCards(self.data[index][6], cards)