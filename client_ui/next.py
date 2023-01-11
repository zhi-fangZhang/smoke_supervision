'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-11 17:13:51
LastEditTime: 2023-01-12 02:02:47
'''
import sys
import final
from second_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import signals 
import utils
import PyQt5
import sip
import time
import folium
from threading import Thread
import io
import numpy as np
import cv2
from PyQt5 import QtGui

app = QApplication(sys.argv)
is_closed=False
sig=signals.Retrive_signals()

class Break_Retriever(utils.Retriever):
    def __init__(self) -> None:
        super().__init__()
    def fetch_every_time_with_break(self,sqls,signals,widgets):
        def th():
            if len(sqls)!=len(signals) or len(sqls)!=len(widgets):
                raise Exception()
            while True:
                global is_closed
                if is_closed==True:
                    break
                bret.fetch_now(sqls,signals,widgets)
                time.sleep(10)               
            th = Thread(target=th,args=())
            th.setDaemon(True)
            th.start()


bret=Break_Retriever()


# 业务类需要继承两个类，一个设计的主界面，另一个是QMainWindow
class Window_2(Ui_MainWindow, QMainWindow):
    def __init__(self,f_id):
        """
         特别注意（最容易出错）：
         1.派生新类访问基类需要super(),同时它的参数是基类文件下的类及“ui_home_window.py中的 
           Ui_MainWindow类”，
        """
        super(Window_2, self).__init__()
        self.f_id=f_id
        global is_closed
        is_closed=False
        self.setupUi(self)
        self.retrieve_task()
        sig.win2_workerlist_retrieve.connect(self.show_workerlist)
        sig.win2_stat_retrieve.connect(self.show_stat)
        sig.win2_sensor_pos_retrieve.connect(self.show_sensor_graph)
        self.worker_list.doubleClicked.connect(self.final_trigger)
    
    def final_trigger(self,index):
        if index.column()==0:
            table_column = index.column()
            table_row = index.row()
            current_item = self.worker_list.item(table_row, table_column)
            txt=current_item.text()
            self.another_window = final.Window_3(int(txt),self.f_id)
            self.another_window.show()
            
            
        
    def closeEvent(self, a0) -> None:
        sip.delete(self.worker_list)
        global is_closed
        is_closed=True
        return super().closeEvent(a0)

    def show_workerlist(self,w,list):
        # w = self.findChild(QtWidgets.QTableWidget, 'worker_list')
        w.setRowCount(0)
        for i in range(len(list)):
            row_count = w.rowCount()  # 返回当前行数(尾部)
            w.insertRow(row_count)  # 尾部插入一行
            for j in range(0,len(list[i])):
                w.setItem(i, j, PyQt5.QtWidgets.QTableWidgetItem(str(list[i][j])))


    def show_stat(self,w,list):
        list=list[0]
        w.item(1).setText("粉尘总量：{}".format(list[0]))
        w.item(2).setText("平均温度：{}℃".format(list[1]))
        w.item(3).setText("平均湿度：{}".format(list[2]))


    def show_sensor_graph(self,w,list):
        wl,ww=w.width(),w.height()
        img = np.zeros((ww, wl, 3), np.uint8)
        img.fill(230)
        for item in list:
            x=float(item[3])/float(item[1])*wl
            y=float(item[4])/float(item[2])*ww
            img=cv2.circle(img,(int(x),int(y)),3,(0,0,0),6)
            img=cv2.putText(img,f'#{item[0]}',(int(x),int(y)+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
            img=cv2.putText(img,f'{item[5]}/mmol',(int(x),int(y)+35),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)


        def dis_img(w,img_org):
            shrink = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)
            qt_img = QtGui.QImage(shrink.data, # 数据源
                              shrink.shape[1],  # 宽度
                              shrink.shape[0],	# 高度
                              shrink.shape[1] * 3, # 行字节数
                              QtGui.QImage.Format_RGB888)
            w.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            w.show()
            
        dis_img(w,img)

    def retrieve_task(self):
        sqls=[
            f'''
            SELECT id,name,accumulate_dust,is_danger
            FROM (SELECT id,f_id,max(time) as time FROM worker_alert GROUP BY id,f_id) w
            NATURAL JOIN worker_alert w 
            NATURAL JOIN worker_info
            WHERE w.f_id={self.f_id};
            ''',
            f'''
            SELECT SUM(concentration),AVG(temperature),AVG(humidity)
            FROM sensor_spvs
            GROUP BY f_id
            HAVING f_id={self.f_id};
            ''',

            f'''
            SELECT s.id,f.length,f.width,s.x,s.y,ss.concentration
            FROM (SELECT id,f_id,max(time) as time FROM sensor_spvs GROUP BY id,f_id) s
            NATURAL JOIN sensor_spvs ss
            NATURAL JOIN sensor_info s
            JOIN factory_info f on s.f_id=f.f_id
            WHERE s.f_id={self.f_id};
            '''
        ]
        sigs=[sig.win2_workerlist_retrieve,sig.win2_stat_retrieve,sig.win2_sensor_pos_retrieve]
        widgets=[self.worker_list,self.stat,self.browser]
        bret.fetch_once(sqls,sigs,widgets)
        bret.fetch_every_time_with_break([sqls[0]],[sigs[0]],[widgets[0]])
    
        
if __name__ == '__main__':

    my_windows = Window_2(1)  # 实例化对象
    my_windows.show()  # 显示窗口
    sys.exit(app.exec_())