

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog16(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 607)
        Dialog.setStyleSheet("border-image: url(b.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 18pt \"Bauhaus 93\";\n"
"text-decoration: underline;\n"
"color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.12, stop:0 rgba(22, 179, 218, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(200, -1, 140, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setStyleSheet("font: bold 12px/25px Arial, sans-serif;  \n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.12, stop:0 rgba(118, 198, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"padding:5;\n"
"font: 11pt \"Malgun Gothic\";\n"
"text-decoration: underline;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("  margin: 10px;\n"
"font: bold 12px/25px Arial, sans-serif;  \n"
"border-radius: 10px;\n"
"color: #19667d;\n"
"background: #70c9e3;\n"
"padding:5;\n"
"font: 14pt \"Impact\";\n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setStyleSheet("font: bold 12px/25px Arial, sans-serif;  \n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.12, stop:0 rgba(118, 198, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"padding:5;\n"
"font: 11pt \"Malgun Gothic\";\n"
"text-decoration: underline;")
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Recherche par Classe"))
        self.comboBox.setItemText(1, _translate("Dialog", "CPI-1"))
        self.comboBox.setItemText(2, _translate("Dialog", "CPI-2"))
        self.comboBox.setItemText(3, _translate("Dialog", "ING-1-EL"))
        self.comboBox.setItemText(4, _translate("Dialog", "ING-1-INFO"))
        self.comboBox.setItemText(5, _translate("Dialog", "ING-2-EL"))
        self.comboBox.setItemText(6, _translate("Dialog", "ING-3-EL"))
        self.comboBox.setItemText(7, _translate("Dialog", "L1-EEA"))
        self.comboBox.setItemText(8, _translate("Dialog", "L1-INFO"))
        self.comboBox.setItemText(9, _translate("Dialog", "L1-MATH"))
        self.comboBox.setItemText(10, _translate("Dialog", "L1-TIC"))
        self.comboBox.setItemText(11, _translate("Dialog", "L2-INFO"))
        self.comboBox.setItemText(12, _translate("Dialog", "L2-MATH"))
        self.comboBox.setItemText(13, _translate("Dialog", "L2-TIC"))
        self.comboBox.setItemText(14, _translate("Dialog", "L3-INFO"))
        self.comboBox.setItemText(15, _translate("Dialog", "L3-MATH"))
        self.comboBox.setItemText(16, _translate("Dialog", "L3-TIC"))
        self.comboBox.setItemText(17, _translate("Dialog", "MP-1-GL"))
        self.comboBox.setItemText(18, _translate("Dialog", "MP-1-III"))
        self.comboBox.setItemText(19, _translate("Dialog", "MP-1-SD"))
        self.comboBox.setItemText(20, _translate("Dialog", "MP-2-GL"))
        self.comboBox.setItemText(21, _translate("Dialog", "MR-1-EL"))
        self.comboBox.setItemText(22, _translate("Dialog", "MR-1-GL"))
        self.comboBox.setItemText(23, _translate("Dialog", "MR-2-EL"))
        self.comboBox.setItemText(24, _translate("Dialog", "MR-2-GL"))
        self.pushButton.setText(_translate("Dialog", "Rechrche"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

