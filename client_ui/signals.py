'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-11 10:33:28
LastEditTime: 2023-01-12 01:56:39
'''
from PySide2.QtCore import Signal,QObject
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTableWidget,QListWidget,QWidget,QLabel
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtChart import QChart, QChartView, QLineSeries 




class Retrive_signals(QObject):
    win1_online_retrive_done=Signal(QListWidget,list)
    win1_alert_retrive_done=Signal(QTableWidget,list)
    win1_factory_info_retrive_done=Signal(QWebEngineView,list)
    win1_click_marker = Signal(QWidget, str)
    win2_workerlist_retrieve=Signal(QTableWidget,list)
    win2_stat_retrieve=Signal(QListWidget,list)
    win2_sensor_pos_retrieve=Signal(QLabel,list)
    win3_retrieve_done=Signal(QChartView,list)
    
    # win1_click_on_marker=InformationWebPageConsole().marker_clicked
    