import cv2
from cv_show import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow , Ui_MainWindow):
    def __init__(self ):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.cam_time = QtCore.QTimer()
        self.open_cam.clicked.connect()
        self.close_cam.connect()

    def start_grap(self):
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0

