'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 15:42:34
LastEditTime: 2023-01-12 15:43:40
'''

from PyQt5.QtWidgets import QApplication
from main import Window_1
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_windows = Window_1()
    my_windows.show() 

    sys.exit(app.exec_())