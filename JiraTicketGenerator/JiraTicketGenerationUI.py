# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pfg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
    def setupUi(self, PFG):
        PFG.setObjectName(_fromUtf8("PFG"))
        PFG.resize(278, 160)
        self.widget = QtWidgets.QWidget(PFG)
        self.widget.setGeometry(QtCore.QRect(0, 0, 271, 150))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createButton = QtWidgets.QPushButton(self.widget)
        self.createButton.setObjectName(_fromUtf8("create"))
        self.horizontalLayout.addWidget(self.createButton)
#        self.closeButton = QtWidgets.QPushButton(self.widget)
#        self.closeButton.setObjectName(_fromUtf8("close"))
#        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(PFG)
        QtCore.QMetaObject.connectSlotsByName(PFG)

    def retranslateUi(self, PFG):
        PFG.setWindowTitle(_translate("PFG", "Dialog", None))
        self.radioButton_3.setText(_translate("PFG", "Prototypfreigabe", None))
        self.radioButton.setText(_translate("PFG", "Vorserienfreigabe", None))
        self.radioButton_2.setText(_translate("PFG", "Serienfreigabe", None))
        self.createButton.setText(_translate("PFG", "Erstelle CSV", None))
#        self.closeButton.setText(_translate("PFG", "Schließen", None))
