from PyQt6 import QtCore, QtGui, QtWidgets
from imagelabel import ImageLabel

class CardInfo(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFixedWidth(350)
        
        self.lb_image = ImageLabel(self)
        self.lb_name = QtWidgets.QLabel(self)
        self.lb_typeValue = QtWidgets.QLabel(self)
        self.lb_banner = QtWidgets.QLabel(self)
        self.lb_boost = QtWidgets.QLabel(self)
        self.lb_mainEffect = QtWidgets.QLabel(self)
        self.lb_immediately = QtWidgets.QLabel(self)
        self.lb_duringCombat = QtWidgets.QLabel(self)
        self.lb_afterCombat = QtWidgets.QLabel(self)
        self.lb_heroCount = QtWidgets.QLabel(self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb_image, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.lb_typeValue, 1, 0, QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.lb_banner, 2, 0, QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.lb_boost, 2, 1, QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.lb_name, 3, 0, 1, 2)
        grid.addWidget(self.lb_mainEffect, 4, 0, 1, 2)
        grid.addWidget(self.lb_immediately, 5, 0, 1, 2)
        grid.addWidget(self.lb_duringCombat, 6, 0, 1, 2)
        grid.addWidget(self.lb_afterCombat, 7, 0, 1, 2)
        grid.addWidget(self.lb_heroCount, 8, 1, QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight)
        self.setLayout(grid)
        
        self.lb_name.setWordWrap(True)
        self.lb_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_mainEffect.setWordWrap(True)
        self.lb_immediately.setWordWrap(True)
        self.lb_duringCombat.setWordWrap(True)
        self.lb_afterCombat.setWordWrap(True)
        
    def setCard(self, data):
        self.lb_image.setImage(f"Images/Heroes/{data[11]}/{data[12]}.png", 216, 300)
        self.lb_typeValue.setText(f"  {data[2] if data[2] != None else "  "}  ")
        color = "black"
        if data[1] == "Прием":
            color = "gold"
        if data[1] == "Атака":
            color = "red"
        if data[1] == "Защита":
            color = "dodgerBlue"
        if data[1] == "Универсальная":
            color = "blueViolet"
        self.lb_typeValue.setStyleSheet(f"background-color: {color}; color: white; font-size: 14pt; font-weight: bold;")
        self.lb_banner.setText(data[3])
        self.lb_boost.setText(f"{data[4] if data[4] != None else "  "}")
        self.lb_boost.setStyleSheet("background-color: black; color: white; font-size: 14pt; font-weight: bold; border: 2px solid black; border-radius: 12px 12px 12px 12px;")
        self.lb_name.setText(data[0])
        self.lb_mainEffect.setText(data[5] if data[5] != None else "")
        self.lb_immediately.setText(f"НЕМЕДЛЕННО: {data[6]}" if data[6] != None else "")
        self.lb_duringCombat.setText(f"ВО ВРЕМЯ БОЯ: {data[7]}" if data[7] != None else "")
        self.lb_afterCombat.setText(f"ПОСЛЕ БОЯ: {data[8]}" if data[8] != None else "")
        self.lb_heroCount.setText(f"{data[9]} | x{data[10]}")