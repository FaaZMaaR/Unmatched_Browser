from PyQt6 import QtCore, QtGui, QtWidgets
from cardinfo import CardInfo

class CardWidget(QtWidgets.QWidget):
    def __init__(self, database, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.umdata = database
        self.data = []
        self.idData = {}
        
        self.table_cards = QtWidgets.QTableWidget(0, 7, self)
        self.wgt_cardInfo = CardInfo(self)
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.table_cards)
        hbox.addWidget(self.wgt_cardInfo)
        self.setLayout(hbox)
        
        headers = ["id", "Название", "Тип", "Значение", "Усиление", "Герой", "Количество"]
        self.table_cards.setHorizontalHeaderLabels(headers)
        
        self.table_cards.hideColumn(0)
        self.table_cards.setSelectionBehavior(self.table_cards.SelectionBehavior.SelectRows)
        
        self.table_cards.currentCellChanged.connect(self.onRowSelected)
        self.fillTable()
        
    def fillTable(self):
        cards = self.umdata.fetchCardData()
        self.table_cards.setRowCount(0)
        for row in range(len(cards)):
            if cards[row][0] == None:
                continue
            self.idData[cards[row][0]] = row
            self.table_cards.insertRow(row)
            for col in range(len(cards[row])):
                self.table_cards.setItem(row, col, QtWidgets.QTableWidgetItem(str(cards[row][col])))
        self.table_cards.resizeColumnsToContents()
        
    def onRowSelected(self, row, col, prevRow, prevCol):
        self.wgt_cardInfo.setCard(self.umdata.fetchCardInfoData(self.table_cards.item(row, 0).text()))