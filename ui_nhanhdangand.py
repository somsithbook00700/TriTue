# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nhanhdanganh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1692, 891)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_input_name = QLabel(self.centralwidget)
        self.label_input_name.setObjectName(u"label_input_name")
        self.label_input_name.setGeometry(QRect(120, 30, 911, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_input_name.setFont(font)
        self.pushButton_browse = QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(30, 30, 81, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 451, 721))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setLineWidth(0)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(520, 70, 20, 721))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 70, 451, 721))
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(True)
        self.pushButton_nhandang = QPushButton(self.centralwidget)
        self.pushButton_nhandang.setObjectName(u"pushButton_nhandang")
        self.pushButton_nhandang.setGeometry(QRect(490, 400, 81, 61))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(1040, 70, 451, 661))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(1270, 740, 221, 51))
        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(1040, 740, 221, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1692, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_input_name.setText("")
        self.pushButton_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton_nhandang.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

