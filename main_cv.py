import cv2
import sys
import time
from cv_show import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyMainWindow(QMainWindow , Ui_MainWindow):
    def __init__(self ):
        super(MyMainWindow, self).__init__()
        self.mear_step = 20
        self.setupUi(self)
        self.start_time1 = time.time()
        self.start_time2 = time.time()
        self.frame1=0
        self.frame2=0
        self.cam_time = QtCore.QTimer()
        self.cam_time2 = QtCore.QTimer()
        self.cam_time.timeout.connect(self.show_pic)
        self.cam_time2.timeout.connect(self.show_pic2)
        self.horizontalSlider.valueChanged.connect(self.moveline)
        self.actionExit.triggered.connect(self.close)
        self.action_1.triggered.connect(self.start_grap)
        self.action_2.triggered.connect(self.start_grap2)
    #移动滑块调节指示线位置
    def moveline(self):
        sta_x = self.horizontalSlider.x()
        sta_y = self.line_2.y()
        length = float(self.horizontalSlider.width()) / 100.0
        sta = sta_x + length/3
        val = self.horizontalSlider.value()
        self.line.move(sta + val*length + val/15 - self.mear_step/2 , sta_y)
        self.line_2.move(sta + val*length + val/15 + self.mear_step/2 , sta_y)

    def start_grap(self):
        self.start_time1 = time.time()
        self.frame1=0
        self.cap1 = cv2.VideoCapture(1+ cv2.CAP_DSHOW)
        self.cam_time.start(60)

    def start_grap2(self):
        self.start_time2 = time.time()
        self.frame2=0
        self.cap2 = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        self.cam_time2.start(60)

    def stop_cam(self):
        self.cap1.release()
        self.cam_time.stop()

    def show_pic(self):
        ret, img = self.cap1.read()
        if not ret:
            print('read error!\n')
            return
        #cv2.flip(img, 1, img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label.setPixmap(pixmap)
        end_time1 = time.time()
        diff_time1 = (end_time1 - self.start_time1)
        self.frame1 = self.frame1 + 1
        if diff_time1>1:
            self.start_time1 = end_time1
            self.label_6.setText('帧率(1):' + str(self.frame1))
            self.frame1 = 0

    def show_pic2(self):
        ret_2, img_2 = self.cap2.read()
        if not ret_2:
            print('read error!\n')
            return
        cv2.flip(img_2, 1, img_2)
        cur_frame = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label_2.setPixmap(pixmap)
        end_time2 = time.time()
        diff_time2 = (end_time2 - self.start_time2)
        self.frame2 = self.frame2 + 1
        if diff_time2 > 1:
            self.start_time2 = end_time2
            self.label_8.setText('帧率(2):' + str(self.frame2))
            self.frame2 = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.showFullScreen()
    sys.exit(app.exec_())