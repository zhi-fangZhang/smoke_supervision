'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 16:06:32
LastEditTime: 2023-01-11 23:20:57
'''
#coding=utf-8
import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMessageBox
import io
import utils
import signals
import PyQt5.QtWidgets
import os
import sys
import folium
import json
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import (
    QGridLayout, QPushButton, QFrame, QSplitter, QHBoxLayout, QScrollArea, QLabel, QComboBox, QFileDialog, QMessageBox,
    QWidget, QApplication
)
from branca.element import Element
from threading import Thread
import next

####################### 全局变量#########################
app = QApplication(sys.argv)
sig=signals.Retrive_signals()




class InformationWebPageConsole(QWebEnginePage):

    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        sig.win1_click_marker.emit(self,msg)




class Window_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.another_window=None
        super(Window_1, self).__init__()
        self.setupUi(self)
        self.retrieve_task()
        sig.win1_online_retrive_done.connect(self.list_widget_online_update)
        sig.win1_alert_retrive_done.connect(self.table_widget_alert_update)
        sig.win1_factory_info_retrive_done.connect(self.load_browser)
        sig.win1_click_marker.connect(self.click_on_marker)



    def click_on_marker(self,w,str):
        self.another_window = next.Window_2(int(str))
        self.another_window.show()
    



    def list_widget_online_update(self,w,list):
        w.item(1).setText("工厂数量：{}".format(*list[0]))
        w.item(2).setText("工人数量：{}".format(*list[1]))
        w.item(3).setText("传感器数量：{}".format(*list[2]))

    def table_widget_alert_update(self,w,list):
        w.setRowCount(0)
        for i in range(len(list)):
            row_count = w.rowCount()  # 返回当前行数(尾部)
            w.insertRow(row_count)  # 尾部插入一行
            for j in range(0,len(list[i])):
                w.setItem(i, j, PyQt5.QtWidgets.QTableWidgetItem(str(list[i][j])))


    def load_browser(self,w,listf):
        # 加载初始地图并加载点击控件信号
        tiles= 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7'
        m = folium.Map(location=[35.3, 100.6], zoom_start=4,attr='高德-常规图',tiles=tiles,
        max_bounds=True,no_touch=True,zoom_control=False)
        mak_js=[]
        for i,l in enumerate(listf):
            mak=folium.Marker(list(map(lambda x:float(x),l[2:])),
                popup=l[1],
                icon=folium.Icon(color='green'))
            mak.add_to(m) 
            mak_js.append((mak.get_name(),l[0]))
        
        m = self.add_customjs(m,mak_js)
        data = io.BytesIO()
        m.save(data, close_file=False)
        page = InformationWebPageConsole(self)
        w.setPage(page)
        w.setHtml(data.getvalue().decode())
        
 
    def add_customjs(self, map_object,mak_js):
        my_js=''         
        for js in mak_js:
            my_js+=f"""{js[0]}.on("click",
                 function (e) {{
                    console.log({js[1]})}});"""
        e = Element(my_js)
        html = map_object.get_root()
        html.script.get_root().render()
        # Insert new element or custom JS
        html.script._children[e.get_name()] = e
        return map_object
    

    def retrieve_task(self):
        sqls=[
            '''
            SELECT f_id,name,longitude,latitude
            FROM factory_info;
            ''',
            '''
            SELECT COUNT(*) FROM factory_info
            UNION all
            SELECT COUNT(*) FROM worker_info
            UNION all
            SELECT COUNT(*) FROM sensor_info;
            ''',
            '''
            SELECT name,id,content 
            FROM (SELECT id,f_id,max(time) as time FROM sensor_alert GROUP BY id,f_id) s 
            NATURAL JOIN sensor_alert s 
            NATURAL JOIN factory_info;
            '''
        ]
        sigs=[sig.win1_factory_info_retrive_done,sig.win1_online_retrive_done,sig.win1_alert_retrive_done]
        widgets=[self.browser,self.list_widget_online,self.list_widget_alert]
        ret=utils.Retriever()
        ret.fetch_once(sqls,sigs,widgets)
        ret.fetch_every_time([sqls[2]],[sigs[2]],[widgets[2]])
        



if __name__ == '__main__':

    my_windows = Window_1()  # 实例化对象
    my_windows.show()  # 显示窗口

    sys.exit(app.exec_())
