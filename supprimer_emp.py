
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 508)
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
        self.horizontalLayout_2.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("font: 16pt \"Gloucester MT Extra Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setStyleSheet("font: bold 12px/25px Arial, sans-serif;  \n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.12, stop:0 rgba(118, 198, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"padding:5;\n"
"font: 11pt \"Malgun Gothic\";\n"
"text-decoration: underline;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(8)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("font: 16pt \"Gloucester MT Extra Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setStyleSheet("font: bold 12px/25px Arial, sans-serif;  \n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.12, stop:0 rgba(118, 198, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"padding:5;\n"
"font: 11pt \"Malgun Gothic\";\n"
"text-decoration: underline;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(200, -1, 200, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
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
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Supprimer Emprunt"))
        self.label_2.setText(_translate("Dialog", "N° d\'inscription:"))
        self.label_3.setText(_translate("Dialog", "Référence:"))
        self.pushButton.setText(_translate("Dialog", "Supprimer"))
