import sys
from PyQt5 import QtGui, QtCore, QtWidgets

from JiraTicketGenerator import JiraTicketGenerationUI
from JiraTicketGenerator.csv_generator import csv_generator as CSV_Generator

class MainUi (QtWidgets.QMainWindow, JiraTicketGenerationUI.Ui_PFG):

    FreigabeArt = None
    def __init__(self):
        super(MainUi, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('CSV Creator for TFS')
        # Exit menu
        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

    def changeFreigabe(self):
        if self.radioButton.isChecked():
            self.FreigabeArt = 'Vorserienfreigabe'
        if self.radioButton_2.isChecked():
            self.FreigabeArt = 'Serienfreigabe'
        if self.radioButton_3.isChecked():
            self.FreigabeArt = 'Prototypfreigabe'

    @QtCore.pyqtSlot()
    def on_btn_add_column_clicked(self):
        self.addColumn()

    @QtCore.pyqtSlot()
    def on_btn_delete_column_clicked(self):
        self.deleteColumn()

    @QtCore.pyqtSlot()
    def on_btn_add_row_clicked(self):
        self.addRow()

    @QtCore.pyqtSlot()
    def on_btn_delete_row_clicked(self):
        self.deleteRow()

    def addColumn(self):
        column_count = self.table.columnCount()
        column_count += 1
        self.table.setColumnCount(column_count)

    def deleteColumn(self):
        column_count = self.table.columnCount()
        column_count -= 1
        self.table.setColumnCount(column_count)

    def addRow(self):
        row_count = self.table.rowCount()
        row_count += 1
        self.table.setRowCount(row_count)

    def deleteRow(self):
        row_count = self.table.rowCount()
        row_count -= 1
        self.table.setRowCount(row_count)

    @QtCore.pyqtSlot()
    def close(self):
        QtWidgets.QApplication.exit()

def main():
    app = QtWidgets.QApplication([])
    PFG = MainUi()
    PFG.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
