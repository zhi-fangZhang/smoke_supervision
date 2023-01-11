# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PyQt5.QtChart import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 732)
        self.window_3 = QWidget(MainWindow)
        self.window_3.setObjectName(u"window_3")
        self.graph = QChartView(self.window_3)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(0, 0, 911, 681))
        self.info = QListWidget(self.window_3)
        QListWidgetItem(self.info)
        QListWidgetItem(self.info)
        QListWidgetItem(self.info)
        QListWidgetItem(self.info)
        QListWidgetItem(self.info)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(910, 0, 261, 301))
        self.info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.suggest = QPlainTextEdit(self.window_3)
        self.suggest.setObjectName(u"suggest")
        self.suggest.setGeometry(QRect(910, 300, 261, 381))
        self.suggest.setReadOnly(True)
        MainWindow.setCentralWidget(self.window_3)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.info.isSortingEnabled()
        self.info.setSortingEnabled(False)
        ___qlistwidgetitem = self.info.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u60c5\u51b5", None));
        ___qlistwidgetitem1 = self.info.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\uff1a", None));
        ___qlistwidgetitem2 = self.info.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7d2f\u8ba1\u63a5\u5c18\u91cf\uff1a", None));
        ___qlistwidgetitem3 = self.info.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8ba1\u672a\u67657\u5929\u63a5\u5c18\u91cf\uff1a", None));
        ___qlistwidgetitem4 = self.info.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5371\u9669\u7cfb\u6570\uff1a", None));
        self.info.setSortingEnabled(__sortingEnabled)

    # retranslateUi

