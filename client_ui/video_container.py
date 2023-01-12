'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 16:00:57
LastEditTime: 2023-01-12 16:42:05
'''
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import cv2
import sys


class  VideoGui(QLabel):
    # 定义构造方法
    def __init__(self,MainWindow):
        QLabel.__init__(self)
        self.timer_camera = QTimer()
        self.open_video()
        self.Btn_Start()

    def Btn_Start(self):
        # 定时器开启，每隔一段时间，读取一帧
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.OpenFrame)

    def open_video(self):
        """选取视频文件"""
        # 这里以mp4和avi视频播放为例
        openfile_name='./video/example.mp4'
        self.file_name = openfile_name  # 获取图片名称
        # 得到文件后缀名  需要根据情况进行修改
        suffix = self.file_name.split("/")[-1][self.file_name.split("/")[-1].index(".") + 1:]
        if self.file_name == '':
            pass
        elif suffix == "mp4" or suffix == "avi":
            self.cap = cv2.VideoCapture(self.file_name)

    def OpenFrame(self):
        ret, image = self.cap.read()
        print(1)
        if ret:
            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                video_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            elif len(image.shape) == 1:
                 video_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Indexed8)
            else:
                 video_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            self.setPixmap(QPixmap(video_img))
            self.setScaledContents(True)  # 自适应窗口
        else:
            self.cap.release()
            self.timer_camera.stop()

    # 界面关闭事件，询问用户是否关闭
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', "是否要退出该界面？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            event.accept()
        else:
            event.ignore()
