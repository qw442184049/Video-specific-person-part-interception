# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainUI(object):
    def setupUi(self, MainUI):
        MainUI.setObjectName("MainUI")
        MainUI.resize(660, 436)
        self.gridLayout_2 = QtWidgets.QGridLayout(MainUI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(MainUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(640, 260))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.SelectFileButton = QtWidgets.QPushButton(self.groupBox)
        self.SelectFileButton.setGeometry(QtCore.QRect(20, 25, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectFileButton.sizePolicy().hasHeightForWidth())
        self.SelectFileButton.setSizePolicy(sizePolicy)
        self.SelectFileButton.setMinimumSize(QtCore.QSize(91, 31))
        self.SelectFileButton.setObjectName("SelectFileButton")
        self.SelectFiletEdit = QtWidgets.QTextEdit(self.groupBox)
        self.SelectFiletEdit.setGeometry(QtCore.QRect(120, 25, 501, 31))
        self.SelectFiletEdit.setMinimumSize(QtCore.QSize(501, 31))
        self.SelectFiletEdit.setObjectName("SelectFiletEdit")
        self.OutDirEdit = QtWidgets.QTextEdit(self.groupBox)
        self.OutDirEdit.setGeometry(QtCore.QRect(120, 72, 501, 31))
        self.OutDirEdit.setMinimumSize(QtCore.QSize(501, 31))
        self.OutDirEdit.setObjectName("OutDirEdit")
        self.OutDirButton = QtWidgets.QPushButton(self.groupBox)
        self.OutDirButton.setGeometry(QtCore.QRect(20, 72, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutDirButton.sizePolicy().hasHeightForWidth())
        self.OutDirButton.setSizePolicy(sizePolicy)
        self.OutDirButton.setMinimumSize(QtCore.QSize(91, 31))
        self.OutDirButton.setObjectName("OutDirButton")
        self.DisplayBox = QtWidgets.QCheckBox(self.groupBox)
        self.DisplayBox.setGeometry(QtCore.QRect(130, 140, 281, 31))
        self.DisplayBox.setObjectName("DisplayBox")
        self.StartButton = QtWidgets.QPushButton(self.groupBox)
        self.StartButton.setGeometry(QtCore.QRect(20, 130, 91, 51))
        self.StartButton.setObjectName("StartButton")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(MainUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(640, 150))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_3.setMinimumSize(QtCore.QSize(491, 115))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_3.addWidget(self.textEdit_3, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(111, 115))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(MainUI)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

    def retranslateUi(self, MainUI):
        _translate = QtCore.QCoreApplication.translate
        MainUI.setWindowTitle(_translate("MainUI", "Form"))
        self.groupBox.setTitle(_translate("MainUI", "操作"))
        self.SelectFileButton.setText(_translate("MainUI", "选取视频"))
        self.OutDirButton.setText(_translate("MainUI", "保存路径"))
        self.DisplayBox.setText(_translate("MainUI", "显示视频（不建议勾取，会降低速度）"))
        self.StartButton.setText(_translate("MainUI", "开始"))
        self.groupBox_2.setTitle(_translate("MainUI", "日志"))
        self.pushButton_3.setText(_translate("MainUI", "清除"))

if __name__=="__main__":
    import sys
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()

    ui = Ui_MainUI()
    ui.setupUi(widget)

    widget.show()
    sys.exit(app.exec_())