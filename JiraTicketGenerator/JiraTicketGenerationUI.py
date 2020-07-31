from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_PFG(object):
    def setupUi(self, UI):
        UI.resize(500, 520)
        self.widget = QtWidgets.QWidget(UI)
        layout = QtWidgets.QVBoxLayout(self.widget)

        # add menu bar
        self.main_menu = self.menuBar()
        self.file_menu = self.main_menu.addMenu('File')

        self.widget.setGeometry(QtCore.QRect(0, 20, 500, 500))
        self.buttonLayout = QtWidgets.QGridLayout(self.widget)

        self.btn_add_column = QtWidgets.QPushButton('Add Column')
        self.btn_add_column.setObjectName('btn_add_column')
        self.btn_delete_column = QtWidgets.QPushButton('Delete Column')
        self.btn_delete_column.setObjectName('btn_delete_column')
        self.btn_add_row = QtWidgets.QPushButton('Add Row')
        self.btn_add_row.setObjectName('btn_add_row')
        self.btn_delete_row = QtWidgets.QPushButton('Delete Row')
        self.btn_delete_row.setObjectName('btn_delete_row')

        self.table = QtWidgets.QTableWidget(2, 4)
        self.buttonLayout.addWidget(self.btn_add_column, 0, 0)
        self.buttonLayout.addWidget(self.btn_delete_column, 0, 1)
        self.buttonLayout.addWidget(self.btn_add_row, 1, 0)
        self.buttonLayout.addWidget(self.btn_delete_row, 1, 1)

        self.buttonCreateCSV = QtWidgets.QPushButton(' Create CSV')
        self.buttonCreateCSV.setObjectName('btn_create_csv')

        layout.addLayout(self.buttonLayout)
        layout.addStretch()
        layout.addWidget(self.table,  QtCore.Qt.AlignTop)
        layout.addWidget(self.buttonCreateCSV)

        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, ItemGenerator):
        ItemGenerator.setWindowTitle(_translate("ItemGenerator", "Dialog", None))
