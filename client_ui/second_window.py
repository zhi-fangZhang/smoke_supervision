# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1211, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stat = QtWidgets.QListWidget(self.centralwidget)
        self.stat.setGeometry(QtCore.QRect(980, 330, 231, 321))
        self.stat.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stat.setObjectName("stat")
        item = QtWidgets.QListWidgetItem()
        self.stat.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.stat.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.stat.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.stat.addItem(item)
        self.video_browser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.video_browser.setGeometry(QtCore.QRect(500, 0, 711, 331))
        self.video_browser.setObjectName("video_browser")
        self.worker_list = QtWidgets.QTableWidget(self.centralwidget)
        self.worker_list.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.worker_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.worker_list.setObjectName("worker_list")
        self.worker_list.setColumnCount(4)
        self.worker_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.worker_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worker_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.worker_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.worker_list.setHorizontalHeaderItem(3, item)
        self.browser = QtWidgets.QLabel(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(500, 330, 481, 321))
        self.browser.setText("")
        self.browser.setObjectName("browser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.stat.isSortingEnabled()
        self.stat.setSortingEnabled(False)
        item = self.stat.item(0)
        item.setText(_translate("MainWindow", "XX工厂统计数据"))
        item = self.stat.item(1)
        item.setText(_translate("MainWindow", "粉尘总量：0"))
        item = self.stat.item(2)
        item.setText(_translate("MainWindow", "温度：0℃"))
        item = self.stat.item(3)
        item.setText(_translate("MainWindow", "湿度：0"))
        self.stat.setSortingEnabled(__sortingEnabled)
        item = self.worker_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号(查看信息)"))
        item = self.worker_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.worker_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "累计接尘量"))
        item = self.worker_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "危险指数"))
from PyQt5 import QtWebEngineWidgets
