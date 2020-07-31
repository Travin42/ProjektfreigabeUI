import sys
from PyQt5 import QtGui, QtCore, QtWidgets

from JiraTicketGenerator import JiraTicketGenerationUI
from JiraTicketGenerator.utils import csv_generator

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

    def close(self):
        QtWidgets.QApplication.exit()

    @QtCore.pyqtSlot()
    def on_btn_create_csv_clicked(self):
        data = QtCore.QMimeData()
        self.table.items(data)
        print(data)
        csv_generator.CSVGenerator(self.table.item(0, 0))

def main():
    app = QtWidgets.QApplication([])
    PFG = MainUi()
    PFG.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
