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
        self.label_input_name.setGeometry(QRect(150, 30, 911, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_input_name.setFont(font)
        self.pushButton_browse = QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(30, 30, 101, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.pushButton_browse.setFont(font1)
        self.pushButton_browse.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(630, 70, 451, 721))
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(True)
        self.pushButton_nhandang = QPushButton(self.centralwidget)
        self.pushButton_nhandang.setObjectName(u"pushButton_nhandang")
        self.pushButton_nhandang.setGeometry(QRect(490, 300, 131, 61))
        self.pushButton_nhandang.setFont(font1)
        self.pushButton_nhandang.setCursor(QCursor(Qt.PointingHandCursor))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(1090, 70, 451, 661))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(1320, 740, 221, 51))
        self.pushButton_clear.setFont(font1)
        self.pushButton_clear.setStyleSheet(u"font-size: 14;\n"
"")
        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(1090, 740, 221, 51))
        self.pushButton_save.setFont(font1)
        self.pushButton_save.setStyleSheet(u"font-size: 14;\n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(490, 390, 131, 61))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 20, 131, 31))
        self.comboBox.setFont(font1)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"padding-left: 28px;\n"
"text-align: center;")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 460, 131, 61))
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(0, 20, 131, 31))
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(u"padding-left: 28px;\n"
"text-align: center;")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton_nhandang.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Vietnam", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Thailand", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Digit", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Just text", None))

    # retranslateUi

