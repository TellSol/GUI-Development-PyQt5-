# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HavfiskCatalog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    
    # STRUCTURE OF GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Nordtind = QtWidgets.QPushButton(self.centralwidget)
        self.Nordtind.setGeometry(QtCore.QRect(20, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Nordtind.setFont(font)
        self.Nordtind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nordtind.setTabletTracking(False)
        self.Nordtind.setObjectName("Nordtind")
        self.Vesttind = QtWidgets.QPushButton(self.centralwidget)
        self.Vesttind.setGeometry(QtCore.QRect(220, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Vesttind.setFont(font)
        self.Vesttind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Vesttind.setObjectName("Vesttind")
        self.Havtind = QtWidgets.QPushButton(self.centralwidget)
        self.Havtind.setGeometry(QtCore.QRect(420, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Havtind.setFont(font)
        self.Havtind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Havtind.setObjectName("Havtind")
        self.Baatsfjord = QtWidgets.QPushButton(self.centralwidget)
        self.Baatsfjord.setGeometry(QtCore.QRect(620, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Baatsfjord.setFont(font)
        self.Baatsfjord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Baatsfjord.setObjectName("Baatsfjord")
        self.Doggi = QtWidgets.QPushButton(self.centralwidget)
        self.Doggi.setGeometry(QtCore.QRect(820, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Doggi.setFont(font)
        self.Doggi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Doggi.setObjectName("Doggi")
        self.GadusPoseidon = QtWidgets.QPushButton(self.centralwidget)
        self.GadusPoseidon.setGeometry(QtCore.QRect(20, 300, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.GadusPoseidon.setFont(font)
        self.GadusPoseidon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GadusPoseidon.setObjectName("GadusPoseidon")
        self.GadusNeptun = QtWidgets.QPushButton(self.centralwidget)
        self.GadusNeptun.setGeometry(QtCore.QRect(220, 300, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.GadusNeptun.setFont(font)
        self.GadusNeptun.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GadusNeptun.setObjectName("GadusNeptun")
        self.GadusNjord = QtWidgets.QPushButton(self.centralwidget)
        self.GadusNjord.setGeometry(QtCore.QRect(420, 300, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.GadusNjord.setFont(font)
        self.GadusNjord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GadusNjord.setObjectName("GadusNjord")
        self.Rypefjord = QtWidgets.QPushButton(self.centralwidget)
        self.Rypefjord.setGeometry(QtCore.QRect(620, 300, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Rypefjord.setFont(font)
        self.Rypefjord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rypefjord.setObjectName("Rypefjord")
        self.Kongsfjord = QtWidgets.QPushButton(self.centralwidget)
        self.Kongsfjord.setGeometry(QtCore.QRect(820, 300, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Kongsfjord.setFont(font)
        self.Kongsfjord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Kongsfjord.setObjectName("Kongsfjord")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(190, 10, 711, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Header.setFont(font)
        self.Header.setObjectName("Header")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(360, 170, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setObjectName("description")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Nordtind.clicked.connect(self.popUp)
        

    # TRANSLATIONS OF NAMES IN GUI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leroy Havfisk - Fleet Catalog"))
        self.Nordtind.setText(_translate("MainWindow", "Nordtind"))
        self.Vesttind.setText(_translate("MainWindow", "Vesttind"))
        self.Havtind.setText(_translate("MainWindow", "Havtind"))
        self.Baatsfjord.setText(_translate("MainWindow", "Baatsfjord"))
        self.Doggi.setText(_translate("MainWindow", "Doggi"))
        self.GadusPoseidon.setText(_translate("MainWindow", "Gadus Poseidon"))
        self.GadusNeptun.setText(_translate("MainWindow", "Gadus Neptun"))
        self.GadusNjord.setText(_translate("MainWindow", "Gadus Njord"))
        self.Rypefjord.setText(_translate("MainWindow", "Rypefjord"))
        self.Kongsfjord.setText(_translate("MainWindow", "Kongsfjord"))
        self.Header.setText(_translate("MainWindow", "Leroy Havfisk Fleet"))
        self.description.setText(_translate("MainWindow", "Click on vessel to see details"))
        
    
    # CRATE POPUPS WHEN CLICKING ON A VESSEL
    def popUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Nordtind picture page")
        msg.setText("Picture of Nortind goes here!")
        x = msg.exec_()

    

# APPLICATION INITIALIZATION AND RUNTIME
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
