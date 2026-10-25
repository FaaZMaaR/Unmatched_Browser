from PyQt6 import QtCore, QtGui, QtWidgets
from setwidget import SetWidget
from herowidget import HeroWidget
from mapwidget import MapWidget
from cardwidget import CardWidget
from data import UnmatchedData

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent, flags = QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Unmatched Browser")
        self.setFixedSize(1200, 800)
        
        self.umdata = UnmatchedData("unmatched.db")
        
        self.wgt_set = SetWidget(self.umdata, self)
        self.wgt_hero = HeroWidget(self.umdata, self)
        self.wgt_map = MapWidget(self.umdata, self)
        self.wgt_card = CardWidget(self.umdata, self)
        
        self.scroll_hero = QtWidgets.QScrollArea(self)
        self.scroll_hero.setWidget(self.wgt_hero)
        self.scroll_hero.setWidgetResizable(True)
        
        menuBar = self.menuBar()
        
        menuApp = menuBar.addMenu("Приложение")
        action = menuApp.addAction("О приложении", self.aboutApp)
        action.setStatusTip("Получение сведений о приложении")
        menuApp.addSeparator()
        action = menuApp.addAction("Выход", QtGui.QKeySequence("Ctrl+Q"), QtWidgets.QApplication.instance().quit)
        action.setStatusTip("Завершение работы приложения")
        
        self.tab = QtWidgets.QTabWidget(self)
        self.tab.addTab(self.wgt_set, "Наборы")
        self.tab.addTab(self.scroll_hero, "Герои")
        self.tab.addTab(self.wgt_map, "Поля")
        self.tab.addTab(self.wgt_card, "Карты")
        
        mainWidget = QtWidgets.QWidget(self)
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        vbox.addWidget(self.tab)
        hbox.addLayout(vbox)
        mainWidget.setLayout(hbox)
        
        self.setCentralWidget(mainWidget)
        
        self.wgt_set.heroExploreClicked.connect(self.onHeroExploreClicked)
        self.wgt_set.mapExploreClicked.connect(self.onMapExploreClicked)
        self.wgt_hero.wgt_cardList.cardSelected.connect(self.onCardSelected)
        
    def aboutApp(self):
        QtWidgets.QMessageBox.about(self, "О приложении", 
                                    """<center>\"Unmatched Browser\" v1.0.0
                                    <br><br>Приложение Unmatched Browser позволяет просматривать информацию о наборах, героях и картах из настольной игры Unmatched<sup>TM</sup>.
                                    <br><br>(c) Restoration Games, 2026<br>(c) FaaZMaaR, 2026""")
        
    def onHeroExploreClicked(self, heroId):
        self.wgt_hero.comb_heroes.setCurrentIndex(self.wgt_hero.idData[heroId])
        self.tab.setCurrentIndex(1)
        
    def onMapExploreClicked(self, mapId):
        self.wgt_map.comb_maps.setCurrentIndex(self.wgt_map.idData[mapId])
        self.tab.setCurrentIndex(2)
        
    def onCardSelected(self, cardId):
        self.wgt_card.table_cards.setCurrentCell(self.wgt_card.idData[cardId], 0)
        self.tab.setCurrentIndex(3)