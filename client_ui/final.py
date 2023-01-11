'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-11 17:13:51
LastEditTime: 2023-01-12 02:06:27
'''
import sys
from final_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import signals 
import utils
from threading import Thread
import numpy as np
from PyQt5 import QtGui
import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow  
from PyQt5.QtChart import QChart, QChartView, QLineSeries 

app = QApplication(sys.argv)
is_closed=False
sig=signals.Retrive_signals()



# 业务类需要继承两个类，一个设计的主界面，另一个是QMainWindow
class Window_3(Ui_MainWindow, QMainWindow):
    def __init__(self,id,f_id):
        """
         特别注意（最容易出错）：
         1.派生新类访问基类需要super(),同时它的参数是基类文件下的类及“ui_home_window.py中的 
           Ui_MainWindow类”，
        """
        super(Window_3, self).__init__()
        self.id=id
        self.f_id=f_id
        global is_closed
        is_closed=False
        self.setupUi(self)
        self.retrieve_task()
        sig.win3_retrieve_done.connect(self.render_once)
    

            
    def render_once(self,w,list):
        self.show_info(self.info,list)
        self.show_suggest(self.suggest,list)
        self.show_graph(self.graph,list)
        return

        

    def show_info(self,w,list):
        list=list[0]
        w.item(1).setText("姓名：{}".format(list[0]))
        w.item(2).setText("累计接尘量：{}".format(list[2]))
        w.item(3).setText("预计未来7天接尘量：{}".format(list[3]))
        w.item(4).setText("危险系数：{}".format(list[4]))

    def show_suggest(self,w,list):
        w.setPlainText('症状较轻，注意防护')


    def show_graph(self,w,list):
        c=QChart()
        lineSeries = QLineSeries()
        for i in range(len(list)):
            lineSeries.append(i,list[i][2])
        c.legend().hide()        
        c.addSeries(lineSeries)
        c.createDefaultAxes()   
        c.setTitle('一个简单的折线图示例')                 
        w.setChart(c)        
        w.setRenderHint(QPainter.Antialiasing)                

    def retrieve_task(self):
        sqls=[
            f'''
            SELECT wi.name,wa.time,wa.accumulate_dust,wa.anticipated_dust,wa.is_danger
            from worker_info as wi
            NATURAL JOIN worker_alert wa
            WHERE wi.id={self.id} AND wi.f_id={self.f_id}
            ORDER BY time DESC
            LIMIT 30;
            '''
        ]
        sigs=[sig.win3_retrieve_done]
        widgets=[self.graph]
        ret=utils.Retriever()
        ret.fetch_once(sqls,sigs,widgets)
