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
        self.table.insertColumn(self.table.columnCount())

    @QtCore.pyqtSlot()
    def on_btn_delete_column_clicked(self):
        self.table.removeColumn(self.table.columnCount() - 1)

    @QtCore.pyqtSlot()
    def on_btn_add_row_clicked(self):
        self.table.insertRow(self.table.rowCount())

    @QtCore.pyqtSlot()
    def on_btn_delete_row_clicked(self):
        self.table.removeRow(self.table.rowCount() - 1)

    def close(self):
        QtWidgets.QApplication.exit()

    @QtCore.pyqtSlot()
    def on_btn_create_csv_clicked(self):
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                print(self.table.item(row, column))
        csv_generator.CSVGenerator(self.table.item(0, 0))

def main():
    app = QtWidgets.QApplication([])
    PFG = MainUi()
    PFG.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
