# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import MainWindow
import PFGcreator

class MainUi (QtGui.QMainWindow, MainWindow.Ui_PFG):

    FreigabeArt = None
    def __init__(self):
        super(MainUi, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Produktfreigabe')
        self.createButton.clicked.connect(self.schreibePFG)
        self.radioButton.clicked.connect(self.changeFreigabe)
        self.radioButton_2.clicked.connect(self.changeFreigabe)
        self.radioButton_3.clicked.connect(self.changeFreigabe)
        self.radioButton_2.setChecked(True)
        self.lineEdit.setFocus()
        self.changeFreigabe()

    def changeFreigabe(self):
        if self.radioButton.isChecked():
            self.FreigabeArt = 'Vorserienfreigabe'
        if self.radioButton_2.isChecked():
            self.FreigabeArt = 'Serienfreigabe'
        if self.radioButton_3.isChecked():
            self.FreigabeArt = 'Prototypfreigabe'

    def schreibePFG(self):
        Produkt = str(self.lineEdit.text())
        PFGcreator.writeFile(self.FreigabeArt, Produkt)


def main():
    app = QtGui.QApplication(sys.argv)
    PFG = MainUi()
    PFG.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
